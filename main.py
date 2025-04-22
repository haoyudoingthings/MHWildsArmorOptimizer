from classes import *
from data import *
from functools import reduce
from itertools import product
from heapq import heappush, heappushpop
from tqdm import tqdm
from wakepy import keep
from joblib import Parallel, delayed
from tqdm_joblib import tqdm_joblib


def combinations_with_limited_replacement(objects, quantities, n):
    def backtrack(combo, start_idx, remaining):
        if remaining == 0:
            yield combo.copy()
            return
        
        for i in range(start_idx, len(objects)):
            # Count how many of this object we've already used
            used = sum(1 for item in combo if item is objects[i])
            
            # If we haven't used all available of this object
            if used < quantities[i]:
                combo.append(objects[i])
                # Stay at same index i to allow reuse
                yield from backtrack(combo, i, remaining - 1)
                combo.pop()
    
    yield from backtrack([], 0, n)

def process_armor_combo(weapon_and_armors, must_have_skills_armor_only, must_have_skills_deco_avail, all_decos, deco_quantity):
    armorset_no_deco = sum(weapon_and_armors, None)
    # minimum skill requirement check 1
    if any(armorset_no_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_armor_only.items()):
        return None
    empty_slots = armorset_no_deco.get_empty_slots()
    
    best_result = None
    for deco_combo in combinations_with_limited_replacement(all_decos+[None], deco_quantity+[sum(empty_slots)], sum(empty_slots)):
        slots_taken = [0] * MAX_DECO_LVL
        for deco in deco_combo:
            if deco is not None:
                slots_taken[deco.lvl-1] += 1
        if any(sum(slots_taken[i:]) > sum(empty_slots[i:]) for i in range(MAX_DECO_LVL)):
            continue

        armorset_with_deco = sum([armorset_no_deco] + list(deco_combo), None)
        if any(armorset_with_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_deco_avail.items()):
            continue
            
        if best_result is None or armorset_with_deco > best_result:
            best_result = armorset_with_deco
            
    return best_result


def main():
    n_jobs = -3
    # TODO: refactor configs into another file
    top_n = 10
    weapons = [ # Meat: +2; Powercharm: +6; Demondrug: +7; Mega Demondrug: +10
        Weapon(220 + 15, 0.05, 0.4), 
    ]
    must_have_skills = {}

    all_decos = []
    deco_quantity = []
    for deco in Decoration.all.values():
        all_decos.append(deco)
        deco_quantity.append(deco.tot_amount)
    armors_by_part = {s: Armor.get_all_armors_by_part(s) for s in ARMOR_PART_NAMES}
    must_have_skills_deco_avail = {}
    for deco in all_decos:
        for skill in deco.skills.keys():
            if skill in must_have_skills:
                must_have_skills_deco_avail[skill] = must_have_skills[skill]
    must_have_skills_armor_only = {k: v for k, v in must_have_skills.items() if k not in must_have_skills_deco_avail}

    armor_combinations = list(product(weapons, *[armors_by_part[k].values() for k in ARMOR_PART_NAMES]))
    
    with tqdm_joblib(total=len(armor_combinations)):
        results = Parallel(n_jobs=n_jobs)(
            delayed(process_armor_combo)(
                combo, 
                must_have_skills_armor_only,
                must_have_skills_deco_avail,
                all_decos,
                deco_quantity
            )
            for combo in armor_combinations
        )
    
    # Filter out None results and get top N
    results = [r for r in results if r is not None]
    results_top_n = []
    for armorset in results:
        if len(results_top_n) < top_n:
            heappush(results_top_n, armorset)
        else:
            heappushpop(results_top_n, armorset)
    results_top_n.sort(reverse=True)

    for armorset in results_top_n:
        print(f"\nEffective Raw: {armorset.get_eff_atk():.4f}")
        print("Weapon: ", armorset.weapon)
        print("Helm:   ", armorset.parts['helm'])
        print("Mail:   ", armorset.parts['mail'])
        print("Braces: ", armorset.parts['braces'])
        print("Coil:   ", armorset.parts['coil'])
        print("Greaves:", armorset.parts['greaves'])
        print("Charm:  ", armorset.parts['charm'])
        print("Decos:  ", ' '.join([str(d) for d in armorset.decos]))
        print("===== Total skills =====")
        for i, (k, v) in enumerate(armorset.get_all_skill_lvls().items()):
            print(f"{str(k) + ' ' + str(v): <30}", end='\n' if i % 3 == 2 else '')
        print("")


if __name__ == '__main__':
    with keep.running():
        main()

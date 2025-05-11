from classes import *
from data import *
from config import *
from itertools import product
from heapq import heappush, heappushpop
from math import ceil
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

def process_armor_combo(weapon_and_armors, must_have_skills_armor_only, must_have_skills_deco_avail, all_decos0, deco_quantity0):
    armorset_no_deco = sum(weapon_and_armors, None)
    # minimum skill requirement check 1
    if any(armorset_no_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_armor_only.items()):
        return None

    all_decos = all_decos0.copy()
    deco_quantity = deco_quantity0.copy()
    for i, deco in enumerate(all_decos):
        if all(skill.is_util and skill not in must_have_skills_deco_avail for skill in deco.skills.keys()):
            deco_quantity[i] = 0
            continue
        deco_quantity[i] = min(
            deco_quantity[i], 
            max(ceil(((skill.tot_lvls() if not skill.is_util else must_have_skills_deco_avail[skill]) - \
                      armorset_no_deco.get_skill_lvl(skill)) / skill_lvl) for skill, skill_lvl in deco.skills.items())
        )
    for i in range(len(deco_quantity)-1, -1, -1):
        if deco_quantity[i] == 0:
            deco_quantity.pop(i)
            all_decos.pop(i)
    
    empty_slots = armorset_no_deco.get_empty_slots()
    deco_quantity_for_each_slot_lvl = [0] * MAX_DECO_LVL
    for deco, deco_cnt in zip(all_decos, deco_quantity):
        deco_quantity_for_each_slot_lvl[deco.lvl-1] += deco_cnt
    excess_decos = 0
    num_no_deco_slots = 0
    for s, d in zip(empty_slots, deco_quantity_for_each_slot_lvl):
        excess_decos += d - s
        if excess_decos < 0:
            num_no_deco_slots += -excess_decos
            excess_decos = 0

    best_result = None
    for deco_combo in combinations_with_limited_replacement(
        all_decos if num_no_deco_slots <= 0 else all_decos + [None], 
        deco_quantity if num_no_deco_slots <= 0 else deco_quantity + [num_no_deco_slots], 
        sum(empty_slots), 
    ):
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
    weapons = [Weapon(w['raw'], w['aff'], w['crit_bonus'], w['name']) for w in WEAPONS]
    must_have_skills = {Skill.all[k]: v for k, v in MUST_HAVE_SKILLS.items()}

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
        results = Parallel(n_jobs=N_JOBS)(
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
        if len(results_top_n) < KEEP_TOP_N:
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

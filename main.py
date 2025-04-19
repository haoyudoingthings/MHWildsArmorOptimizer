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

# def get_deco_combinations(slots, available_decos, armor_skills):
#     remaining_slots = slots
#     remaining_decos_by_lvl = available_decos
#     current_skills = armor_skills
#     searched_used_decos = {}
#     def recursive(used_decos):
#         if sum(remaining_slots) == 0:
#             return
#         new_remaining_slots = list(remaining_slots)
#         if remaining_slots[0] > 0 and len(remaining_decos_by_lvl[0]) > 0:
#             new_remaining_slots[0] -= 1
#             for deco, num in remaining_decos_by_lvl[0]:
#                 if num == 1:
#                     del remaining_decos_by_lvl[0][deco]
#                 else:
#                     remaining_decos_by_lvl[0][deco] -= 1
#                 for skill, skill_lvl in deco.skills:
#                     current_skills[skill] += skill_lvl
#                     yield from recursive(used_decos | {deco})
#                     if 
#                     current_skills[skill] -= 

def get_deco_combinations_iterator(slots, available_decos):
    """
    Generate all possible combinations of decorations that maximize slot usage.
    
    Args:
        slots: List [a, b, c] where a = number of level-1 slots,
                               b = number of level-2 slots,
                               c = number of level-3 slots
        available_decos: Dictionary {Decoration: count} with available decorations
    
    Yields:
        Valid combinations, where each combination is a list of Decoration objects
        (None means empty slot)
    """
    # Convert the slots format [a, b, c] to a flat list of levels
    flat_slots = []
    for level, count in enumerate(slots, 1):
        flat_slots.extend([level] * count)
    
    # Sort slots by level (highest first) for optimal filling
    flat_slots.sort(reverse=True)
    
    # Group decorations by level for easier access
    deco_by_level = {1: [], 2: [], 3: []}
    for deco, count in available_decos.items():
        deco_by_level[deco.lvl].append((deco, count))
    
    seen = set()
    current = [None] * len(flat_slots)
    remaining_decos = {deco: count for deco, count in available_decos.items()}
    
    def recursive_generate(slot_idx):
        # Base case: all slots have been considered
        if slot_idx == len(flat_slots):
            # Check if it's maximal (no more decos can be added)
            is_maximal = True
            for i, slot_level in enumerate(flat_slots):
                if current[i] is None:  # Empty slot
                    for level in range(1, min(slot_level, 3) + 1):
                        for deco, count in deco_by_level[level]:
                            if remaining_decos[deco] > 0:
                                is_maximal = False
                                break
                        if not is_maximal:
                            break
                if not is_maximal:
                    break
            
            if is_maximal:
                # Create a combination signature for deduplication
                combo_key = tuple(d.name if d else None for d in current)
                if combo_key not in seen:
                    seen.add(combo_key)
                    yield current.copy()
            return
        
        # Get the level of the current slot
        slot_level = flat_slots[slot_idx]
        
        # Try each decoration that can fit in this slot
        for level in range(min(slot_level, 3), 0, -1):
            for deco, _ in deco_by_level[level]:
                if remaining_decos[deco] > 0:
                    # Place the deco
                    current[slot_idx] = deco
                    remaining_decos[deco] -= 1
                    
                    # Recursively generate combinations for the next slot
                    yield from recursive_generate(slot_idx + 1)
                    
                    # Backtrack: remove the deco
                    remaining_decos[deco] += 1
                    current[slot_idx] = None
        
        # Also try leaving this slot empty
        current[slot_idx] = None
        yield from recursive_generate(slot_idx + 1)
    
    # Start the recursive generation
    yield from recursive_generate(0)

def main():
    # TODO: refactor configs into another file
    top_n = 20
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
    
    # # parallelization
    # all_armorset_no_deco = [sum(tup, None) for tup in product(weapons, *[armors_by_part[k].values() for k in ARMOR_PART_NAMES])]
    # def fill_deco_and_check_must_have_skills(armorset_no_deco):
    #     if any(armorset_no_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_armor_only.items()):
    #         return []
    #     empty_slots = armorset_no_deco.get_empty_slots()
        
    #     res = []
    #     for deco_combo in combinations_with_limited_replacement(all_decos+[None], deco_quantity+[sum(empty_slots)], sum(empty_slots)):
    #         # check if there's enough slots
    #         slots_taken = [0] * MAX_DECO_LVL
    #         for deco in deco_combo:
    #             if deco is not None:
    #                 slots_taken[deco.lvl-1] += 1
    #         if any(sum(slots_taken[i:]) > sum(empty_slots[i:]) for i in range(MAX_DECO_LVL)):
    #             continue

    #         armorset_with_deco = sum([armorset_no_deco] + list(deco_combo), None)

    #         # minimum skill requirement check 2
    #         if not any(armorset_with_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_deco_avail.items()):
    #             res.append(armorset_with_deco)
        
    #     return res
    
    # with tqdm_joblib(tqdm(total=len(all_armorset_no_deco))) as progress_bar:
    #     tmp = Parallel(n_jobs=n_jobs)(delayed(fill_deco_and_check_must_have_skills)(armorset) for armorset in all_armorset_no_deco)
    
    # all_armorset_with_deco = sum(tmp, [])
    # with tqdm_joblib(tqdm(total=len(all_armorset_with_deco))) as progress_bar:
    #     eff_atks = Parallel(n_jobs=n_jobs)(delayed(lambda x: x.get_eff_atk())(armorset) for armorset in all_armorset_with_deco)
    # # for armorset, eff_atk in tqdm(zip(all_armorset_with_deco, eff_atks)):
    # #     armorset.eff_atk = eff_atk
    
    # results = []
    # for armorset in tqdm(all_armorset_with_deco):
    #     if len(results) < top_n:
    #         heappush(results, armorset)
    #     else:
    #         heappushpop(results, armorset)

    # TODO: efficiency of armor search can still be improved
    available_decos = {deco: deco.tot_amount for deco in Decoration.all.values()}
    results = []
    for weapon_and_armors in tqdm(
        product(weapons, *[armors_by_part[k].values() for k in ARMOR_PART_NAMES]), 
        total=reduce(lambda a, b: a * b, [len(weapons)] + [len(l) for l in armors_by_part.values()])
    ):
        armorset_no_deco = sum(weapon_and_armors, None)
        # minimum skill requirement check 1
        if any(armorset_no_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_armor_only.items()):
            continue
        empty_slots = armorset_no_deco.get_empty_slots()
        
        # TODO: this part can definitely be sped up
        # Use DFS? From low lvl slots up?
        for deco_combo in combinations_with_limited_replacement(all_decos+[None], deco_quantity+[sum(empty_slots)], sum(empty_slots)):
            # check if there's enough slots
            slots_taken = [0] * MAX_DECO_LVL
            for deco in deco_combo:
                if deco is not None:
                    slots_taken[deco.lvl-1] += 1
            if any(sum(slots_taken[i:]) > sum(empty_slots[i:]) for i in range(MAX_DECO_LVL)):
                continue

        # for deco_combo in get_deco_combinations_iterator(empty_slots, available_decos):
            armorset_with_deco = sum([armorset_no_deco] + list(deco_combo), None)

            # minimum skill requirement check 2
            if any(armorset_with_deco.get_skill_lvl(skill) < lvl for skill, lvl in must_have_skills_deco_avail.items()):
                continue

            if len(results) < top_n:
                heappush(results, armorset_with_deco)
            else:
                heappushpop(results, armorset_with_deco)

    
    results.sort(reverse=True)
    for armorset in results:
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

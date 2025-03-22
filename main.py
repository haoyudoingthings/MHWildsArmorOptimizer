# No need to vectorize the calculation (yet)
from MHWildsArmorOptimizer.classes import *
from MHWildsArmorOptimizer.data import *
from itertools import product
from heapq import heappush, heappushpop


def main():
    top_n = 5

    base_atk = 200
    base_aff = 0.15
    crit_bonus = 0.34 # CB3
    
    must_have_skills = {GArkveld: 4}

    results = []
    for helm, mail, braces, coil, greaves, charm in product(HELMS, MAILS, BRACES, COILS, GREAVES, CHARMS):
        armorset_no_deco = sum(helm, mail, braces, coil, greaves, charm)
        empty_slots = armorset_no_deco.get_empty_slots()
        # TODO: iterate over decoration combinations
        
        # minimum skill requirement check
        if any(skill not in tot_skills or tot_skills[skill] < lvl for skill, lvl in must_have_skills.items()):
            continue

        atk, aff = base_atk, base_aff
        for skill_name, skill_lvl in tot_skills.items():
            if skill_name not in SKILLS:
                continue
            skill = SKILLS[skill_name]
            atk += skill.atk(skill_lvl)
            aff += skill.aff(skill_lvl)
        eff_atk = atk * (1 + min(1, aff) * crit_bonus)
        if len(results) < top_n:
            heappush(results, (eff_atk, armorset)) # TODO: create Armorset class as the sum of Armor, create get_eff_atk func, and override __lt__ with the comparison of eff_atk
        else:
            heappushpop(results, (eff_atk, armorset))

    
    results.sort(key=lambda x: x[0], reverse=True)

    best_eff_atk, best_armorset = results[0]
    print("Best armorset:")
    print(' '.join([armor.name for armor in best_armorset]))
    print(f"Effective attack power: {best_eff_atk:.4f}")


if __name__ == '__main__':
    main()

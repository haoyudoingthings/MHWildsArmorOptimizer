# No need to vectorize the calculation (yet)
from MHWildsArmorOptimizer.classes import *
from MHWildsArmorOptimizer.data import *
from itertools import product
from heapq import heappush, heappushpop


# change this into skill method
def dict_sum(l_dict):
    out = {}
    for d in l_dict:
        for k, v in d.items():
            if k not in out:
                out[k] = v
            else:
                out[k] += v
    return out

def main():
    top_n = 5

    base_atk = 230 * 1.04 + 9 # AB5
    base_aff = 0
    crit_bonus = 0.25
    available_decos = {'Tenderizer': 1, 'Mighty': 2}
    all_decos = {k: v.lvl for k, v in DECORATIONS.items()}
    must_have_skills = {"G. Arkveld's Vitality": 4}

    results = []
    for helm, mail, braces, coil, greaves, charm in product(HELMS, MAILS, BRACES, COILS, GREAVES, CHARMS):
        armorset = [helm, mail, braces, coil, greaves, charm]

        # TODO: refactor this part into a function
        tot_slots = dict_sum([armor.slots for armor in armorset])
        # TODO: add addtional skills from decos
        tot_skills = dict_sum([armor.skills for armor in armorset])
        
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

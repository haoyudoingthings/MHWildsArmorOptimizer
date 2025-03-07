# No need to vectorize the calculation yet
# May need to import from itertools

class Skill:
    def __init__(self, atk_buffs: list = None, aff_buffs: list = None, name: str = 'unnamed'):
        # start from level 1 (do not include level 0 data)
        assert (atk_buffs is None) or (aff_buffs is None) or (len(atk_buffs) == len(aff_buffs))
        self.atk_buffs = atk_buffs if atk_buffs is not None else []
        self.aff_buffs = aff_buffs if aff_buffs is not None else []
        self.name = name

    def atk(self, lvl):
        if len(self.atk_buffs) == 0:
            return 0
        if lvl > len(self.atk_buffs):
            return self.atk_buffs[-1]
        return self.atk_buffs[lvl-1]
    
    def aff(self, lvl):
        if len(self.aff_buffs) == 0:
            return 0
        if lvl > len(self.aff_buffs):
            return self.aff_buffs[-1]
        return self.aff_buffs[lvl-1]

class Decoration:
    def __init__(self, skills: dict, lvl: int, name: str = 'Unnamed'):
        self.skills = skills
        self.lvl = lvl # width of the decoration
        self.name = name

class Armor:
    def __init__(self, skills: dict, slots: dict = None, name: str = 'Unnamed'):
        self.skills = skills
        self.slots = slots if slots is not None else {} # {lvl: num}
        self.name = name


SKILLS = {
    "Weakness Exploit": Skill(name="Weakness Exploit", aff_buffs=[0.05, 0.1, 0.15, 0.2, 0.3]), 
    "Agitator": Skill(name="Agitator", atk_buffs=[4, 8, 12, 16, 20], aff_buffs=[0.03, 0.05, 0.07, 0.1, 0.15]), 
    "Maximum Might": Skill(name="Maximum Might", aff_buffs=[0.1, 0.2, 0.3]), 
    "Burst": Skill(name="Burst", atk_buffs=[5]), 
    # "Counterstrike": Skill(name="Counterstrike"), 
    "Doshaguma's Might": Skill(name="Doshaguma's Might", atk_buffs=[0, 10, 10, 25]), 
}

DECORATIONS = {
    "Tenderizer": Decoration(name="Tenderizer", lvl=3, skills={"Weakness Exploit": 1}), 
    "Challenger": Decoration(name="Challenger", lvl=3, skills={"Agitator": 1}), 
    "Mighty": Decoration(name="Mighty", lvl=2, skills={"Maximum Might": 1}), 
    "Chain": Decoration(name="Chain", lvl=3, skills={"Burst": 1}), 
}

ARMOR_SETS = {
    "Doshaguma B": [
        None, #Armor(name="Doshaguma Helm B", slots={2: 1, 1: 2}, skills={"Doshaguma's Might": 1}), 
        Armor(name="Doshaguma Mail B", slots={1: 3}, skills={"Doshaguma's Might": 1}), 
        None, #Armor(name="Doshaguma Braces B", slots={2: 1, 1: 1}, skills={"Doshaguma's Might": 1}), 
        Armor(name="Doshaguma Coil B", slots={2: 2}, skills={"Doshaguma's Might": 1}), 
        Armor(name="Doshaguma Greaves B", slots={2: 1, 1: 2}, skills={"Doshaguma's Might": 1}), 
    ], 
    "G. Doshaguma B": [
        Armor(name="G. Doshaguma Helm B", slots={2: 2, 1: 1}, skills={"Doshaguma's Might": 1}), 
        Armor(name="G. Doshaguma Mail B", slots={2: 2}, skills={"Doshaguma's Might": 1}), 
        Armor(name="G. Doshaguma Braces B", slots={2: 2, 1: 1}, skills={"Doshaguma's Might": 1}), 
        None, #Armor(name="G. Doshaguma Coil B", slots={2: 1, 1: 1}, skills={"Doshaguma's Might": 1}), 
        None, #Armor(name="G. Doshaguma Greaves B", slots={2: 1, 1: 1}, skills={"Doshaguma's Might": 1}), 
    ], 
    # "Arkveld A": [
    #     Armor(name="Arkvulcan Helm A", slots={}, skills={"Arkveld's Hunger": 1}), 
    #     Armor(name="Arkvulcan Mail A", slots={2: 1}, skills={"Arkveld's Hunger": 1, "Weakness Exploit": 1}), 
    #     Armor(name="Arkvulcan Braces A", slots={2: 2}, skills={"Arkveld's Hunger": 1}), 
    #     Armor(name="Arkvulcan Coil A", slots={1: 1}, skills={"Arkveld's Hunger": 1, "Weakness Exploit": 2}), 
    #     Armor(name="Arkvulcan Greaves A", slots={2: 1, 1: 1}, skills={"Arkveld's Hunger": 1}), 
    # ], 
    "Arkveld B": [
        Armor(name="Arkvulcan Helm B", slots={3: 1, 2: 1, 1: 1}, skills={"Arkveld's Hunger": 1}), 
        Armor(name="Arkvulcan Mail B", slots={3: 1, 2: 1}, skills={"Arkveld's Hunger": 1, "Weakness Exploit": 1}), 
        Armor(name="Arkvulcan Braces B", slots={2: 2, 1: 1}, skills={"Arkveld's Hunger": 1}), 
        Armor(name="Arkvulcan Coil B", slots={1: 2}, skills={"Arkveld's Hunger": 1, "Weakness Exploit": 2}), 
        Armor(name="Arkvulcan Greaves B", slots={3: 1, 1: 1}, skills={"Arkveld's Hunger": 1}), 
    ], 
    "G. Arkveld B": [
        Armor(name="G. Arkveld Helm B", slots={3: 1, 1: 1}, skills={"G. Arkveld's Vitality": 1}), 
        Armor(name="G. Arkveld Mail B", slots={3: 1}, skills={"G. Arkveld's Vitality": 1}), 
        Armor(name="G. Arkveld Braces B", slots={1: 3}, skills={"G. Arkveld's Vitality": 1, "Weakness Exploit": 2}), 
        Armor(name="G. Arkveld Coil B", slots={2: 1, 1: 1}, skills={"G. Arkveld's Vitality": 1}), 
        Armor(name="G. Arkveld Greaves B", slots={2: 1, 1: 1}, skills={"G. Arkveld's Vitality": 1, "Weakness Exploit": 1}), 
    ], 
    # "G. Rathalos A": [
    #     Armor(name="G. Rathalos Helm A", slots={1: 2}, skills={"Weakness Exploit": 1}), 
    #     Armor(name="G. Rathalos Mail A", slots={1: 1}, skills={"Weakness Exploit": 1}), 
    #     Armor(name="G. Rathalos Braces A", slots={2: 1}, skills={"Weakness Exploit": 1}), 
    #     Armor(name="G. Rathalos Coil A", slots={1: 2}, skills={"Weakness Exploit": 1}), 
    #     Armor(name="G. Rathalos Greaves A", slots={1: 1}, skills={"Weakness Exploit": 1}), 
    # ], 
    "G. Rathalos B": [
        Armor(name="G. Rathalos Helm B", slots={2: 2}, skills={"Weakness Exploit": 1}), 
        None, #Armor(name="G. Rathalos Mail B", slots={2: 1}, skills={"Weakness Exploit": 1}), 
        Armor(name="G. Rathalos Braces B", slots={2: 1, 1: 2}, skills={"Weakness Exploit": 1}), 
        None, #Armor(name="G. Rathalos Coil B", slots={2: 2, 1: 1}), 
        None, #Armor(name="G. Rathalos Greaves B", slots={2: 1}, skills={"Weakness Exploit": 1}), 
    ], 
    "G. Fulgur A": [
        None, #Armor(name="G. Fulgur Helm A", skills={"Fulgur Anjanath's Will": 1, "Agitator": 2}), 
        None, #Armor(name="G. Fulgur Mail A", slots={2: 1}, skills={"Fulgur Anjanath's Will": 1, "Maximum Might": 1}), 
        Armor(name="G. Fulgur Braces A", slots={1: 1}, skills={"Fulgur Anjanath's Will": 1, "Agitator": 1, "Maximum Might": 1}), 
        Armor(name="G. Fulgur Coil A", slots={1: 2}, skills={"Fulgur Anjanath's Will": 1, "Maximum Might": 1}), 
        None, #Armor(name="G. Fulgur Greaves A", slots={1: 1}, skills={"Fulgur Anjanath's Will": 1}), 
    ], 
    "G. Fulgur B": [
        Armor(name="G. Fulgur Helm B", slots={2: 1}, skills={"Fulgur Anjanath's Will": 1, "Agitator": 2}), 
        Armor(name="G. Fulgur Mail B", slots={2: 1, 1: 2}, skills={"Fulgur Anjanath's Will": 1, "Maximum Might": 1}), 
        Armor(name="G. Fulgur Braces B", slots={2: 2}, skills={"Fulgur Anjanath's Will": 1, "Maximum Might": 1}), 
        Armor(name="G. Fulgur Coil B", slots={2: 2}, skills={"Fulgur Anjanath's Will": 1}), 
        Armor(name="G. Fulgur Greaves B", slots={2: 1, 1: 1}, skills={"Fulgur Anjanath's Will": 1}), 
    ], 
    "Dahaad A": [
        Armor(name="Dahaad Shardhelm A", slots={1: 1}, skills={"Jin Dahaad's Revolt": 1, "Agitator": 1, "Weakness Exploit": 1}), 
        None, #Armor(name="Dahaad Shardmail A", slots={3: 1, 1: 1}, skills={"Jin Dahaad's Revolt": 1}), 
        Armor(name="Dahaad Shardbraces A", skills={"Jin Dahaad's Revolt": 1, "Agitator": 2}), 
        None, #Armor(name="Dahaad Shardcoil A", slots={1: 2}, skills={"Jin Dahaad's Revolt": 1, "Weakness Exploit": 1}), 
        None, #Armor(name="Dahaad Shardgreaves A", slots={1: 1}, skills={"Jin Dahaad's Revolt": 1, "Agitator": 2}), 
    ], 
    "Dahaad B": [
        Armor(name="Dahaad Shardhelm B", slots={2: 2}, skills={"Jin Dahaad's Revolt": 1, "Agitator": 1}), 
        Armor(name="Dahaad Shardmail B", slots={3: 1, 2: 1}, skills={"Jin Dahaad's Revolt": 1}), 
        Armor(name="Dahaad Shardbraces B", slots={3: 1}, skills={"Jin Dahaad's Revolt": 1, "Agitator": 1}), 
        Armor(name="Dahaad Shardcoil B", slots={1: 3}, skills={"Jin Dahaad's Revolt": 1, "Weakness Exploit": 1}), 
        Armor(name="Dahaad Shardgreaves B", slots={2: 1}, skills={"Jin Dahaad's Revolt": 1, "Agitator": 2}), 
    ], 
}

HELMS = {l[0].name: l[0] for l in ARMOR_SETS.values() if l[0] is not None}
MAILS = {l[1].name: l[1] for l in ARMOR_SETS.values() if l[1] is not None}
BRACES = {l[2].name: l[2] for l in ARMOR_SETS.values() if l[2] is not None}
COILS = {l[3].name: l[3] for l in ARMOR_SETS.values() if l[3] is not None}
GREAVES = {l[4].name: l[4] for l in ARMOR_SETS.values() if l[4] is not None}
CHARMS = {
    "Challenger Charm II": Armor(name="Challenger Charm II", skills={"Agitator": 2}), 
    "Exploiter Charm II": Armor(name="Exploiter Charm II", skills={"Weakness Exploit": 2}), 
    "Mighty Charm II": Armor(name="Mighty Charm II", skills={"Maximum Might": 2}), 
    "Chain Charm II": Armor(name="Chain Charm II", skills={"Burst": 2}), 
    # "Counter Charm III": Armor(name="Counter Charm III", skills={"Counterstrike": 3}), 
}

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
    base_atk = 230 * 1.04 + 9 # AB5
    base_aff = 0
    crit_bonus = 0.25
    available_decos = {'Tenderizer': 1, 'Mighty': 2}
    all_decos = {k: v.lvl for k, v in DECORATIONS.items()}

    results = []
    for helm in HELMS.values():
        for mail in MAILS.values():
            for braces in BRACES.values():
                for coil in COILS.values():
                    for greaves in GREAVES.values():
                        for charm in CHARMS.values():
                            armorset = [helm, mail, braces, coil, greaves, charm]

                            tot_slots = dict_sum([armor.slots for armor in armorset])
                            # TODO: add addtional skills from decos
                            tot_skills = dict_sum([armor.skills for armor in armorset])
                            
                            atk, aff = base_atk, base_aff
                            for skill_name, skill_lvl in tot_skills.items():
                                if skill_name not in SKILLS:
                                    continue # TODO: add minimum skill requirement check
                                skill = SKILLS[skill_name]
                                atk += skill.atk(skill_lvl)
                                aff += skill.aff(skill_lvl)
                            eff_atk = atk * (1 + min(1, aff) * crit_bonus)
                            results.append((eff_atk, armorset))
    results.sort(key=lambda x: x[0], reverse=True)

    best_eff_atk, best_armorset = results[0]
    print("Best armor set:")
    print(' '.join([armor.name for armor in best_armorset]))
    print("Effective attack power:", best_eff_atk)


if __name__ == '__main__':
    main()

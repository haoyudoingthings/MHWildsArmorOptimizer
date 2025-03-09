from MHWildsArmorOptimizer.classes import *

# TODO: move the set of all skills to class attribute of SKILL
SKILLS = {
    "Weakness Exploit": Skill(name="Weakness Exploit", aff_buffs=[0.05, 0.1, 0.15, 0.2, 0.3]), 
    "Agitator": Skill(name="Agitator", atk_buffs=[4, 8, 12, 16, 20], aff_buffs=[0.03, 0.05, 0.07, 0.1, 0.15]), 
    "Maximum Might": Skill(name="Maximum Might", aff_buffs=[0.1, 0.2, 0.3]), 
    "Burst": Skill(name="Burst", atk_buffs=[5]), 
    # "Counterstrike": Skill(name="Counterstrike"), 
    "Doshaguma's Might": Skill(name="Doshaguma's Might", atk_buffs=[0, 10, 10, 25]), 
    "Ebony Odogaron's Power": Skill(name="Ebony Odogaron's Power", atk_buffs=[0, 3, 3, 10])
}

DECORATIONS = {
    "Tenderizer": Decoration(name="Tenderizer", lvl=3, skills={"Weakness Exploit": 1}), 
    "Challenger": Decoration(name="Challenger", lvl=3, skills={"Agitator": 1}), 
    "Mighty": Decoration(name="Mighty", lvl=2, skills={"Maximum Might": 1}), 
    "Chain": Decoration(name="Chain", lvl=3, skills={"Burst": 1}), 
}

ARMORSETS = {
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
    "G. Ebony A": [
        None, #Armor(name="G. Ebony Helm A", skills={"Ebony Odogaron's Power": 1, "Burst": 2}), 
        None, #Armor(name="G. Ebony Mail A", slots={2: 1}, skills={"Ebony Odogaron's Power": 1}), 
        Armor(name="G. Ebony Braces A", skills={"Ebony Odogaron's Power": 1, "Burst": 2}), 
        None, #Armor(name="G. Ebony Coil A", slots={2: 1}, skills={"Ebony Odogaron's Power": 1, "Burst": 1}), 
        None, #Armor(name="G. Ebony Greaves A", slots={2: 1}, skills={"Ebony Odogaron's Power": 1}), 
    ], 
    "G. Ebony B": [
        Armor(name="G. Ebony Helm B", slots={2: 1}, skills={"Ebony Odogaron's Power": 1, "Burst": 2}), 
        Armor(name="G. Ebony Mail B", slots={2: 2}, skills={"Ebony Odogaron's Power": 1}), 
        Armor(name="G. Ebony Braces B", slots={2: 1, 1: 1}, skills={"Ebony Odogaron's Power": 1, "Burst": 1}), 
        Armor(name="G. Ebony Coil B", slots={2: 1, 1: 1}, skills={"Ebony Odogaron's Power": 1, "Burst": 1}), 
        Armor(name="G. Ebony Greaves B", slots={2: 1, 1: 1}, skills={"Ebony Odogaron's Power": 1}), 
    ], 
}

HELMS = [l[0] for l in ARMORSETS.values() if l[0] is not None]
MAILS = [l[1] for l in ARMORSETS.values() if l[1] is not None]
BRACES = [l[2] for l in ARMORSETS.values() if l[2] is not None]
COILS = [l[3] for l in ARMORSETS.values() if l[3] is not None]
GREAVES = [l[4] for l in ARMORSETS.values() if l[4] is not None]
CHARMS = {
    "Challenger Charm II": Armor(name="Challenger Charm II", skills={"Agitator": 2}), 
    "Exploiter Charm II": Armor(name="Exploiter Charm II", skills={"Weakness Exploit": 2}), 
    "Mighty Charm II": Armor(name="Mighty Charm II", skills={"Maximum Might": 2}), 
    "Chain Charm II": Armor(name="Chain Charm II", skills={"Burst": 2}), 
    # "Counter Charm III": Armor(name="Counter Charm III", skills={"Counterstrike": 3}), 
}

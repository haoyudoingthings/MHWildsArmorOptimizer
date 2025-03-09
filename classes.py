class Skill:
    all = {}

    def __init__(self, atk_buffs: list = None, aff_buffs: list = None, name: str = 'Unnamed', uptime: float = 1):
        # start from level 1 (do not include level 0 data)
        assert (atk_buffs is None) or (aff_buffs is None) or (len(atk_buffs) == len(aff_buffs))
        self.atk_buffs = atk_buffs if atk_buffs is not None else []
        self.aff_buffs = aff_buffs if aff_buffs is not None else []
        self.name = name
        Skill.all[name] = self

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
    all = {}

    def __init__(self, skills: dict, lvl: int, name: str = 'Unnamed'):
        self.skills = skills
        self.lvl = lvl # width of the decoration
        self.name = name
        Decoration.all[name] = self

class Armor:
    all = {}

    def __init__(self, skills: dict, slots: dict = None, name: str = 'Unnamed'):
        self.skills = skills
        self.slots = slots if slots is not None else {} # {lvl: num}
        self.name = name
        Armor.all[name] = self

# class Armorset:
#     def __init__(self, helm: Armor = None, mail: Armor = None, braces: Armor = None, coil: Armor = None, greaves: Armor = None, charm: Armor = None, decos: Decoration = None):
#         self.helm = helm
#         self.mail = mail
#         self.braces = braces
#         self.coil = coil
#         self.greaves = greaves
#         self.charm = charm
#         self.decos = decos

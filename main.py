# No need to vectorize the calculation yet
# May need to import from itertools

class Skill:
    def __init__(self, atk_buffs: list = None, aff_buffs: list = None):
        # start from level 1 (do not include level 0 data)
        assert (atk_buffs is None) or (aff_buffs is None) or (len(atk_buffs) == len(aff_buffs))
        self.atk_buffs = atk_buffs if atk_buffs is not None else []
        self.aff_buffs = aff_buffs if aff_buffs is not None else []

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
    def __init__(self, skills: dict, lvl: int):
        self.skills = skills
        self.lvl = lvl # width of the decoration

class Armor:
    def __init__(self, skills: dict, decos: dict = None):
        self.skills = skills
        self.decos = decos if decos is not None else {}


def main():
    base_atk = 230 * 1.04 + 9 # AB5
    base_aff = 0
    crit_bonus = 0.25


if __name__ == '__main__':
    main()

# TODO: add ways for skills to interact with each other (e.g. Fulgar Anjanath's Power and Maximum Might)
# TODO: add ways to accommodate skills that have different effects during different circumstances (e.g. Gore Magala's Tyranny)
from itertools import chain

class Skill:
    all = {}

    def __init__(self, atk_buffs: list = None, aff_buffs: list = None, name: str = 'Unnamed', uptime: float = 1):
        # start from level 1 (do not include level 0 data)
        assert (atk_buffs is None) or (aff_buffs is None) or (len(atk_buffs) == len(aff_buffs))
        self.atk_buffs = atk_buffs if atk_buffs is not None else []
        self.aff_buffs = aff_buffs if aff_buffs is not None else []
        self.name = name
        Skill.all[name] = self

    def tot_lvls(self):
        return max(len(self.atk_buffs), len(self.aff_buffs))

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

    def __init__(self, skills: dict, lvl: int, name: str = 'Unnamed', tot_amount: int = None):
        self.skills = skills
        self.lvl = lvl # width of the decoration
        self.name = name
        self.tot_amount = tot_amount if tot_amount is not None else max(skill.tot_lvls() for skill in skills.keys())
        Decoration.all[name] = self

class Armor:
    all = {}

    def __init__(self, skills: dict, part: str, slots: list = None, name: str = 'Unnamed'):
        assert part in ['helm', 'mail', 'braces', 'coil', 'greaves', 'charm'], "Unsupported name for part"
        self.skills = skills
        self.slots = slots if slots is not None else [0, 0, 0] # slots[lvl] = num of slots of that level open
        self.name = name
        self.part = part
        Armor.all[name] = self
    
    def __add__(self, other):
        if isinstance(other, Armor):
            assert self.part != other.part, "Cannot add two armors of the same part together"
            return Armorset(parts={self.part: self, other.part: other})
        elif isinstance(other, Decoration):
            assert sum(self.slots[other.lvl-1:]) >= 1, "Not enough open slots for decoration"
            return Armorset(parts={self.part: self}, decos=[other])
        else:
            return NotImplemented

class Armorset:
    def __init__(self, parts: dict = None, decos: list = None):
        assert parts is None or all(k in ['helm', 'mail', 'braces', 'coil', 'greaves', 'charm'] for k in parts.keys()), "Unsupported keys for parts"
        self.parts = parts if parts is not None else {}
        self.decos = decos if decos is not None else []
    
    def __add__(self, other):
        if isinstance(other, Armor):
            assert other.part not in self.parts, "Overlapping armor parts"
            return Armorset(parts=self.parts | {other.part: other}, decos=self.decos)
        elif isinstance(other, Decoration):
            assert sum(self.get_empty_slots()[other.lvl-1:]) >= 1, "Not enough slots for the decoration"
            return Armorset(parts=self.parts, decos=self.decos + [other])
        elif isinstance(other, Armorset):
            assert self.parts.keys().isdisjoint(other.parts.keys()), "Overlapping armor parts"
            return Armorset(parts=self.parts | other.parts, decos=self.decos + other.decos)
        else:
            return NotImplemented
    
    def __lt__(self, other):
        assert isinstance(other, Armorset), "Can only compare between two armor sets"
        return self.get_eff_atk() < other.get_eff_atk() # TODO: somehow isolate base atk, aff and crit bonus

    def get_empty_slots(self):
        empty_slots = [0, 0, 0]
        for armor in self.parts.values():
            for i in range(3):
                empty_slots[i] += armor.slots[i]
        for d in self.decos:
            if empty_slots[d.lvl-1] > 1:
                empty_slots[d.lvl-1] -= 1
            elif d.lvl < 3 and empty_slots[d.lvl] > 1:
                empty_slots[d.lvl] -= 1
            elif d.lvl < 2 and empty_slots[d.lvl+1] > 1:
                empty_slots[d.lvl+1] -= 1
        return empty_slots
    
    def get_skill_lvl(self, skill):
        lvl = 0
        for part in chain(self.parts.values(), self.decos):
            if skill in part.skills: # TODO: confirm whether to use Skill or str as keys for skills dictionary
                lvl += parts.skills[skill]
        return lvl
    
    def get_all_skill_lvls(self):
        all_skills = {}
        for part in chain(self.parts.values(), self.decos):
            for k, v in part.skills.items():
                if k in all_skills:
                    all_skills[k] = v
                else:
                    all_skills[k] += v
        return all_skills

    def get_eff_atk(self, base_atk, base_aff, crit_bonus):
        atk, aff = base_atk, base_aff

        all_skills = self.get_all_skill_lvls()
        for skill, lvl in all_skills.items():
            # TODO: properly take uptime into account
            atk += skill.atk(lvl) * skill.uptime
            aff += skill.aff(lvl) * skill.uptime
        
        return atk * (1 + min(1, aff) * (crit_bonus if aff >= 0 else -0.25))

# TODO: add ways to accommodate skills that have different effects during different circumstances (e.g. Gore Magala's Tyranny)
from itertools import chain


MAX_DECO_LVL = 3
ARMOR_PART_NAMES = ['helm', 'mail', 'braces', 'coil', 'greaves', 'charm']

class Skill:
    all = {}

    def __init__(
            self, atk_buffs: list[float] | None = None, aff_buffs: list[float] | None = None, 
            name: str = 'Unnamed', uptime: list[float] | float = 1, replace: list | None = None, 
            uptime_buffs_lst_lst: list[list[tuple[float, float, float]]] | None = None, pass_calc: bool = False, 
        ):
        # start from level 1 (do not include level 0 data)
        assert atk_buffs is None or aff_buffs is None or len(atk_buffs) == len(aff_buffs)
        assert (atk_buffs is None and aff_buffs is None) or uptime_buffs_lst_lst is None
        assert uptime_buffs_lst_lst is None or all(sum(p for p, _, _ in l) == 1 for l in uptime_buffs_lst_lst), "Sum of uptimes must be 1"
        self.atk_buffs = atk_buffs if atk_buffs is not None else []
        self.aff_buffs = aff_buffs if aff_buffs is not None else []
        self.uptime_lst = [uptime] if isinstance(uptime, (int, float)) else uptime
        self.name = name
        self.replace = replace
        self.uptime_buffs_lst_lst = uptime_buffs_lst_lst
        self.pass_calc = pass_calc
        Skill.all[name] = self

    def __str__(self):
        return self.name

    def tot_lvls(self) -> int:
        if self.uptime_buffs_lst_lst is None:
            return max(len(self.atk_buffs), len(self.aff_buffs))
        else:
            return len(self.uptime_buffs_lst_lst)

    def atk(self, lvl) -> float:
        if self.uptime_buffs_lst_lst is not None:
            return NotImplemented
        if len(self.atk_buffs) == 0:
            return 0
        if lvl > len(self.atk_buffs):
            return self.atk_buffs[-1]
        return self.atk_buffs[lvl-1]
    
    def aff(self, lvl) -> float:
        if self.uptime_buffs_lst_lst is not None:
            return NotImplemented
        if len(self.aff_buffs) == 0:
            return 0
        if lvl > len(self.aff_buffs):
            return self.aff_buffs[-1]
        return self.aff_buffs[lvl-1]

    def uptime(self, lvl) -> float:
        if lvl > len(self.uptime_lst):
            return self.uptime_lst[-1]
        return self.uptime_lst[lvl-1]
    
    def get_uptime_buffs_lst(self, lvl) -> list[tuple[float, float, float]]:
        if self.uptime_buffs_lst_lst is not None:
            if lvl > len(self.uptime_buffs_lst_lst):
                return self.uptime_buffs_lst_lst[-1]
            return self.uptime_buffs_lst_lst[lvl-1]
        if self.uptime(lvl) == 1:
            return [(1, self.atk(lvl), self.aff(lvl))]
        return [(self.uptime(lvl), self.atk(lvl), self.aff(lvl)), (1 - self.uptime(lvl), 0, 0)]
    
    def replace_skill(self, lvl):
        if self.replace is None:
            return None
        if lvl > len(self.replace):
            return self.replace[-1]
        return self.replace[lvl-1]

class Decoration:
    all = {}

    def __init__(self, skills: dict[Skill, int], lvl: int, name: str = 'Unnamed', tot_amount: int | None = None):
        self.skills = skills
        self.lvl = lvl # width of the decoration
        self.name = name
        self.tot_amount = tot_amount if tot_amount is not None else max(skill.tot_lvls() for skill in skills.keys())
        Decoration.all[name] = self

    def __str__(self):
        return self.name

class Weapon:
    def __init__(self, atk: int, aff: float, crit_bonus: float, name: str | None = None):
        self.atk = atk
        self.aff = aff
        self.crit_bonus = crit_bonus
        self.name = name

    def __str__(self):
        if self.name is not None:
            return self.name
        else:
            return f"Weapon({self.atk}, {self.aff}, {self.crit_bonus})"
    
    def __add__(self, other):
        if other is None:
            return self
        else:
            return NotImplemented
        
    def __radd__(self, other):
        return self + other

class Armor:
    all = {}

    def __init__(self, skills: dict[Skill, int], part: str, slots: list[int] | None = None, name: str = 'Unnamed'):
        assert part in ARMOR_PART_NAMES, "Unsupported name for part"
        self.skills = skills
        self.slots = slots if slots is not None else [0] * MAX_DECO_LVL # slots[lvl] = num of slots of that level open
        self.name = name
        self.part = part
        Armor.all[name] = self

    def __str__(self):
        return self.name

    def __add__(self, other):
        if other is None:
            return self
        elif isinstance(other, Armor):
            assert self.part != other.part, "Cannot add two armors of the same part together"
            return Armorset(parts={self.part: self, other.part: other})
        elif isinstance(other, Decoration):
            assert sum(self.slots[other.lvl-1:]) >= 1, "Not enough open slots for decoration"
            return Armorset(parts={self.part: self}, decos=[other])
        elif isinstance(other, Weapon):
            return Armorset(parts={self.part: self}, weapon=other)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
    
    @classmethod
    def get_all_armors_by_part(cls, part: str):
        return {k: v for k, v in cls.all.items() if v.part == part}

class Armorset:
    def __init__(self, parts: dict[str, Armor] | None = None, decos: list[Decoration] | None = None, weapon: Weapon | None = None):
        assert parts is None or all(k in ARMOR_PART_NAMES for k in parts.keys()), "Unsupported keys for parts"
        self.parts = parts if parts is not None else {}
        self.decos = decos if decos is not None else []
        self.weapon = weapon
        self.eff_atk = None
    
    def __add__(self, other):
        if other is None:
            return self
        elif isinstance(other, Armor):
            assert other.part not in self.parts, "Overlapping armor parts"
            return Armorset(parts=self.parts | {other.part: other}, decos=self.decos, weapon=self.weapon)
        elif isinstance(other, Decoration):
            assert sum(self.get_empty_slots()[other.lvl-1:]) >= 1, "Not enough slots for the decoration"
            return Armorset(parts=self.parts, decos=self.decos + [other], weapon=self.weapon)
        elif isinstance(other, Weapon):
            assert self.weapon is None, "Armorset already contains a weapon"
            return Armorset(parts=self.parts, decos=self.decos, weapon=other)
        elif isinstance(other, Armorset):
            assert self.parts.keys().isdisjoint(other.parts.keys()), "Overlapping armor parts"
            assert self.weapon is None or other.weapon is None, "Overlapping weapons"
            return Armorset(parts=self.parts | other.parts, decos=self.decos + other.decos, weapon=self.weapon if self.weapon is not None else other.weapon)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        return self + other
    
    def __lt__(self, other):
        assert isinstance(other, Armorset), "Can only compare between two armor sets"
        return self.get_eff_atk() < other.get_eff_atk()

    def get_empty_slots(self) -> list[int]:
        empty_slots = [0] * MAX_DECO_LVL
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
    
    def get_skill_lvl(self, skill) -> int:
        lvl = 0
        for part in chain(self.parts.values(), self.decos):
            if skill in part.skills:
                lvl += part.skills[skill]
        return lvl
    
    def get_all_skill_lvls(self) -> dict[Skill, int]:
        all_skills = {}
        for part in chain(self.parts.values(), self.decos):
            for k, v in part.skills.items():
                if k in all_skills:
                    all_skills[k] += v
                else:
                    all_skills[k] = v
        return all_skills

    def get_eff_atk(self) -> float:
        if self.eff_atk is None:
            atk0, aff0, crit_bonus = self.weapon.atk, self.weapon.aff, self.weapon.crit_bonus
            all_skills = self.get_all_skill_lvls()

            skill_replacement = [skill.replace_skill(lvl) for skill, lvl in all_skills.items() if skill.replace_skill(lvl) is not None]
            for skill, skill2 in skill_replacement:
                if skill in all_skills:
                    all_skills[skill2] = all_skills[skill]
                    del all_skills[skill]
            
            uptime_atk_aff_bonus_lst = [(1, 0, 0)]
            for skill, lvl in all_skills.items():
                if skill.pass_calc:
                    continue
                new_lst = []
                for p, atk, aff in skill.get_uptime_buffs_lst(lvl):
                    new_lst.extend([(p0 * p, atk0 + atk, aff0 + aff) for p0, atk0, aff0 in uptime_atk_aff_bonus_lst])
                uptime_atk_aff_bonus_lst = new_lst
                # uptime_atk_aff_lst = [(p * skill.uptime(lvl), atk + skill.atk(lvl), min(1, aff + skill.aff(lvl))) for p, atk, aff in uptime_atk_aff_lst] + \
                #                      [(p * (1 - skill.uptime(lvl)), atk, aff) for p, atk, aff in uptime_atk_aff_lst]
            
            self.eff_atk = sum(p * (atk0 + atk) * (1 + min(1, aff0 + aff) * (crit_bonus if aff0 + aff >= 0 else -0.25)) for p, atk, aff in uptime_atk_aff_bonus_lst)
        
        return self.eff_atk

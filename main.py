import random

from dataclasses import dataclass


@dataclass
class Thing:
    name_thing: str
    perc_prot: int
    attack: int
    life: int


class Person:
    def __init__(self, name_person, count_hp, base_attack,
                 base_perc_prot):
        self.name_person = name_person
        self.count_hp = count_hp
        self.base_attack = base_attack
        self.base_perc_prot = base_perc_prot

    def set_thing(self):
        pass


class Paladin(Person):
    def __init__(self, name_person, count_hp, base_attack,
                 base_perc_prot):
        super().__init__(name_person, count_hp, base_attack,
                         base_perc_prot)
        self.count_hp = count_hp * 2
        self.base_perc_prot = base_perc_prot * 2


class Warrior(Person):
    def __init__(self, name_person, count_hp, base_attack,
                 base_perc_prot):
        super().__init__(name_person, count_hp, base_attack,
                         base_perc_prot)
        self.base_attack = base_attack * 2


if __name__ == '__main__':
    pass

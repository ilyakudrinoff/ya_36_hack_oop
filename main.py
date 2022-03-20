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

    def set_thing(self, things):
        things_pers = []
        random_index = random.randint(0, len(things) - 1)
        for i in range(0, random.randint(1, 4)):
            things_pers.append(things[random_index])
            return things_pers

    def attack_damage(self):
        pass

    def minus_life(self):
        return (HitPoints - (attack_damage - attack_damage
                             * finalProtection))


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


def create_thing():
    name = {'щит': [0.05, 0.08, 0.02], 'меч': [0.04, 0.08, 0.03],
            'броня': [0.08, 0.01, 0.01], 'кольчуга': [0.06, 0.01, 0.02],
            'дубинка': [0.03, 0.06, 0.02], 'сапоги': [0.01, 0.01, 0.01]
            }
    random_index = random.randint(0, len([name.keys()]) - 1)
    return Thing(name[random_index], *name[random_index])


def create_person() -> Person:
    name_persons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o',
                    'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z']
    persons = {'WR': Warrior, 'PL': Paladin}
    index_person = random.randint(0, len([persons.keys()]) - 1)
    random_index = random.randint(0, len(name_persons) - 1)
    return persons[index_person](name_persons[random_index],
                                 random.randint(0, 10), 2, 2)


def main():
    my_things = []
    for thing in range(1, random.randint(2, 10)):
        my_things.append(create_thing())
    for i in range(1, 10):
        create_person().set_thing(my_things)

    print(f'{person_attack} наносит удар по '
          f'{person_protect} на {count_hp} урона.')


if __name__ == '__main__':
    main()

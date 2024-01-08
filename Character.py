class Character:
    def __init__(self, strength, dexterity, wit, melee, weapon_bonus) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.wit = wit
        self.melee = melee
        self.weapon_bonus = weapon_bonus
        self.wounds = 0

    def take_damage(self, damage_value) -> None:
        self.wounds += damage_value

    def can_fight(self) -> bool:
        return self.wounds <= 6
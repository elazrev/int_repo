class Human:
    def __init__(self, health):
        self.health = health

    def attack(self):
        print("Attacking!")


class Warrior(Human):

    def __init__(self, health, defence=0, weapon_rate=1):
        super().__init__(health)
        self.defence = defence
        self.current_weapon_rate = weapon_rate

    def __str__(self):
        return f"This warrior has {self.health} points of health \nand {self.current_weapon_rate} of weapon harm rate!"

    def get_armor(self, armor=1):
        self.defence += armor

    def improve_weapon(self, weapon):
        self.current_weapon_rate += weapon

    def attacked(self, damage: float):
        self.defence -= damage
        if self.defence < 0:
            self.health += self.defence
            self.defence = 0


class Barbarian(Human):

    def __init__(self, health, damage_rate=1):
        super().__init__(health)
        self.damage_rate = damage_rate

    def __str__(self):
        return f"this is a barbarian person, He have {self.health} points of health"


class Monster:
    def __init__(self, health=100, damage_rate=1):
        self.health = health
        self.damage = damage_rate

    def __str__(self):
        if self.health > 0:
            return f"This monster have {self.health} point of health \nand {self.damage} points of damage potential"
        else:
            return "Dead monster on the road!"

    def attacked(self, harm_points):
        self.health -= harm_points
        if self.health > 0:
            print(f"Monster attacked! current health rate is {self.health}")
        else:
            print("The monster is dead!!!")
            return False


soldier = Warrior(100)
barbar = Barbarian(60)
lochi = Monster()

print(soldier)
print(barbar)
print(lochi)

for i in range(5):
    lochi.attacked(soldier.current_weapon_rate)


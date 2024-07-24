from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


dice6 = Die(6)
dice10 = Die(10)
dice20 = Die(20)

# rolls for 6 sided dice
for roll in range(1, 11):
    print(dice6.roll_die())
print("----------------")
# rolls for 10 sided dice
for roll in range(1, 11):
    print(dice10.roll_die())
print("----------------")
# rolls for 20 sided dice
for roll in range(1, 11):
    print(dice20.roll_die())
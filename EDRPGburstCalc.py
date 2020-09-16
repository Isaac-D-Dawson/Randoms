import random as rand

#Lets go the whole hog

class Dice:     #Generic dice object used for handling rolls. because.
    def __init__(self, sides: int = 6, *name):
        self.sides = sides
        if not name:
            name = f"D{sides}"
        self.name = name
        self.showing = 1    #All dice show 1 when created
    
    @property
    def roll(self):
        self.showing = rand.randint(1, self.sides)
        return self.showing

def calc_burst(targ: int, flat: int, burst: int) -> None:
    d10 = Dice(10)
    roll = d10.roll
    if roll < targ:
        print("you missed")
    elif roll == targ:
        print(f"You hit, Dealing {d10.roll} damage!")
    elif  roll > targ:
        print(f"You hit, Dealing {d10.roll} damage and {d10.roll} Burst damage!")

calc_burst(4, 1, 3)

# Notes:
# -Shift roll mechanic to before checks rather than walrusing it.
# -use the players weapon stats
# -Find some way to compensate for both Diced and Non-Diced burst weapons
# -Make it so flat and burst actually have relevancy to damage dealt
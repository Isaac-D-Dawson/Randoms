import random as rand

language = ["and", "Or", "But", "not"]

def string_karkatenate(*args: str) -> str:
    outval = ""
    for i in args:
        if rand.randint(0, 1) == 1:
            outval += f"{rand.choice(language)} {i} "
        else:
            outval += f"{i.strip()} "
    return outval.upper().strip()

print(string_karkatenate("Test1", "Option2", "Third example"))
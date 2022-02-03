#Contains a function that arbitrarily generates a string containing;
#-An opening Char.
#-A filler Char repeated between a and b times.
#=By default a=4 and b=20, however this should be adjustable
#-An ending Char.

def arbitraryBookend(start:str = ">", fill:str = "/", end:str = "<", limiter:list = [int(4), int(20)]) -> str:
    '''
    Returns a random length repeating string inside two "Bookend" strings; Start and End.
    Start, Stop, and fill can all be adjusted to suit user needs, but default is ">////<"

    Note that the limiter values are both inclusive- default is 4-20
    '''
    
    import random as rand 

    limiter.sort() #just in case some nutcase tries to pass in the values backwards
    #Not that it'd break anything, but just in case.

    outval = start
    
    for i in range(limiter[0], rand.randint(limiter[0], limiter[-1])+1):
        outval += fill
        #Add one to the limiter- even though randint is randrange+1,
        # This ensures more reliability with user expectation;
        # That the stop value is *inclusive*
    
    outval += end

    return outval

print(arbitraryBookend())
#This can't be easily tested by assertions.
#I could hack together some sort of load-state output into the function but..Why?
#Instead, we'll trust human error to judge. Good luck, End User.

print("Testing to confirm that the ducktyped keys can be overriden.")
print(arbitraryBookend(start="This ", fill="i", end="s one heck of a test.", limiter=[1, 7]))

print("Testing to confirm that the ranges can be overriden in such a way as to force a single output.")
print(arbitraryBookend(start="This ", fill="is ", end="a Boring test.", limiter=[1, 1]))
print("a much more ham-fisted approach to that, that also confirms you can't bust it by giving it only one input.")
print(arbitraryBookend(limiter=[1]))

print("Testing to confirm that parsing the limiter inputs out-of-order won't cause issues.")
#It shouldn't, I prepared for this, but still.
print(arbitraryBookend(limiter=[10, 7]))

print("And finally checks for \"Too many inputs!\"")
print(arbitraryBookend(limiter=[1,5,2,7,10]))
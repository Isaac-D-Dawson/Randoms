#This will require the existing "isPrime.py".
#This function returns the prime factors of the current hour and minuite.

#Ideal end goal is a game that compares a users input to the time in the same way as https://xkcd.com/247/

#firstly, import prerequisites, and inform endu-user of importing
print("Importing required packages")
print("Importing Datetime")
import datetime as dt
print("importing isPrime")
import isPrime as iP
print("Importing Done")

for i in range(1, 1001):
    iP.isPrime(i)

primeRecord = {}
for i in range(0, len(iP.primeRecord.keys())):
    if iP.primeRecord[i] == True:
        primeRecord[i] = iP.primeRecord[i]

knownFactorised = {2:[2], 3:[3], 4:[2, 2]}

def primeFactors(num:int) -> list():
    #Memoiseation
    if num in knownFactorised:
        return knownFactorised[num]
    
    outval = []
    original_num = num

    i = 1
    primes = [i for i in primeRecord.keys()]
    while isinstance(i, int):
        if i <= len(primeRecord):
            if num % primes[i] == 0:
                outval.append(primes[i])
                num = num/primes[i]
                i = 1
        else:
            i = None

    print(outval)

primeFactors(20)

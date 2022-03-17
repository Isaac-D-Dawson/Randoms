#Script file for isPrime function.

#Logic as thus;
#Get Number
#Check if in prime record
#If yes, return True
#Else, refer to prime record keys.



primeRecord = {0 : False, 1 : False, 2 : True, 3 : True}

def isPrime(num:int) -> bool:
    '''
    Returns "True" if the provided integer is prime,
    Returns "False" if it is not.
    Only accepts Positive Ints.
    '''
    if num <= 0: #Confirm input is positive
        raise ValueError("Negative number cannot be resolved as prime.")
    
    if num in primeRecord.keys():#Check if number is known
        return primeRecord[num]
    else:
        #Check all prime values below the square root of the target
        test_primes = [i for i in range(1, int(num**0.5)+1 ) if isPrime(i) == True]
        for j in test_primes:
            if num % j == 0:
                primeRecord[num] = True
                return False
    primeRecord[num] = True
    return True

assert isPrime(1)   ==  False, "One is not Prime"
assert isPrime(2)   ==  True,  "Two Is Prime"
assert isPrime(100) ==  False, "100 is not prime"
assert isPrime(17)  ==  True,  "17 is Prime"
assert isPrime(5)   ==  True, "Should have been established during 100"
assert isPrime(-1) #Lets see what happens.
from math import factorial #import only the factorial function

def permutations(numObjects, numObjectsTaken):
    
    numPermutations = factorial(numObjects)/factorial(numObjects - numObjectsTaken)
    
    return numPermutations



print("Selecting 4 digits between 0-9 using one digit only once has %d permutations." % permutations(10, 4))
    

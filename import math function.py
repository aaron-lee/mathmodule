import math

def permutations(numObjects, numObjectsTaken):
    
    numPermutations = math.factorial(numObjects)/math.factorial(numObjects - numObjectsTaken)
    
    return numPermutations


print("Selecting 4 digits between 0-9 using one digit only once has %d permutations." % permutations(10, 4))
    
    
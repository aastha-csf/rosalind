import os
from rosalindUtilities import getInputFromFile, setOutputToFile

def rabbitsAndRecurrenceRelations(filename):
    line = getInputFromFile(filename).split()
    n = int(line[0])
    k = int(line[1])
    pairs = pairsOfRabbits(n, k)
    setOutputToFile(str(pairs))
    return pairs

memo = {}
def pairsOfRabbits(n, k):
    args = (n, k)
    if args in memo:
        return memo[args]

    if n == 0 or n == 1: return n
    elif n == 2: return 1
    else:
        temp = k+1
        pairs = (pairsOfRabbits(n-3, k) * k + pairsOfRabbits(n-2, k) * (temp))

    memo[args] = pairs 

    return pairs

print(rabbitsAndRecurrenceRelations("data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"))
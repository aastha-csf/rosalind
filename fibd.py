import os
from rosalindUtilities import getInputFromFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def mortalFibRabbits(n, m):
    """
    This function takes in 2 parameters, n and m, 
    and returns the total number of rabbit pairs after n months if they die after m months.

    :param int n: The number of months to calculate the rabbit population
    :param int m: The number of months rabbits live
    :return: The total number of rabbit pairs after n months
    :rtype: int
    """
    rabbits = [0, 0]
    newborn = [0, 1]
    for i in range(2, n+1):
        newborn.append(rabbits[i-1])
        rabbits.append(rabbits[i-1] + newborn[i-1])
        
        if i > m:
            rabbits[i] -= newborn[i-m]
    return rabbits[-1] + newborn[-1]

def main():
    n, m, *_ = getInputFromFile(filename).split()
    setOutputToFile(str(mortalFibRabbits(int(n), int(m))))

if __name__ == "__main__":
    main()
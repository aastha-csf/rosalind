import os
from rosalindUtilities import getInputFromFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def hammingDistance(s, t):
    """
    This function takes two strings, s and t, as input and returns the hamming distance between the two strings.
    
    The hamming distance is the number of positions at which the corresponding symbols are different.
    """
    hammingDistance = 0
    for (base1, base2) in zip(s, t):
        if(base1 != base2):
            hammingDistance = hammingDistance +1

    return hammingDistance

def main():
    s, t = getInputFromFile(filename).split("\n")[:-1]
    setOutputToFile(str(hammingDistance(s, t)))

if __name__ == "__main__":
    main()
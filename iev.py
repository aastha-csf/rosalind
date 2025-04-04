import os 
from rosalindUtilities import getInputFromFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def expectedOffspringWithDominantPhenotype(parents):
    """
    This function takes in a list of integers representing the number of parents 
    in each of the six possible genotypes (AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa) 
    and returns the expected number of offspring that will display the dominant phenotype.

    :param list parents: A list of six integers representing the number of 
        parents in each of the six possible genotypes.
    :return: The expected number of offspring that will display the dominant 
        phenotype.
    :rtype: int
    """
    expected = 0
    probablilities = [1, 1, 1, 0.75, 0.50, 0]
    for i, parent in enumerate(parents): 
        expected += (parent*2)*probablilities[i]

    return expected

def main():
    parents = [int(num) for num in getInputFromFile(filename).split()]
    setOutputToFile(str(expectedOffspringWithDominantPhenotype(parents)))

if __name__ == "__main__":
    main()

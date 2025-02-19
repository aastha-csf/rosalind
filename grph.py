import os
from rosalindUtilities import getInputFromFASTAFileWithID, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def overlapStrings(fastaFormat, k):
    """
    Finds all overlapping strings in a given FASTA formatted file.

    :param dict fastaFormat: A dictionary where the keys are the IDs and the values are the corresponding DNA strings
    :param int k: The number of characters to consider for overlap
    :return: A list of strings where each string is of the form "ID1 ID2" indicating that the corresponding DNA strings overlap
    :rtype: list[str]
    """
    adjacencyList = []
    for (ID1, DNAString1) in zip(fastaFormat.keys(), fastaFormat.values()):
        suffix = DNAString1[-3:]
        for (ID2, DNAString2) in zip(fastaFormat.keys(), fastaFormat.values()):
            prefix = DNAString2[0:3]
            if ID1 != ID2 and suffix == prefix:
                adjacencyList.append(ID1 + " " + ID2)

    setOutputToFile("\n".join(adjacencyList))
    return adjacencyList

def main():
    fastaFormat = getInputFromFASTAFileWithID(filename)
    setOutputToFile("\n".join(overlapStrings(fastaFormat, 3)))

if __name__ == "__main__":
    main()
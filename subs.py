import os
from rosalindUtilities import getInputFromFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def findMotifInDNA(DNASequence, motif):
    """
    Finds all occurrences of a motif within a DNA sequence and returns their positions.

    :param str DNASequence: The DNA sequence in which to search for the motif.
    :param str motif: The motif to search for within the DNA sequence.
    :return: A list of positions (1-based index) where the motif is found in the DNA sequence.
    :rtype: list
    """
    indexsOfMotif = []
    i = DNASequence.find(motif)
    
    while i > 0:
        indexsOfMotif.append(str(i+1))
        i = DNASequence.find(motif, i+1)

    return indexsOfMotif

def main():
    DNASequence, motif, *_ = getInputFromFile(filename).split("\n")
    setOutputToFile(" ".join(findMotifInDNA(DNASequence, motif)))

if __name__ == "__main__":
    main()
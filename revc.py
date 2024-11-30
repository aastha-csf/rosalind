import os
from rosalindUtilities import getInputFromFile, setOutputToFile
# print("data/rosalind_" + os.path.basename(__file__)[:-2] + "txt")
def complementing_a_strand_of_DNA(filename):
    dnaSequence = getInputFromFile(filename).split("\n")[0]
    reversedComplementDNA = "".join([_complement(x) for x in dnaSequence[len(dnaSequence)-1::-1]])
    setOutputToFile(reversedComplementDNA)
    return reversedComplementDNA
            
def _complement(base: str):
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "G":
        return "C"
    elif base == "C":
        return "G"

print(complementing_a_strand_of_DNA("data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"))
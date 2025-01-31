import os
from rosalindUtilities import getInputFromFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def rna_to_protein(RNAString):
    # get RNA Codon table from file 
    """
    Translates an RNA string into a protein string using an RNA codon table.

    :param str RNAString: The RNA sequence to be translated.
    :return: The resulting protein string, with each codon translated to its corresponding amino acid.
    :rtype: str
    """
    RNACodons = getInputFromFile("resorces/RNACodonTable.txt").split()
   
    RNACodonsDict = {}
    for (codon, aminoAcid) in zip(RNACodons[::2], RNACodons[1::2]):
        RNACodonsDict[codon] = aminoAcid

    proteinString = ""
    [(proteinString := proteinString+ RNACodonsDict["".join(codon)]) for codon in zip(RNAString[::3], RNAString[1::3], RNAString[2::3]) if RNACodonsDict["".join(codon)] != "Stop"]

    return proteinString

def main():
    rnaString = getInputFromFile(filename)
    setOutputToFile(rna_to_protein(rnaString))

if __name__ == "__main__":
    main()
import os 
from rosalindUtilities import getInputFromFASTAFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def getProfileAndConsensus(DNASequences):
    """
    Generates the consensus string and profile matrix for a list of DNA sequences.

    :param list DNASequences: A list of DNA sequences represented as strings.
    :return: A tuple containing the profile matrix as a list of strings and the consensus string.
    :rtype: tuple(profile,consensus)
    """
    consensus = ""
    profile = ["A: ", "C: ", "G: ", "T: "]
    l = len(DNASequences[0])
    for i in range(l):
        # for each index of the DNA Sequences 
        # count its nucleotides
        # determine max nucleotide to determine letter of consensus string 

        A, C, G, T = 0, 0, 0, 0

        for DNAString in DNASequences:
            base = DNAString[i]
            if base == "A":
                A+=1
            elif base == "C":
                C+=1
            elif base == "G":
                G+=1
            elif base == "T":
                T+=1

        pairs = ((A, "A"), (C,"C"), (G,"G"), (T,"T"))

        consensus = consensus + max(pairs)[1] 

        profile[0] += " " + str(pairs[0][0])
        profile[1] += " " + str(pairs[1][0])
        profile[2] += " " + str(pairs[2][0])
        profile[3] += " " + str(pairs[3][0])
    
    return (profile, consensus)

def main():
    profile, consensus = getProfileAndConsensus(getInputFromFASTAFile(filename))
    setOutputToFile(consensus + "\n" + profile[0] + "\n" + profile[1] + "\n" + profile[2] + "\n" + profile[3])

if __name__ == "__main__":
    main()
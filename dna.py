from rosalindUtilities import setOutputToFile, getInputFromFile
def countingDnaNucleotides(filename):
    dna = getInputFromFile(filename)
    A, C, G, T = 0, 0, 0, 0
    for nucleotide in dna:
        if nucleotide == "A":
            A += 1
        elif nucleotide == "C":
            C += 1
        elif nucleotide == "G":
            G += 1
        elif nucleotide == "T":
            T += 1
    output = str(A) + " " + str(C) + " " + str(G) + " " + str(T)
    return output

print(countingDnaNucleotides("data/rosalind_dna.txt"))
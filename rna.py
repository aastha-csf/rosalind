from rosalindUtilities import setOutputToFile, getInputFromFile

def transcribingDnaIntoRna(filename):
    dna = getInputFromFile(filename)
    rna = dna.replace('T','U')
    setOutputToFile(rna)
    return rna

print(transcribingDnaIntoRna("data/rosalind_rna.txt"))

import os
from rosalindUtilities import getInputFromFASTAFileWithID, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def max_gc_content(FASTA_format_DNA_string):
    """
    Given a dictionary of DNA strings with their IDs, this function returns the ID
    of the string with the highest GC content and the GC content itself.
    
    Parameters:
        FASTA_format_DNA_string (dictionary): A dictionary of DNA strings with their IDs.
    
    Returns:
        tuple: A tuple of the ID of the DNA string with the highest GC content and the GC content itself.
    """
    maxGCCcontent = 0
    IDofMaxGCContent = ""

    for ID, nucleobaseSeq in FASTA_format_DNA_string.items():
        GCContent = (countGC(nucleobaseSeq) / len(nucleobaseSeq))*100
        if(GCContent > maxGCCcontent):
            maxGCCcontent = GCContent
            IDofMaxGCContent = ID

    return (IDofMaxGCContent, maxGCCcontent)

def countGC(nucleobaseSeq: str) -> int:
    """Counts the number of G+C in a DNA sequence."""
    counter: int = 0
    for base in nucleobaseSeq:
        if base == 'G' or base == 'C':
            counter = counter +1 
    return counter
    
def main():
    ID, maxGC = max_gc_content(getInputFromFASTAFileWithID(filename))
    setOutputToFile(str(ID) + "\n" + str(maxGC))

if __name__ == "__main__":
    main()


import os 
from rosalindUtilities import getInputFromFile, setOutputToFile

filename = "data/rosalind_" + os.path.basename(__file__)[:-2] + "txt"

def getProbabilityOffspringWithDomAllele(k, m, n):
    """
    This function takes in 3 parameters, k, m, and n, and 
    returns the probability of an offspring having a dominant allele 
    
    :param int k: The number of organisms that are homozygous recessive
    :param int m: The number of organisms that are heterozygous
    :param int n: The number of organisms that are homozygous dominant
    :return: The probability that two randomly selected organisms will produce an offspring with a dominant allele
    :rtype: float
    """
    totalOrganisms = k+m+n
    totalOffspring = (((totalOrganisms-1)*(totalOrganisms)) / 2) * 4

    A = totalOrganisms

    offSpringWithDomAllele = (
            ((k/A)*((k-1)/(A-1)) * totalOffspring)  +
            ((2 * (k/A)*(m/(A-1))) * totalOffspring)  +
            ((2 * (k/A)*(n/(A-1))) * totalOffspring)   +
            (((m/A)*((m-1)/(A-1))) * ((3/4) * totalOffspring)) +
            ((2 * (m/A)*(n/(A-1))) * ((2/4) * totalOffspring))    )

    return offSpringWithDomAllele/ totalOffspring

def main():
    k, m, n = (int(input) for input in getInputFromFile(filename).split())
    setOutputToFile(str(getProbabilityOffspringWithDomAllele(k, m, n)))

if __name__ == "__main__":
    main()
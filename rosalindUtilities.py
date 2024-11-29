from shutil import ReadError

def getInputFromFile(fileName: str):
    """
    Reads the contents of a file and returns it as a string.

    Parameters:
        fileName (str): The name of the file to be read.

    Returns:
        str: The contents of the file as a string.

    Raises:
        ReadError: If there is an error reading the file.
    """

    try:
        with open(fileName) as inputFile:
            return inputFile.read()
            
    except ReadError:
        print("no input file")

def setOutputToFile(output: str):
    """
    Writes the given output string to a file named "output.txt".

    Parameters:
        output (str): The output string to be written to the file.

    Returns:
        None
    """

    open("output.txt", "w+").close()
    with open("output.txt", 'w') as outputFile:
        outputFile.write(output)

def getInputFromFASTAFile(fileName: str):
    """
    Reads a FASTA file and returns a list of DNA sequences in the file.

    Parameters:
        fileName (str): The name of the FASTA file to be read.

    Returns:
        list: A list of DNA sequences in the file.
    """
    
    DNAString = ""
    dataset = []
    for line in getInputFromFile(fileName).split("\n"):
        if line.startswith(">") or line == "":
            dataset.append(DNAString)
            DNAString = ""
        else:
            DNAString = DNAString + line

    return dataset[1::]

def getInputFromFASTAFileWithID(fileName: str):
    """
    Reads a FASTA file and returns a list containing sequence IDs and their corresponding DNA sequences.

    Parameters:
        fileName (str): The name of the FASTA file to be read.

    Returns:
        list: A list where each DNA sequence is preceded by its sequence ID.
    """

    DNAString = ""
    dataset = []
    for line in getInputFromFile(fileName).split("\n"):
        if line.startswith(">"):
            if DNAString != "":
                dataset.append(DNAString)
                DNAString = ""
            dataset.append(line)
        else:
            DNAString = DNAString + line
            
    dataset.append(DNAString)

    return dataset[::]

def printMatrix(matrix=""):
    """
    Prints a matrix.

    Parameters:
        matrix (list): The matrix to be printed.

    Returns:
        None

    """

    print('\n'.join([' '.join([str(i) for i in y]) for y in matrix]))
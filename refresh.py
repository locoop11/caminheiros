# 2023-2024 Programacao 2 LTI
# Grupo 42
# 60253 Hugo Silva
# 60232 DUarte Correia
import os
from runner import Runner
import sys

def printUsage(message):
    print(message)
    print("Usage: python refresh.py <network filename> <connections filename> <output filename>")
    print("    <network filename>: Mandatory parameter. The name of the file with the network information in the form *LevadasNetwork*.txt")
    print("    <connections filename>: Mandatory parameter. The name of the file with the connections information in the form *Stations*.txt")
    print("    <output filename>: Mandatory parameter. The name of the file where the results will be saved in the form *Results*.txt")
    print("\n Environment Variables:\n   <NUMBER_OF_BEST_PATHS>: Optional parameter. The number of best paths to be saved. Default value is 3.")


def main():
    """
    Main program.
    Requires:
    Three command-line arguments, corresponding to the names of the files
    with the list of doctors, the list of birth assistances and the list of requests, respectively.
    """
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 4:
        printUsage("Usage Error: Invalid number of arguments.")
        return
    
    # Extract the file names from the command-line arguments

    networkFileName = ""
    connectionsFileName = ""
    resultFileName = ""

    k = (os.getenv('NUMBER_OF_BEST_PATHS', '3'))
    #verificar se o k é um inteiro
    try:
        k = int(k)
    except ValueError:
        k = 3
        return
    print(sys.argv)
    for file in sys.argv:
        if file.find("LevadasNetwork") != -1:
            networkFileName = file
        if file.find("Stations") != -1:
            connectionsFileName = file
        if file.find("Results") != -1:
            resultFileName = file
    
    if( networkFileName == "" or connectionsFileName == "" or resultFileName == ""):
        printUsage("Usage Error: Missing mandatory file.")
        exit(1)
    try:
        #"Para os testes" runner = Runner("./testSets_v1/testSet1/doctors10h00.txt", "./testSets_v1/testSet1/requests10h30.txt", "./testSets_v1/testSet1/schedule10h00.txt")
        runner = Runner(networkFileName, connectionsFileName, resultFileName, k)
        runner.run()
        

    except Exception as e:
        print(f"An error occurred: {e.with_traceback()}")
        print(f"An error occurred: {e}")
        # Optionally, you can perform additional error handling here if needed

        # Exit in a controlled way (e.g., with a specific exit code)
        exit(1)  # Exit with a non-zero exit code to indicate an error

if __name__ == "__main__":
    main()
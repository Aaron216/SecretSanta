import sys
import os
import random

# Constants
BUDGET = "$30.00"

# Main function
def main():
    # Check python version
    if sys.version_info.major < 3:
        print("Error: Requires Python 3")
        print("Exiting.\n")
        exit()

    # Check input arguments
    if len(sys.argv) != 3:
        print("Error: Incorrect number of input arguments.")
        print(f"Ussage: {sys.argv[0]} <Participants filepath> <Output folder>")
        print("Exiting.\n")
        exit()

    filepath = str(sys.argv[1])
    outputFolder = str(sys.argv[2])

    partList = open_file(filepath)      # Create participants list
    assign_santas(partList)             # Assign secret santas
    write_files(partList, outputFolder) # Write files

    print("Complete.\n")

def open_file(filepath):
    partList = []

    # Check if file exisits
    if os.path.exists(filepath):
        with open(filepath, mode='r') as inputFile:
            # Create participants
            for row in inputFile:
                if len(row) != 0:
                    partList.append([row.strip(), ""])
            inputFile.close()
        print(f"Read participant file: {filepath}")
    else:
        print(f"Error: Cannot read file: {filepath}")
        print("Exiting.\n")
        exit()
    return partList

def assign_santas(partList):
    random.shuffle(partList)
    for ii in range(0, len(partList)):
        partList[ii][1] = partList[(ii+1)%len(partList)][0]

def write_files(partList, outputFolder):
    if not os.path.exists(outputFolder):
        os.mkdir(outputFolder)

    for part in partList:
        write_file(part, outputFolder)

def write_file(part, outputFolder):
    fileName = f"{outputFolder}/{part[0]}_Santa.txt"
    fileContent = (
        f"To {part[0]},\n" +
        f"You get to buy a secret santa present for {part[1]}.\n" +
        f"The budget is {BUDGET}.\n"
        "Good luck.\n"
    )

    outputFile = open(fileName, mode='w', newline='\r\n')
    outputFile.write(fileContent)
    outputFile.close()

    print(f"File created: {fileName}")

if __name__ == "__main__":
    main()

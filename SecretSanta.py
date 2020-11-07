import sys
import os
import random

from tabulate import tabulate

# Main function
def main():
    # Check input arguments
    if len(sys.argv) != 2:
        print("Error: Incorrect number of input arguments.")
        print(f"Ussage: {sys.argv[0]} <Participants filepath>")
        print("Exiting.\n")
        exit()

    filepath = str(sys.argv[1])

    partList = open_file(filepath)  # Create participants list
    assign_santas(partList)         # Assign secret santas
    write_files(partList)           # Write files

    print(tabulate(partList, headers=['Name', 'Recipient']))
    print("Complete.")

def open_file(filepath):
    partList = []

    # Check if file exisits
    if os.path.exists(filepath):
        with open(filepath, mode='r') as inputFile:
            # Create participants
            for row in inputFile:
                if len(row) != 0:
                    partList.append([row, ""])
            inputFile.close()
    return partList

def assign_santas(partList):
    random.shuffle(partList)
    for ii in range(0, len(partList)):
        partList[ii][1] = partList[(ii+1)%len(partList)][0]

def write_files(partList):
    for part in partList:
        write_file(part)

def write_file(part):
    fileName = part[0] + "_Santa.txt"
    fileContent = (
        "To " + part[0] + ",\n" +
        "You get to buy a secret santa present for " + part[1] + ".\n" +
        "The budget is $30.00.\n"
        "Good luck.\n"
    )

    outputFile = open(fileName, mode='w', newline='\r\n')
    outputFile.write(fileContent)
    outputFile.close()

if __name__ == "__main__":
    main()

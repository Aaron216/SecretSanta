import sys
import os
import random

from PIL import Image, ImageDraw, ImageFont

# Constants
BUDGET = '$30.00'
FONTS_FOLDER = 'C:\Windows\Fonts'

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
    fileName = os.path.join(outputFolder, f"{part[0]}_Santa.png")
    fileContent = (
        f"To {part[0]},\n" +
        "You get to buy a secret \n" +
        f"santa present for {part[1]}.\n" +
        f"The budget is {BUDGET}.\n"
        "Good luck.\n"
    )

    im = Image.new('RGBA', (600, 250), 'white')
    draw = ImageDraw.Draw(im)
    fontsFolder = FONTS_FOLDER
    robotoFont = ImageFont.truetype(os.path.join(fontsFolder, 'Roboto-Regular.ttf'), 32)
    draw.text((20, 20), fileContent, fill='black', font=robotoFont)
    im.save(fileName)

    print(f"File created: {fileName}")

if __name__ == "__main__":
    main()

inputFile = "your_input_file.txt"
outputFile = "your_output_file.txt"
stringToAppend = "https://"

with open(inputFile, 'r') as inFile, open(outputFile, 'w') as outFile:
    for line in inFile:
        outFile.write(stringToAppend+line)


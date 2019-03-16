import sys

def CopyFileData(inputfile, outputfile, countoflines):
    inputfd = open(inputfile)
    outputfd = open(outputfile, "w")

    count = 1
    line = inputfd.readline()
    while line != "":
        if(count > countoflines):
            break
        outputfd.write(line)
        line = inputfd.readline()
        count += 1
    
def main():

    if(len(sys.argv) != 4):
        print("Please enter valid argument list")
        print("<program name> <inputFile> <outputFile> <countoflines>")
    else:
        print(sys.argv)
        CopyFileData(str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

#print all words having 'end' in between

import re

def PrintEndInBetween(filename):
    fd = open(filename)
    data = fd.read()
    without_case=re.compile(r"\w+end\B",re.IGNORECASE)

    for match in without_case.findall(data):
        print(match)
        

def main():
    filename = eval(input("Enter file name :"))
    PrintEndInBetween(filename)
    

if __name__ == "__main__":
    main()

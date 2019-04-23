#print all verbs(ly or ing at end)

import re

def PrintVerbs(filename):
    fd = open(filename)
    data = fd.read()
    regxobj=re.compile(r"\w+ly|\w+ing\b", re.IGNORECASE)

    for match in regxobj.findall(data):
        print(match)
        

def main():
    filename = eval(input("Enter file name :"))
    PrintVerbs(filename)
    

if __name__ == "__main__":
    main()

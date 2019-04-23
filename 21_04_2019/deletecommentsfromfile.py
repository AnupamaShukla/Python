#delete all coments from file
#read file in buffer and close
#for singleline comment:
#start with # and end with \n
#need to use re.multiline
#for multiline comment:
#start and end with ''' or """ (including \n as well)
#open same file in write mode and dump the updated buffer

import re

def DeleteComments(filename):
    fd = open(filename)
    data = fd.read()
    fd.close()

    #for single line comment

    data = re.sub(re.compile(r"#.*?\n"),"",data)

    #for ''' or """ multiline comment
    data = re.sub(re.compile(r'\'''(.|[\r\n])*\'''',re.DOTALL | re.MULTILINE),"",data)
    data = re.sub(re.compile(r'\"""(.|[\r\n])*\"""',re.DOTALL | re.MULTILINE),"",data)

    #for '''  or """ multiline comment (alternative)
    #data = re.sub(re.compile(r"'''.*?'''",re.DOTALL | re.MULTILINE),"",data)
    #data = re.sub(re.compile(r'""".*?"""',re.DOTALL | re.MULTILINE),"",data)
    
    print(data)

    fd = open(filename, "w")
    fd.write(data)
    fd.close()
        

def main():
    filename = eval(input("Enter file name :"))
    DeleteComments(filename)
    #DeleteComments("try.txt")
    

if __name__ == "__main__":
    main()

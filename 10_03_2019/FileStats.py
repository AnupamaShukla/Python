import os
import time
from stat import *

def PrintFileStats(filename):
    statdata = os.stat(filename)

    print("size = " +str(statdata[ST_SIZE]))
    print("Inode no = " +str(statdata[ST_INO]))
    print("Mode = " +str(statdata[ST_MODE]))
    print("last accessed time = " +str(time.asctime(time.localtime(statdata[ST_ATIME]))))
    print("last modified time = " +str(time.asctime(time.localtime(statdata[ST_MTIME]))))
    print("last matadata changed time = " +str(time.asctime(time.localtime(statdata[ST_CTIME]))))
    

def main():
    inputFile = eval (input("Enter File Name:"))
    PrintFileStats(inputFile)

if __name__ == '__main__':
    main()

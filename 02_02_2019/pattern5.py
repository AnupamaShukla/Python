
# print following pattern
#        *
#      * * *
#    * * * * *
#      * * *
#        *

def pattern(num):
    n = 0
    for x in range (1,num+1):
        for _ in range (1,(num-x)+1):
            print (end=' ')
        while n != (2*x-1):
            print ('*',end='')
            n = n+1
        n = 0
        print()

    k = 1
    n = 1
    for x in range (1,num):
        for _ in range (1,k+1):
            print (end=' ')
        k = k+1
        while n <= 2*(num-x)-1:
            print ('*',end='')
            n = n+1
        n = 1
        print()
    

def main():
    no=int(input("Enter Number of rows:"))
    pattern(no)

if __name__ == '__main__':
    main()

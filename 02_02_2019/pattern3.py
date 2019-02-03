
# print following pattern
#       A
#     B A B
#   C B A B C
# D C B A B C D


def pattern(n):
    for x in range(1,n+1):
        for _ in range (1,n-x+1):
            print (" ",end=' ')
        temp=x
        for j in range (1,x*2):
            print (chr(temp+64),end=' ')
            if(j<x):
                temp = temp - 1
            else:
                temp = temp + 1
        print()

def main():
    no=int(input("Enter Number :"))
    pattern(no)

if __name__ == '__main__':
    main()



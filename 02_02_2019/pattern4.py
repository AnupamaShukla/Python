
# print following pattern
# * * * * * * *
# * * *   * * *
# * *       * *
# *           *


def Pattern(n):

    for _ in range(0,n*2+1):
      print("*",end='')
    print()
      
    for x in range(0,n):
        # left *
        for _ in range(x,n):
            print("*",end='')

        # middle space
        for _ in range(0,2*x+1):
            print(" ",end='')

        # right *
        for _ in range(x,n):
            print("*", end='')

        print()

def main():
    no=int(input("Enter Number :"))
    Pattern(no)

if __name__ == '__main__':
    main()

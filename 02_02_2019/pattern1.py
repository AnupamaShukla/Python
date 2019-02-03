
# print following pattern
# * * * *
#   * * *
#     * *
#       *

def PrintPattern(n):

    for i in range(1,n):
        for _ in range(1,i):
            print(" ", end=' ')
        for _ in range(1, n-i+2):
            print("*", end=' ')
        print()


def main():
    number = int (input("Enter Number of rows:"))
    PrintPattern(number)

if __name__ == '__main__':
    main()



# print following pattern
# * * * *
# * * *
# * *
# *

def PrintPattern(n):

    for i in range(0,n):
        for _ in range(0, n-i):
            print("*", end=' ')
        print()


def main():
    number = int (input("Enter Number of rows:"))
    PrintPattern(number)

if __name__ == '__main__':
    main()


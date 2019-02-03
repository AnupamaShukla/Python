
def Reverse(num):

    rem = 0
    rev = 0

    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num//10
    return rev

def PrintWord(num):
    
    rev = Reverse(num)
    while rev != 0:
        temp = rev % 10
        if temp == 0:
            print("Zero", end=' ')
        if temp == 1:
            print("One", end=' ')
        if temp == 2:
            print("Two", end=' ')
        if temp == 3:
            print("Three", end=' ')
        if temp == 4:
            print("Four", end=' ')
        if temp == 5:
            print("Five", end=' ')
        if temp == 6:
            print("Six", end=' ')
        if temp == 7:
            print("Seven", end=' ')
        if temp == 8:
            print("Eight", end=' ')
        if temp ==9:
            print("Nine", end=' ')
            
        rev = rev // 10

def main():
    number = int (input("Enter Number: "))
    PrintWord(number)

if __name__ == '__main__':
    main()


# Print fibonacci series upto given number


def fibo(number):
    temp1=1
    temp2=1
    print(temp1,temp2,end=' ')
    while True:
        temp3=temp1+temp2
        if(temp3>number):
            break
        print(temp3,end=' ')
        temp1=temp2
        temp2=temp3
        
def main():
    num = int (input("Enter number:"))
    fibo(num)

if __name__ == '__main__':
    main()


import math
def IsPrime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num%2 == 0:
        return False

    max_value_to_check = math.floor(math.sqrt(num))

    for x in range(3, max_value_to_check+1, 2):
        if num%x == 0:
            return False
    return True

def main():
    number = int (input("Enter No to check Prime:"))
    print(IsPrime(number))

if __name__ == '__main__':
    main()
        
    

def FromKeys(Input, value):
    if (type(value)) == list:
        y = 0
        for key in Input:
            Input[key] = value[y]
            if len(value) > 1:
                y += 1
        return Input
    
def main():
    inputDict = eval (input("Enter Key value in dict:"))
    values = eval (input("Enter list of value :"))
    print("Existing dict:" +str(inputDict))
    newDict = FromKeys(inputDict,values)
    print("New dict:" +str(newDict))

if __name__ == '__main__':
    main()

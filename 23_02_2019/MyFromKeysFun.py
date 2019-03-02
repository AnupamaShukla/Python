def FromKeys(Input, value):
    if (type(value)) == list:
        y = 0
        for key in Input:
            if(y >= len(value)):
                Input[key] = None
                continue
            Input[key] = value[y]
            y += 1
        return Input
    else:
        res = dict.fromkeys(Input,value)
        return res
    
def main():
    inputDict = eval (input("Enter Key value in dict:"))
    values = eval (input("Enter list of value :"))
    print("Existing dict:" +str(inputDict))
    newDict = FromKeys(inputDict,values)
    print("New dict:" +str(newDict))

if __name__ == '__main__':
    main()

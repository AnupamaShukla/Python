def DictOfUpperLower(inputstr):
    res = {"Upper":None, "Lower":None}

    UpCount = 0
    LowCount = 0
    for ch in inputstr:
        if ch.isupper():
            UpCount += 1
        elif ch.islower():
            LowCount += 1
    res["Upper"] = UpCount
    res["Lower"] = LowCount
    return res
            

def main():
    inputstr = eval (input("Enter sentence:"))
    res = DictOfUpperLower(inputstr)
    print(str(res))
    

if __name__ == '__main__':
    main()

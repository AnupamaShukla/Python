
#bubble Sort
def SortList(List1):
    length = len(List1)
    for x in range (length):
        for y in range (0,length-x-1):
            if List1[y] > List1[y+1]:
                temp = List1[y]
                List1[y] = List1[y+1]
                List1[y+1] = temp

def main():
    list1 = eval(input("Enter List of integers:"))
    SortList(list1)
    print(list1)
    
if __name__=='__main__':
    main()

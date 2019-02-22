def EnQueue(List1, x):
    if False == IsFull(List1):
        List1.append(x)

def Peep(List1):
    return List1[-1]
    
def DeQueue(List1):
    if False == IsEmpty(List1):
        List1.remove(1)
    
def IsFull(List1):
    if len(List1) == 10:
        return True
    else:
        return False
    
def IsEmpty(List1):
    if len(List1) == 0:
        return True
    else:
        return False

def main():
    list1 = eval(input("Enter List:"))
    print("1.Enqueue\n2.Dequeue\n3.IsEmpty\n4.IsFull\n5.Peep\n6.Exit")
    choice = int(input("Enter your choice:"))
    while (choice != 6):
        if(choice == 1):
            num = int(input("Enter number to add in queue:"))
            EnQueue(list1,num)
            print(list1)
        if(choice == 2):
            DeQueue(list1)
            print(list1)
        if(choice == 3):
            res = IsEmpty(list1)
            print(res)
        if(choice == 4):
            res = IsFull(list1)
            print(res)
        if(choice == 5):
            res = Peep(list1)
            print(res)
        choice = int(input("Enter your choice:"))
    
if __name__=='__main__':
    main()

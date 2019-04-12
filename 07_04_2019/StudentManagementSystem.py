#!/usr/bin/python

class Student:
    auto_roll_no = 1
    def __init__(self, name, address, dob, course, division):
        self.__roll_no = Student.auto_roll_no
        Student.auto_roll_no += 1
        self.__name = name
        self.__address = address
        self.__dob = dob
        self.__course = course
        self.__division = division
        self.__marks = dict()
    def getRollNo(self):
        return self.__roll_no
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getDOB(self):
        return self.__dob
    def getCourse(self):
        return self.__course
    def getDivision(self):
        return self.__division
    def getMarks(self):
        return self.__marks
    def updateAddress(self, address):
        self.__address = address
    def updateMarks(self, subject, marks):
        self.__marks[subject] = marks
    def updateCourse(self, course):
        self.__course = course
    def updateDivision(self, division):
        self.__division = division
    def __repr__(self):
        return "Name:"+self.__name+"\nAddress:"+self.__address+"\nDOB:"+self.__dob+"\nCourse:"+self.__course+"\nDivision:"+self.__division+"\nMarks:"+str(self.__marks)+"\nRoll No:"+str(self.__roll_no)

class StudentManager:
    def __init__(self, noOfStudents):
        self.__no_of_students = noOfStudents
        self.__enrolled_students = dict()
        self.__suspended_students = dict()

    def GetEnrolledStudents(self):
        return self.__enrolled_students

    def GetSuspendedStudents(self):
        return self.__suspended_students

    def EnrollStudent(self, name, address, dob, course, div):
        st = Student(name, address, dob, course, div)
        self.__enrolled_students[st.getRollNo()] = st

    def SuspendStudent(self, roll_no):
        if roll_no in self.__suspended_students:
            pass
        elif roll_no in self.__enrolled_students:
            st = self.__enrolled_students.pop(roll_no)
            self.__suspended_students[roll_no] = st
        else:
            return False
        return True

    def UpdateMarks(self, roll_no, subject, marks):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateMarks(subject, marks)
            return True
        return False
    def GetMarks(self, roll_no):
        return self.__enrolled_students[roll_no].getMarks()

    def UpdateAddress(self, roll_no, address):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateAddress(address)
            return True
        return False
    def GetAddress(self, roll_no):
        return self.__enrolled_students[roll_no].getAddress()
        
    def UpdateCourse(self, roll_no, course):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateCourse(course)
            return True
        return False
    def GetCourse(self, roll_no):
        return self.__enrolled_students[roll_no].getCourse()

    def UpdateDivision(self, roll_no, division):
        if roll_no in self.__enrolled_students:
            self.__enrolled_students[roll_no].updateDivision(division)
            return True
        return False
    def GetDivision(self, roll_no):
        return self.__enrolled_students[roll_no].getDivision()
    
def Menu():
    print("*********MENU************\n1. Enroll Student\n2. Suspend Student\n3. Print All Students\n4. Print Enrolled Students with Percentage\n5. Print Suspended Students\n6. Update Student Details\n7. Exit\n")
    choice = eval(input("Enter your choice:"))
    return choice

def StudentManagementSystem(no_of_students):
    sm = StudentManager(no_of_students)
    while True:
        ch = Menu()
        if (ch == 7):
            break
        if (ch < 1 or ch > 7):
            print("Please Enter valid choice!")
        
        if ch == 1:
            name = eval(input("Enter Student Name:"))
            address = eval(input("Enter Student Address:"))
            dob = eval(input("Enter Student Date Of Birth (DD-MM-YYYY):"))
            course = eval(input("Enter Student class:"))
            div = eval(input("Enter Student division:"))
            sm.EnrollStudent(name, address, dob, course, div)

        if ch == 2:
            roll_no = eval(input("Enter Student Roll No to suspend:"))
            sm.SuspendStudent(roll_no)
            
        if ch == 3:
            print("\n***********Displaying Enrolled Students*********\n")
            en_students =  sm.GetEnrolledStudents()
            for st in en_students:
                print(en_students[st])

            print("\n***********Displaying Suspended Students**********\n")
            sus_students =  sm.GetSuspendedStudents()
            for st in sus_students:
                print(sus_students[st])

        if ch == 4:
            print("\n***********Displaying Enrolled Students with Percentage*********\n")
            en_students =  sm.GetEnrolledStudents()
            for st in en_students:
                print(en_students[st])

                mark_dict = en_students[st].getMarks()
                totalmark = 0
                for key in mark_dict:
                    totalmark = totalmark + mark_dict[key]

                perc = totalmark / (len(mark_dict)*100) * 100
                print("Percentage:" + str(perc))

        if ch == 5:
            print("\n***********Displaying Suspended Students**********\n")
            sus_students =  sm.GetSuspendedStudents()
            for st in sus_students:
                print(sus_students[st])

        if ch == 6:
            rollNo = eval(input("Enter Roll no for which you want to update data:"))
            while True:
                subchoice = eval(input(" 1.Address\n 2.Division\n 3.Course\n 4.Marks\n 5.Exit\n Enter your choice to update : "))
                
                if subchoice < 1 or subchoice > 4:
                    print ("Please enter correct choice")
                if subchoice == 5:
                    break
                if subchoice == 1:
                    addr = eval(input("Enter updated address:"))
                    sm.UpdateAddress(rollNo, addr)
                if subchoice == 2:
                    Div = eval(input("Enter updated division:"))
                    sm.UpdateDivision(rollNo, Div)
                if subchoice == 3:
                    Course = eval(input("Enter updated course:"))
                    sm.UpdateCourse(rollNo, Course)
                if subchoice == 4:
                    subject,Marks = eval(input("Enter subject and updated marks:"))
                    sm.UpdateMarks(rollNo, subject, Marks)
        
def main():
    no_of_students = eval(input("Enter student count :"))
    StudentManagementSystem(no_of_students)
    
if __name__ == "__main__":
    main()

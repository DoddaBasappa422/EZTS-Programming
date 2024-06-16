'''class A:
    def __init__(self,a,b):
        self.a=a
        self.__b=b
    def PrintB(self):
        print(self.__b)

obj1=A(2,3)
print(obj1.a)
obj1.PrintB()
'''


#create a student class that holds the details of students like 
# name,USN and the marks in 5 subjects percentage and grade
#create 5 student object and get the data for name,usn and marks after that 
# find the percentage and grade and store it to the class object.




class Student:
    
    def __init__(self, name, usn):
        self.name = name
        self.usn = usn
        self.marks_list = []

    def marks(self):
        total_marks = 0
        for i in range(5):
            mark = float(input("Enter marks for subject {}: ".format(i+1)))
            self.marks_list.append(mark)
            total_marks += mark
        self.percentage = (total_marks / 5)

        if self.percentage >= 90:
            self.grade = 'A+'
        elif self.percentage >= 80:
            self.grade = 'A'
        elif self.percentage >= 70:
            self.grade = 'B+'
        elif self.percentage >= 60:
            self.grade = 'B'
        elif self.percentage >= 50:
            self.grade = 'C'
        elif self.percentage >= 40:
            self.grade = 'D'
        elif self.percentage >= 33:
            self.grade = 'E'
        else:
            self.grade = 'F'

    def details(self):
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Percentage:", self.percentage)
        print("Grade:", self.grade)

students = []
for i in range(5):
    name = input("Enter name of student {} : ".format(i+1))
    usn = input("Enter USN of student {}: ".format(i+1))
    student = Student(name, usn)
    student.marks()
    students.append(student)

print("\nStudent Details:")
for student in students:
    student.details()
    print()







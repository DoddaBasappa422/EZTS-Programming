'''class student:
    def __init__(self,name,age,gender):#__(double underscore defines that the function is private )
        self.name=name
        self.age=age
        self.gender=gender



st1=student("Ajay",18,"M")
print(st1.name,st1.age,st1.gender)'''


"""class student:
    def __init__(self):#__(double underscore defines that the function is private )
        self.name=None
        self.age=None
        self.gender=None



st1=student()
st1.name=input("Enter the name of the student:")
st1.age=input("Enter the age of the student:")
st1.gender=input("Enter the gender of the student:")
print(st1.name,st1.age,st1.gender)"""


class student:
    def __init__(self,name,age,gender):#__(double underscore defines that the function is private )
        self.name=name
        self.age=age
        self.gender=gender

a=input("Enter the name of the student:")  # a,b,c are the formal values
b=input("Enter the age of the student:")   # where self.name,self.age,self.gender are actual values
c=input("Enter the gender of the student:")
st1=student(a,b,c)
print(st1.name,st1.age,st1.gender)
print(type(st1))
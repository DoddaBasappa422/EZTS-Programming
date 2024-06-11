class arithmetic:

    def __init__(self):
        print("Some of Arithmetics are like addition,substraction,multiplication,division")

    def add(self):
        print("The sum of two numbers:")
        a=10
        b=5
        self.c=a+b
        print(self.c)
        
    def multiplication(self,d):
        print("The product of sum of two numbers and d:")
        print(self.c*d)

a=arithmetic()    
a.add()
a.multiplication(5)
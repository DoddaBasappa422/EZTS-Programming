class cse1:
    def __init__(self,a,b) : #parameterised constructor
        self.a1=a
        self.b1=b
        print("I am constructor")

    def strength(self):
        print("the strength is 101")
        self.s=101
    
    def kn(self,c,d):
        print("the knowledge is good")
        self.know="Good"
        pro=c*d
        print(pro)
    
    def details(self):
        print("the current strength and the knowledge")
        c_s=self.s-10
        print(c_s,self.know)
        print(self.a1+self.b1)

day_2=cse1(3,5)
day_2.strength()
day_2.kn(2,10)
day_2.details()

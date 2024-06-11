'''
1.Create a class of car show room in which create a function (name car company) which will allow a user to select car company out of the displayed company.
 if the user enters any random car company he or she should be asked to re-enter.
2.According to the car company selected the user should be redirected to selecting the models of that company out of the given list, if any random models entered then again re-enter.
3.After selecting the model the user should be redirected to selecting the variant.
4.According to the car company model and variant a price should be calculated to which SGST and CGST are added to make it the total price.
NOTE: SGST and CGST are common for all the cars'''


class car:
    def __init__(self):
        self.cgst=5555
        self.sgst=5555
        self.insurance=5555
    def company(self):
        while True:
                print("Toyota,Mercedes")
                self.n=input("Enter the car company: ")
                if self.n=="Toyota":
                     print("Welcome to toyo")
                     self.model()
                     break
                elif self.n=="Mercedes":
                    print("Welcome to mercedes")
                    self.model()
                    break
                else:
                     print("enter valid company")
    def model(self):
        if self.n=="Toyota":
            while True:
                print("Select from Fortuner and LC")
                self.choice=input("Enter the car model: ")
                if self.choice=="Fortuner":
                    self.p=4500000
                    while True:
                        print("Select from Petrol and Diesel")
                        self.choice=input("Enter the variant:")
                        if self.choice=="Petrol":
                            self.price(self.choice,self.p)
                            break
                        elif self.choice=="Diesel":
                            self.price(self.choice,self.p)
                            break
                        else:
                            print("Enter valid")
                    break
                elif self.choice=="LC":
                    self.p=1000000
                    while True:
                        print("Select from Petrol and Diesel")
                        self.choice=input("Enter the variant:")
                        if self.choice=="Petrol":     
                            self.price(self.choice,self.p)
                            break
                        elif self.choice=="Diesel":
                            self.price(self.choice,self.p)
                            break
                        else:
                            print("Enter valid")
                    break
                else:
                    print("Enter valid")
        elif self.n=="Mercedes":
            while True:
                print("Select from amg and gw")
                self.choice=input("Enter the car model: ")
                if self.choice=="amg":
                    self.p=24432874
                    while True:
                        print("Select from Petrol and Diesel")
                        self.choice=input("Enter the variant:")
                        if self.choice=="Petrol":
                            self.price(self.choice,self.p)
                            break
                        elif self.choice=="Diesel":
                            self.price(self.choice,self.p)
                            break
                        else:
                            print("Enter valid")
                    break        
                elif self.choice=="gw":
                    self.p=843726837
                    while True:
                        print("Select from Petrol and Diesel")
                        self.choice=input("Enter the variant:")
                        if self.choice=="Petrol":   
                            self.price(self.choice,self.p)
                            break
                        elif self.choice=="Diesel":
                            self.price(self.choice,self.p)
                            break
                        else:
                           print("Enter valid")
                    break
                else:
                    print("Enter valid")
    def price(self,choice,pr):
        self.pr=0
        if choice=="Petrol":
            self.pr=110
        elif choice=="Diesel":
            self.pr=95   
        tot_p=self.p+self.sgst+self.cgst+self.insurance+self.pr
        print(tot_p)
c=car()
c.company()
        
              
       
            
        
    
     
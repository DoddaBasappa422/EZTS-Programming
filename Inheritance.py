'''
#Simple inheritence
class employee:
    def __init__(self,name,dprt,e_id):
        self.name=name
        self.dprt=dprt
        self.e_id=e_id
    def print_info(self):
        print("Employee details:",self.name,self.dprt,self.e_id)
obj = employee("Ajay","RTS",1001)
obj.print_info()

class rts(employee):
    pass
obj1 = rts("Arun","RTS",1003)
obj1.print_info()

'''
'''#Hierarchial inheritance
class employee:
    def __init__(self,name,dprt,e_id):
        self.name=name
        self.dprt=dprt
        self.e_id=e_id
    def print_info(self):
        print("Employee details:",self.name,self.dprt,self.e_id)
obj = employee("Ajay","RTS",1001)
obj.print_info()

class rts(employee):
    pass
obj1 = rts("Arun","RTS",1003)
obj1.print_info()

class Indu(employee):
    pass
obj1 = rts("Amar","Indu",1004)
obj1.print_info()'''

'''#Multilevel inheritance

class manager:
    print("Manager is the main employee of company")

class employee:
    def __init__(self,name,dprt,e_id):
        self.name=name
        self.dprt=dprt
        self.e_id=e_id
    def print_info(self):
        print("Employee details:",self.name,self.dprt,self.e_id)
obj = employee("Ajay","RTS",1001)
obj.print_info()

class rts(manager,employee):
    pass
obj1 = rts("Arun","RTS",1003)
obj1.print_info()
'''

#Multiple inheritance

class manager:
    print("Manager is the main employee of company")

class employee(manager):
    def __init__(self,name,dprt,e_id):
        self.name=name
        self.dprt=dprt
        self.e_id=e_id
    def print_info(self):
        print("Employee details:",self.name,self.dprt,self.e_id)
obj = employee("Ajay","RTS",1001)
obj.print_info()

class rts(employee):
    pass
obj1 = rts("Arun","RTS",1003)
obj1.print_info()

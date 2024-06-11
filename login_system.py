
def registration():
    database = {}
    print("----------Welcom to Registration---------------")
    u_name=input("Enter the your username: ")
    age=int(input("Enter your age:"))
    u_pwd=input("Enter your password: ")
    database[u_name] = u_pwd
    while True:
        print("----------Welcome to Login-----------------------")
        l_name=input("Enter the your user name: ")
        l_pwd=input("Enter your user password: ")
        if l_name in database:
            if database[u_name]==l_pwd:
                print("Login successfull")
                break
            else:
                print("invalid username or password")
        else:
            print("user not found")
            break
registration()



 
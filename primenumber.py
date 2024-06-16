m=(int(input("Enter the message: ")))
flag=0
for i in range(2,(m//2)+1):
    if m%i==0:
        flag=1
        break
if flag==0:
    print("The message is prime number")
else:
    print("The message is not prime number") 

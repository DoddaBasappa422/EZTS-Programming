
n=int(input("enter the number:\n"))
temp=n
m=n
r=0
c=0
while n!=0:
    n=n//10
    c=c+1
print(c)
while temp!=0:
    rem=temp%10
    p=pow(rem,c)
    r=r+p
    temp=temp//10   
print(r)
if m==r:
    print("Amstrong number")
else:
    print("Not A Amstrong number")



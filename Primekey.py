def check_prime(m):  #function to find prime number
    flag=0
    if m<1:
        flag=1
    elif m==1:
        flag=0
    else:
        for i in range(2,(m//2)+1):
            if m%i==0:
                flag=1
                break
    if flag==0:
        return 1 # prime number
    else:
        return 0 #not a prime number
    
t=[] 
n=int(input("Enter the number : "))   #input the number
p=n+1
flag=0
while flag<1:
    flag=check_prime(p)
    if flag==1:
        t.append(p)
    else:
        p=p+1 

sum=0
for i in range(n+1,p):
    sum+=i
t.append(sum)


p1=p
flag=0
p=p1+1
while flag<1:
    flag=check_prime(p)
    if flag==1:
        p2=p
    else:
        p+=1 

        
p=p1*p2
flag=check_prime(p)
if flag ==0:
    t.append(False)
else:
    t.append(True)
Prime_key=tuple(t)
print(Prime_key)


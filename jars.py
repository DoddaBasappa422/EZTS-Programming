def Choco(c,N):
    A=0
    count=0
    for jar in c:
        count=jar//3
        rem=jar%3
        A+=count
        if rem>0:
            A+=1
    return A



N=int(input("Enter the number of jars:"))
c=[]
for i in range(N):
    ch=int(input("Enter the number of chocolates in Jar : "))
    c.append(ch)
print(Choco(c,N))


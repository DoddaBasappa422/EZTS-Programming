c=10
p=6
s=int(input("Enter the place of starting person: "))
L=(c+s-1)%p
if L==0:
    L=p
print(L)
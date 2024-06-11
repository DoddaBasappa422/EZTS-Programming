list=[2,1,0,1,1,2,0,0]
c=0
c1=0
c2=0
for i in range(len(list)):
    if list[i]==0:
        c=c+1
    elif list[i]==1:
        c1=c1+1
    else:
        c2=c2+1
print(c,c1,c2)
j=0
while c>0:
    list[j]=0
    j=j+1
    c-=1
while c1>0:
    list[j]=1
    j=j+1
    c1-=1
while c2>0:
    list[j]=2
    j=j+1
    c2-=1
print(list)
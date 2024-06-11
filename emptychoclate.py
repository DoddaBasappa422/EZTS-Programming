'''list=['4','5','0','1','9','0','5','0']
list1=[]
list2=[]
for i in range(len(list)):
    if list[i]=='0':
        list1[i]=list[i]
    else:
        list2[i]=list[i]
for i in range(len(list)):
    list[i]=list1[i]+list2[i]
print(list)'''
list=[4,5,0,1,9,0,5,0]
i=0
j=0
n=len(list)
for i in range(0,n):
    if list[i]!=0:
        list[j]=list[i]
        j=j+1
while j<n:
    list[j]=0
    j=j+1
print(list)

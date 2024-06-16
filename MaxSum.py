'''given an integer array . your task is to 
find the 3 continious digits which gives you the maximum sum where k is entered by user
 sample input:
[2,4,3,5,6,3,4,6,7,1,2,5] 

output: [4,6,7]'''


si = [2,4,3,5,6,3,4,6,7,1,2,5]
'''l=len(si)
k=int(input("Enter the number of terms : "))
sum=0
maxsum=0
for i in range(0,l-k-1):
    sum=0
    for j in range(0,k):
        sum=sum+si[i+j]
    print(sum)        
    if sum>maxsum:
        maxsum=sum
        pos=i
print(maxsum)'''


l=[2,4,3,5,6,3,4,6,7,9,9,9]
window = max = 0
k = int(input("Enter the no of continious digit: "))

for j in range(0,k):
        window+=l[j]
l.append(0)
for i in range(0,len(l)-k):
    if max<window:
        max=window
        pos=i
    window = window+l[i+k]-l[i]

print("result")
print(max)
for j in range(0,k):
    print(l[pos+j])

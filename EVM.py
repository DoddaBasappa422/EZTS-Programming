evm=[]
count = [0]*5
for i in range(5):
    evm.append(int(input("Enter the vote:")))
print(evm)
for i in evm:
    count[i-1] =count[i-1]+1
print(count)
winner= count.index(max(count))
a=evm[winner]
print(f"The winner is: {a}")
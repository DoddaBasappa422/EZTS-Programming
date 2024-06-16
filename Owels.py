'''f={}
a,e,i,o,u=0,0,0,0,0
dict={'a':a,'e':e,'i':i,'o':o,'u':u}
v='aeiou'
for i in range(5):
    n=input("Enter the name of speaker: ")
    s=input("Enter the sentence :")
    f[n]=s
    for i in s:
        if i in v:
            match(i):
                case 'a':dict['a']+=1 
                case 'e':dict['e']+=1
                case 'i':dict['i']+=1
                case 'o':dict['o']+=1
                case 'u':dict['u']+=1
    max=0
    item=' '
    for i in dict:
        if dict[i]>=max:
            max=dict[i]
            item=i
    m={}
    m[n]=item 
    print(f)
    print(m)'''

def count_vowel(S):
    dic = {'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in S:
        if i == 'a' or i == 'A':
            dic['A'] += 1
        elif i == 'e' or i == 'E':
            dic['E'] += 1
        elif i == 'i' or i == 'I':
            dic['I'] += 1
        elif i == 'o' or i == 'O':
            dic['O'] += 1
        elif i == 'u' or i == 'U':
            dic['U'] += 1
    
    x=max(dic.values())
    result =[]
    for i,j in dic.items():
        if j == x:
            result.append(i)
    
    return result



i_p = [
    ["Alex", "I enjoy hiking in the mountains."],
    ["Sam", "A lovely sunny day at the beach."],
    ["Jamie", "Reading a book is my favorite pastime."],
    ["Taylor", "I love playing video games on weekends."],
    ["Chris", "Exploring new cities is exciting and fun."]
]

o_p = {}

for i in i_p:
    o_p[i[0]]= count_vowel(i[1])

print(o_p)
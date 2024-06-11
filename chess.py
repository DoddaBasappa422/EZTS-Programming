'''r = 8
c = 8
for i in range(r):
    for j in range(c):
        if (i+j)%2==0:
            print("false",end=' ')
        else:
            print("true",end=' ')
    print()'''
e_r="2468"
o_r="1357"
e_c="bdfh"
o_c="aceg"
s=input("Enter the co-ordinates: ")
if s[0] in e_c:
    if s[1] in e_r:
        print("black")
    else:
        print("white")
else:
    if s[1] in e_r:
        print("white")
    else:
        print("black")
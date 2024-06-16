import os
  
with open("file.txt",'w') as f:
    f.write("Dodda Basappa\n")
    f.write("3BR21CS038\n")
with open("file.txt",'a') as f:
    f.write("I am sportsman\n")
with open("file.txt",'r') as f:
    s=f.read()
    print(s)
s=s.replace("3BR21CS038","I am singer\n")
with open("file.txt",'a') as f:
    f.write(s)
with open("file.txt",'r+b') as f:
    print(f.tell())
    f.seek(-35,2)
    print(f.tell())
    f.write(b"#")
    print(f.read().decode('utf-8'))
    f.close()
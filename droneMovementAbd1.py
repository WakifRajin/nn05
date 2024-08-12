def xyz(string):
    num=[]
    for char in string:
        if char.isnumeric():
            num.append(int(char))
    return num

x1=y1=z1=0
ini_pos=input("Enter the Initial position: ")
x1,y1,z1=xyz(ini_pos)

n=int(input("Enter total number of movements: "))
cmd=[]

for i in range(n):
    cmds=input()
    cmd.append(cmds)

for char in cmd:
    x2,y2,z2=xyz(char)
    x1+=x2
    y1+=y2
    z1+=z2

print(f"Final position: {x1}i+{y1}j+{z1}k")
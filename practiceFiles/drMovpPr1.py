x = 0
y = 0

n = int(input("Number of movements: "))
cmds = []

for i in range (n):
    cmd = input()
    cmds.append(cmd)

#print(cmds)

for elem in cmds:
    command =  elem.split(" ")
    dir = command[0]
    dist = int(command[1])
    
    if dir in ["F", "f", "w", "W"]:
        y += dist
    elif dir in ["B", "b", "s", "S"]:
        y -= dist
    elif dir in ["R", "r", "d", "D"]:
        x += dist
    elif dir in ["L", "l", "a", "A"]:
        x -= dist
    
print(x,y)
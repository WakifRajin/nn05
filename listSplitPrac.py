x=y=0

cmds = []
n = int(input())
for i in range (n):
    cmd = input()
    cmds.append(cmd)

print(cmds)

for elem in cmds:
    cmdList = elem.split(" ")
    dir, dist = cmdList[0], int(cmdList[1])

    if dir == "F":
        y += dist
    elif dir == "B":
        y -= dist
    elif dir == "R":
        x += dist
    elif dir == "L":
        x -= dist

print(x, y)
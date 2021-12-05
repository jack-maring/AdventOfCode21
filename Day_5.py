lines=open('Inputs/Day_5.txt', 'r').read().split('\n')
newLines=[]

maxX=0
maxY=0
for i, a in enumerate(lines):
    newLines.append([])
    newLines[-1].append(int(a[:a.index(",")]))
    if newLines[-1][-1]>maxX:
        maxX=newLines[-1][-1]
    newLines[-1].append(int(a[a.index(",")+1:a.index(" ")]))
    if newLines[-1][-1]>maxY:
        maxY=newLines[-1][-1]
    a=a[a.index(">")+2:]
    newLines[-1].append(int(a[:a.index(",")]))
    if newLines[-1][-1]>maxX:
        maxX=newLines[-1][-1]
    newLines[-1].append(int(a[a.index(",")+1:]))
    if newLines[-1][-1]>maxY:
        maxY=newLines[-1][-1]

lines=newLines
grid=[[0 for j in range(maxX+1)] for i in range(maxY+1)]

for i, a in enumerate(lines):
    if a[0]==a[2]:
        for j in range(min(a[1], a[3]), max(a[1], a[3])+1):
            grid[j][a[0]]+=1
    elif a[1]==a[3]:
        for j in range(min(a[0], a[2]), max(a[0],a[2])+1):
            grid[a[1]][j]+=1

    #For part 1 just comment this else block out
    else:
        x1=a[0]
        y1=a[1]
        x2=a[2]
        y2=a[3]
        grid[y1][x1]+=1

        if y1>y2 and x1>x2:
            curPos=[x2, y2]
            while curPos!=[x1, y1]:
                grid[curPos[1]][curPos[0]]+=1
                curPos[0]+=1
                curPos[1]+=1

        elif y1>y2 and x1<x2:
            curPos=[x2, y2]
            while curPos!=[x1, y1]:
                grid[curPos[1]][curPos[0]]+=1
                curPos[0]-=1
                curPos[1]+=1

        elif y1<y2 and x1<x2:
            curPos = [x2, y2]
            while curPos != [x1, y1]:
                grid[curPos[1]][curPos[0]] += 1
                curPos[0] -= 1
                curPos[1] -= 1

        elif y1<y2 and x1>x2:
            curPos=[x2, y2]
            while curPos!=[x1, y1]:
                grid[curPos[1]][curPos[0]]+=1
                curPos[0]+=1
                curPos[1]-=1

count=0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j]>1:
            count+=1

print(count)
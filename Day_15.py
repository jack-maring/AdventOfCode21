#Note: This is **NOT** optimized enough for part two, it takes close to 5 minutes to get an answer for it, but it will eventually work
lines = open("Inputs/Day_15.txt", "r").read().split("\n")

newLines=[]
for line in lines:
    newLines.append([int(i) for i in line])

lines=newLines
orig=lines.copy()

#Copy these two for loops and width out for part 1
for i in range(1,5):
    lines+=[[k+i if k+i<=9 else k+i-9 for k in j] for j in orig]

width=len(lines[0])

for i in range(len(lines)):
    for j in range(1,5):
        lines[i]+=[k+j if k+j<=9 else k+j-9 for k in lines[i][:width]]

risks=[[float("inf") for i in range(len(lines[0]))] for j in range(len(lines))]
risks[0][0]=0

def getNeighbors(l, i, j):
    res=[]
    if i>0:
        res.append([i-1, j])
    if j>0:
        res.append([i, j-1])
    if i<len(l)-1:
        res.append([i+1, j])
    if j<len(l[0])-1:
        res.append([i, j+1])

    return res

q=[[0, 0]]

while len(q)>0:
    x, y = q.pop(0)
    nebs=getNeighbors(lines, x, y)
    for n in nebs:
        i, j=n

        myRisk=risks[x][y]
        if myRisk+lines[i][j]<risks[i][j]:
            risks[i][j]=myRisk+lines[i][j]
            if not (n in q):
                q.append(n)

print(risks[-1][-1])
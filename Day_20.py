#Note: not very efficient but not unbearable, takes about 30 seconds for part 2
def printGrid(grid):
    for g in grid:
        print(g)

def convert(token):
    binary=""
    for t in token:
        binary+="1" if t=="#" else "0"

    count=0

    for i in range(len(binary)-1, -1, -1):
        count+=(2**(len(binary)-1-i))*int(binary[i])

    return count

lines=open("Inputs/Day_20.txt", "r").read().split("\n")

space=lines.index("")
alg=""

for i in lines[:space]:
    alg+=i

newLines=[]
for i in lines[space+1:]:
    newLine=["." for q in range(150)]
    for j in i:
        newLine.append(j)
    newLine+=["." for q in range(150)]
    newLines.append(newLine)
lines=newLines

newLines=[["." for i in range(len(lines[0]))] for j in range(150)] + lines + [["." for i in range(len(lines[0]))] for j in range(150)]
lines=newLines

for _ in range(50): #Change to 2 for part 1
    res = [["." for i in range(len(lines[0]))] for j in range(len(lines))]
    for i in range(1, len(res)-1):
        for j in range(1, len(res[i])-1):
            token=""
            for q in range(-1, 2):
                for k in range(-1, 2):
                    token+=lines[i+q][j+k]

            index=convert(token)
            res[i][j]=alg[index]

    lines=res

count=0

for i in range(40, len(res)-80):
    for j in range(20, len(res[i])-80):
        if res[i][j]=="#":
            count+=1

print(count)







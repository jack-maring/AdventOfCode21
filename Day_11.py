#Make data
def makeData():
    lines=open("Inputs/Day_11.txt", "r").read().split("\n")
    newLines=[[int(j) for j in lines[i]] for i in range(len(lines))]
    return newLines

#Main solve
def solve(lines):
    #count=0 Use this for pat1
    step=0
    while True:
        for j in range(len(lines)):
            for k in range(len(lines[j])):
                lines[j][k]+=1

        lines, temp=raiseAllNines(lines)
        #count+=temp Use this for part 1 and ignore bellow parts
        flag=True
        for i in lines:
            for j in i:
                if j!=0:
                    flag=False
                    break

        if flag:
            return step+1

        step+=1

def raiseAllNines(lines, flashed=[]):
    nines=[]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]>9 and not([i,j] in flashed):
                nines.append([i,j])

    #print(nines)
    count=len(nines)

    for k in nines:
        if k[0]>0: #Up
            lines[k[0]-1][k[1]]+=1
        if k[0]>0 and k[1]<len(lines[0])-1: #Up-right
            lines[k[0]-1][k[1]+1]+=1
        if k[1]<len(lines[0])-1: #Right
            lines[k[0]][k[1]+1] += 1
        if k[0]<len(lines)-1 and k[1] < len(lines[0]) - 1: #Down-right
            lines[k[0]+1][k[1] + 1] += 1
        if k[0]<len(lines)-1: #Down
            lines[k[0]+1][k[1]] += 1
        if k[0]<len(lines)-1 and k[1]>0: #Down-left
            lines[k[0]+1][k[1]-1] += 1
        if k[1]>0: #Left
            lines[k[0]][k[1]-1] += 1
        if k[0]>0 and k[1]>0: #Up-Left
            lines[k[0]-1][k[1]-1] += 1

    if len(nines)==0:
        for k in flashed:
            lines[k[0]][k[1]]=0
        return lines, count

    lines, temp=raiseAllNines(lines, nines+flashed)
    return lines, temp+count


#Calculate and display answer
def display(ans):
    print(ans)

#Main function
def main():
    lines=makeData()
    ans=solve(lines)
    display(ans)

main()
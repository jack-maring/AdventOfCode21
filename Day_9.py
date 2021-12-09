#Make data
def makeData():
    lines=open("Inputs/Day_9.txt", "r").read().split("\n")
    newLines=[]
    for i in range(len(lines)):
        newLines.append([])
        for j in range(len(lines[i])):
            newLines[-1].append(int(lines[i][j]))

    return newLines


#Main solve
def getLows(lines):

    lows=[]
    for i in range(1,len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if lines[i][j]<lines[i-1][j] and lines[i][j]<lines[i+1][j] and lines[i][j]<lines[i][j-1] and lines[i][j]<lines[i][j+1]:
                lows.append([i,j])

    for i in range(1,len(lines)-1):
        if lines[i][0]<lines[i-1][0] and lines[i][0]<lines[i+1][0] and lines[i][0]<lines[i][1]:
            lows.append([i,0])
        if lines[i][-1]<lines[i-1][-1] and lines[i][-1]<lines[i+1][-1] and lines[i][-1]<lines[i][-2]: #It took me 40 minutes to do part 1 today and 25+ of those minutes were spent trying to fix a bug caused by this being elif instead of if :((((((
            lows.append([i,-1])

    for i in range(1,len(lines[0])-1):
        if lines[0][i]<lines[0][i-1] and lines[0][i]<lines[0][i+1] and lines[0][i]<lines[1][i]:
            lows.append([0, i])
        if lines[-1][i]<lines[-1][i-1] and lines[-1][i]<lines[-1][i+1] and lines[-1][i]<lines[-2][i]:
            lows.append([-1,i])

    if lines[0][0]<lines[0][1] and lines[0][0]<lines[1][0]:
        lows.append([0,0])
    if lines[-1][0]<lines[-1][1] and lines[-1][0]<lines[-2][0]:
        lows.append([-1,0])
    if lines[-1][-1]<lines[-1][-2] and lines[-1][-1]<lines[-2][-1]:
        lows.append([-1,-1])
    if lines[0][-1]<lines[1][-1] and lines[0][-1]<lines[0][-2]:
        lows.append([0,-1])

    return getBasins(lows, lines) # For part 1 just return lows

def getBasins(lows, lines):
    basins=[]
    for i in lows:
        if i[0]==-1:
            i[0]=len(lines)-1
        if i[1]==-1:
            i[1]=len(lines[0])-1
        lastBasins = [-1]
        basins.append([i])
        while lastBasins!=basins:
            for cord in basins[-1]:
                nebs=[]

                if cord[0]>0 and lines[cord[0]-1][cord[1]]>lines[i[0]][i[1]] and lines[cord[0]-1][cord[1]]!=9:
                    nebs.append([cord[0]-1,cord[1]])
                if cord[0]<len(lines)-1 and lines[cord[0]+1][cord[1]]>lines[i[0]][i[1]] and lines[cord[0]+1][cord[1]]!=9:
                    nebs.append([cord[0]+1,cord[1]])
                if cord[1]>0 and lines[cord[0]][cord[1]-1]>lines[i[0]][i[1]] and lines[cord[0]][cord[1]-1]!=9:
                    nebs.append([cord[0],cord[1]-1])
                if cord[1]<len(lines[0])-1 and lines[cord[0]][cord[1]+1]>lines[i[0]][i[1]] and lines[cord[0]][cord[1]+1]!=9:
                    nebs.append([cord[0],cord[1]+1])
                for j in nebs:
                    if not(j in basins[-1]):
                        basins[-1].append(j)

                lastBasins=basins
    return basins

#Calculate and display answer
def display(ans, lines):
    #For part 1 change this to display len(ans) + lines indexed at every value in ans
    sizes=[]
    for i in ans:
        sizes.append(len(i))

    count=1
    for i in range(3):
        count*=max(sizes)
        sizes.pop(sizes.index(max(sizes)))

    print(count)

#Main function
def main():
    lines=makeData()
    ans=getLows(lines)
    display(ans, lines)

main()
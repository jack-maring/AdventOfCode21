lines=open("Inputs/Day_13.txt", "r").read().split("\n")

i=0
cords=[]
while lines[i]!="":
    cords.append([int(lines[i][:lines[i].index(",")]),int(lines[i][lines[i].index(",")+1:])])

    i+=1
i+=1
folds=[]
while i<len(lines):
    folds.append(lines[i][lines[i].index("=")-1]+lines[i][lines[i].index("=")+1:])
    i+=1

for i in folds:
    if i[0]=="y":
        val=int(i[1:])
        remove = []
        for cord in cords:
            if cord[1]>val:
                if [cord[0], val-(cord[1]-val)] in cords:
                    remove.append(cord)
                else:
                    cord[1]=val-(cord[1]-val)

    else:
        val=int(i[1:])
        remove=[]
        for cord in cords:
            if cord[0]>val:
                if [val-(cord[0]-val), cord[1]] in cords:
                    remove.append(cord)
                else:
                    cord[0]=val-(cord[0]-val)

    for r in remove:
        cords.remove(r)

#For part 1 delete all of this and just print(len(cords))
grid=[["." for i in range(40)] for j in range(6)]

for cord in cords:
    grid[cord[1]][cord[0]]="#"

for g in grid:
    print(g)




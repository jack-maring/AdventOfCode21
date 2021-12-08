#Make data
def makeData():
    lines=open("Inputs/Day_8.txt", "r").read().split("\n")

    return lines


#Main solve
def solve(lines):
    counts=[]

    for i in range(len(lines)):
        config=lines[i][:lines[i].index("|")-1].split(" ")
        outer=lines[i][lines[i].index("|")+2:].split(" ")
        sixOrNine=[]
        others=[]

        for j in config:
            if len(j)==2:
                one=j

            elif len(j)==3:
                seven=j

            elif len(j)==4:
                four=j

            elif len(j)==7:
                eight=j

            elif len(j)==6:
                sixOrNine.append(j)

            elif len(j)==5:
                others.append(j)

        map=[[] for j in range(7)]

        for j in one:
            map[2].append(j)
            map[6].append(j)

        for j in seven:
            if not(j in one):
                map[1].append(j)

        for j in four:
            if not(j in one):
                map[0].append(j)
                map[3].append(j)

        for j in eight:
            if not(j in four) and not(j in seven):
                map[4].append(j)
                map[5].append(j)

        #print(map)
        #flag=False
        for j in sixOrNine:
            if map[2][0] in j and not(map[2][1] in j):
                map[6]=[map[2][0]]
                map[2]=[map[2][1]]
                break

            elif not(map[2][0] in j) and map[2][1] in j:
                temp=map[2][1]
                map[2] = [map[2][0]]
                map[6] = [temp]
                break


        for j in others:
            flag=True
            for q in seven:
                if not(q in j):
                    flag=False
                    break

            if flag:
                if map[5][0] in j:
                    map[4] = [map[5][1]]
                    map[5] = [map[5][0]]
                else:
                    map[4] = [map[5][0]]
                    map[5] = [map[5][1]]

        for j in others:
            flag=True
            for q in seven:
                if not(q in j):
                    flag=False
                    break

            if flag:
                for q in four:
                    if not(q in j):
                        map[0]=[q]
                        break

        if map[0][0]==map[3][0]:
            map[3]= [map[3][1]]
        else:
            map[3] = [map[3][0]]
        #print(map)
        newMap=[j[0] for j in map]
        map=newMap
        count=""
        for j in outer:
            count+=translate(map, j)

        counts.append(count)

    return counts

def translate(key, code):
    try:
        myVal=["1110111","0010001","0111110","0111011","1011001","1101011","1101111","0110001","1111111","1111011"]
        curr=""
        for i in key:
            if i in code:
                curr+="1"
            else:
                curr+="0"

        return str(myVal.index(curr))

    except:
        print(key, code)



#Calculate and display answer
def display(ans):
    tot=0
    for count in ans:
        tot+=int(count)

    print(tot)


#Main function
def main():
    lines=makeData()
    #print(lines)
    ans=solve(lines)
    display(ans)

main()
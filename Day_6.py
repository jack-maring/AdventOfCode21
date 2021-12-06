#Make data
def makeData():
    lines=open("Inputs/Day_6.txt", "r").read().split(",")
    data={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,}
    for i in range(len(lines)):
        data[int(lines[i])]+=1

    return data


#Main solve
def solve(data):

    for i in range(80): #change to range(80) for part 1
        temp=data[1]
        for j in range(2,9):
            data[j-1]=data[j]

        data[6]+=data[0]
        data[8]=data[0]
        data[0]=temp

    return data


#Calculate and display answer
def display(data):
    count=0

    for key in data:
        count+=data[key]

    print(count)

    return -1


#Main function
def main():
    lines=makeData()
    ans=solve(lines)
    display(ans)

main()
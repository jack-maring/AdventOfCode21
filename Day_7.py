#Make data
def makeData():
    lines=open("Inputs/Day_7.txt", "r").read().split(",")
    lines=[int(i) for i in lines]

    return lines


#Main solve
def solve(lines):
    highest=max(lines)
    best=float("inf")

    for i in range(highest):
        count=0
        for j in range(len(lines)):
            count+=abs(lines[j]-i)*(abs(lines[j]-i)+1)/2 #For part 1 just make it abs(lines[j]-i)

        if count<best:
            best=count

    return best


#Calculate and display answer
def display(ans):
    print(ans)
    return -1


#Main function
def main():
    lines=makeData()
    ans=solve(lines)
    display(ans)

main()
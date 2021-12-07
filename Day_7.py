memo={} #After further testing memoization isn't really necessary here but the program didn't give me output instantly and I got scared

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
            count+=sumAllLess(abs(lines[j]-i)) #For part 1 just get rid of the sumAllLess() part and make it just lines[j]-i

        if count<best:
            best=count

    return best


def sumAllLess(n):
    if n in memo:
        return memo[n]

    count=0

    for i in range(n+1):
        count+=i

    memo[n]=count
    return count


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
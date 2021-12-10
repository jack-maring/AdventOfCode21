lines=open("Inputs/Day_10.txt", "r").read().split("\n")

stack=[]
converter={")":3, "]":57, "}":1197, ">":25137}
count=0

def convert(close):
    key={"(":")", "[":"]","{":"}","<":">"}
    out=""
    for i in range(len(close)-1, -1, -1):
        out+=key[close[i]]
    return out

def score(close):
    tot=0
    key = {")":1, "]":2, "}":3, ">":4}
    for i in close:
        tot*=5
        tot+=key[i]

    return tot


newLines=lines.copy()
#count=0
for i in lines:
    stack = []
    for j in i:
        if j=="(" or j=="[" or j=="{" or j=="<":
            stack.append(j)
        elif j==")":
            if stack.pop()!="(":
                newLines.remove(i) # For part 1 change all of these to count+=converter[j]
                break
        elif j=="]":
            if stack.pop()!="[":
                newLines.remove(i)
                break
        elif j=="}":
            if stack.pop()!="{":
                newLines.remove(i)
                break
        elif j==">":
            if stack.pop()!="<":
                newLines.remove(i)
                break

lines=newLines
#print(count)

#For part 1 comment out everything below here
scores=[]
for i in lines:
    stack=[]
    for j in i:
        if j == "(" or j == "[" or j == "{" or j == "<":
            stack.append(j)
        else:
            stack.pop()

    scores.append(score(convert(stack)))

scores.sort()
print(scores[int(len(scores)/2)])


#Part 1 and part 2 are completely different for this one so im just leaving in part 2 here

lines=["-2"]

while lines[-1]!=["-1"]:
    #print(lines)
    lines.append(input().split())

lines.pop(0)
lines.pop(-1)

nums=lines.pop(0)[0].split(",")
#print(nums)

newLines=[]
for i in range(len(lines)):
    if lines[i]!=[]:
        newLines.append(lines[i])

lines=newLines
orig=lines.copy()

res=-1

def func():
    global lines
    global orig
    lastPopped=[]
    toPop=[]
    for j, b in enumerate(nums):
        #print(lines)
        if len(lines)==0:
            return lastPopped, lastPoppedCall

        lastCall=b
        for i, a in enumerate(lines):
            if b in a:
                lines[i]=[a[i] if a[i]!=b else "-1" for i in range(len(a))]

        for i in range(0, len(lines), 5):
            if lines[i].count("-1")==5 or lines[i+1].count("-1")==5 or lines[i+2].count("-1")==5 or lines[i+3].count("-1")==5 or lines[i+4].count("-1")==5:
                toPop.append(i)
            for k in range(len(lines[i])):
                if not(i in toPop) and lines[i][k]=="-1" and lines[i+1][k]=="-1" and lines[i+2][k]=="-1" and lines[i+3][k]=="-1" and lines[i+4][k]=="-1":
                    toPop.append(i)

        #print(toPop, b)
        #lastPopped=[lines[i] for i in range(toPop, toPop+5)]
        for i, a in enumerate(toPop):
            a-=5*i
            lastPopped = [lines[j] for j in range(toPop[i]-5*i, toPop[i] + 5-5*i)]
            for q in range(5):
                lines.pop(a)
                if len(orig)>5:
                    orig.pop(a)

            lastPoppedCall=lastCall

        #print(orig)

        toPop=[]

    #print("hello")
    return lastPoped, lastPoppedCall

# winStart, lastCall=func()
# count=0
# for i in range(winStart, winStart+5):
#     print(lines[i])
#     for j in range(len(lines[i])):
#         if lines[i][j]!="-1":
#             count+=int(orig[i][j])
#             print(orig[i][j])
#
# print(count)
# print(count*int(lastCall))

lines, lastCall=func()
#print(orig)
#print(lines)
count=0
for i in range(len(lines)):
    #print(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j]!="-1":
            count+=int(orig[i][j])
           #print(orig[i][j])

print(count, lastCall)
print(count*int(lastCall))


lines=["-2"]

while lines[-1]!="-1":
    lines.append(input())

lines.pop(0)
lines.pop(-1)

# -------------PART 1-------------
# ep=""
# gamma=""
# ones=[0 for i in range(12)]
#
# for i, a in enumerate(lines):
#     for j in range(len(a)):
#         if a[j]=="1":
#             ones[j]+=1
#
# for i, a in enumerate(ones):
#     if a/len(lines)<0.5:
#         gamma+="0"
#         ep+="1"
#     else:
#         gamma+="1"
#         ep+="0"
#
def convert(s):
    out=0
    for i in range(len(s)):
        out+=2**i*int(s[len(s)-1-i])

    return out
#
# print(convert(gamma)*convert(ep))

# -------------PART 2-------------
k=0
while len(lines)>1:
    oneCount=0
    for i, a in enumerate(lines):
        if a[k]=="1":
            oneCount+=1

    newLines=[]
    if oneCount/len(lines)>=0.5:
        for i, a in enumerate(lines):
            if a[k]=="1":
                newLines.append(a)
    else:
        for i, a in enumerate(lines):
            if a[k]=="0":
                newLines.append(a)

    k+=1

    lines=newLines

print(convert(lines[0]))


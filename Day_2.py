# -----------------PART 1-------------------
# lines=["-2"]
#
# while lines[-1]!="-1":
#     lines.append(input())
#
# lines=lines[1:len(lines)-1]
#
# hor=0
# depth=0
#
# for i, a in enumerate(lines):
#     #print(a)
#     command=a[:a.index(" ")]
#     num=int(a[a.index(" ")+1:])
#     if command=="forward":
#         hor+=num
#
#     elif command=="up":
#         depth-=num
#
#     else:
#         depth+=num
#
# print(hor*depth)

#-----------------PART 2-------------------
lines=["-2"]

while lines[-1]!="-1":
    lines.append(input())

lines=lines[1:len(lines)-1]

hor=0
depth=0
aim=0

for i, a in enumerate(lines):
    #print(a)
    command=a[:a.index(" ")]
    num=int(a[a.index(" ")+1:])
    if command=="forward":
        hor+=num
        depth+=aim*num

    elif command=="up":
        aim-=num

    else:
        aim+=num

print(hor*depth)
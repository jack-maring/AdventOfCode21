# -----------------PART 1-------------------
# lines=open('Inputs/Day_2.txt', 'r').read().split('\n')
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
lines=open('Inputs/Day_2.txt', 'r').read().split('\n')

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
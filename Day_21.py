#Brute forcing part 2 does not work

lines=open("Inputs/Day_21.txt", "r").read().split("\n")

starts=[int(lines[0][lines[0].index(":")+2:]), int(lines[1][lines[1].index(":")+2:])]
pos=[starts[0],starts[1]]
scores=[0,0]
die=1
player=0
rolls=0

while max(scores)<1000:
    rolls+=3
    for i in range(3):
        pos[player]+=die
        die+=1

        if die>100:
            die=1

        if pos[player]>10:
            pos[player]=pos[player]%10 if pos[player]%10!=0 else 10

    scores[player]+=pos[player]
    player=1 if player==0 else 0

print(min(scores)*rolls)


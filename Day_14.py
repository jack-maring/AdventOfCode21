lines=open("Inputs/Day_14.txt", "r").read().split("\n")

pairs={}
for i in range(1, len(lines[0])):
    pairs[lines[0][i - 1:i + 1]] = pairs[lines[0][i - 1:i + 1]]+1 if lines[0][i-1:i+1] in pairs else 1

inserts={}
for i in range(2, len(lines)):
    inserts[lines[i][:2]]=lines[i][6:]

counts={}
for i in lines[0]:
    counts[i]=counts[i]+1 if i in counts else 1

for i in range(40): #Change to 10 for part 1
    newPairs={}
    for key in inserts:
        if key in pairs:
            counts[inserts[key]] = counts[inserts[key]] +pairs[key] if inserts[key] in counts else pairs[key]
            newPairs[key[0] + inserts[key]] = newPairs[key[0] + inserts[key]]+ pairs[key] if key[0] + inserts[key] in newPairs else pairs[key]
            newPairs[inserts[key]+key[1]] = newPairs[inserts[key]+key[1]] + pairs[key] if inserts[key]+key[1] in newPairs else pairs[key]

    pairs=newPairs

highest, lowest=float("-inf"), float("inf")
for key in counts:
    highest, lowest = max(highest, counts[key]), min(lowest, counts[key])

print(highest-lowest)
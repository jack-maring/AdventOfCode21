lines=open("Inputs/Day_12.txt", "r").read().split("\n")
nodes={}

for i in range(len(lines)):
    first = lines[i][:lines[i].index("-")]
    last = lines[i][lines[i].index("-")+1:]
    nodes[first] = nodes[first] + [last] if first in nodes else [last]
    nodes[last] = nodes[last] + [first] if last in nodes else [first]

def getPathsFromNode(curr, paths):
    tot=[]

    if curr=="end":
        return paths

    for neb in nodes[curr]:
        if neb!="start":
            for i in paths:
                if not(neb in i) or neb!=neb.lower():
                    tot+=getPathsFromNode(neb, [i+[neb]])

                #Comment these two lines out for part 1
                elif i[0]==0:
                    tot+=getPathsFromNode(neb, [[1] + i[1:] + [neb]])

    return tot

print(len(getPathsFromNode("start", [[0, "start"]])))
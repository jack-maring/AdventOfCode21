lines = open("Inputs/Day_25.txt", "r").read().split("\n")
lines = [[i for i in j] for j in lines]

step = 0
movement = True

while movement:
    movement = False
    newLines = [[lines[i][j] for j in range(len(lines[i]))] for i in range(len(lines))]

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == ">":
                if j < len(lines[i]) - 1 and lines[i][j + 1] == ".":
                    newLines[i][j] = "."
                    newLines[i][j + 1] = ">"
                    movement = True
                elif j == len(lines[i]) - 1 and lines[i][0] == ".":
                    newLines[i][j] = "."
                    newLines[i][0] = ">"
                    movement = True
                else:
                    newLines[i][j] = ">"
    lines = newLines
    newLines = [[lines[i][j] for j in range(len(lines[i]))] for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "v":
                if i < len(lines) - 1 and lines[i + 1][j] == ".":
                    newLines[i][j] = "."
                    newLines[i + 1][j] = "v"
                    movement = True
                elif i == len(lines) - 1 and lines[0][j] == ".":
                    newLines[i][j] = "."
                    newLines[0][j] = "v"
                    movement = True
                else:
                    newLines[i][j] = "v"
    lines = newLines

    if movement:
        step += 1

print(step + 1)

xLow=int(input())
xHigh=int(input())
yLow=int(input())
yHigh=int(input())

def traj(xVel, yVel):
    xPos=0
    yPos=0
    hit=False

    while xPos<=xHigh and yPos>=yLow:
        xPos+=xVel
        yPos+=yVel

        if xVel!=0:
            xVel=xVel-1 if xVel>0 else xVel+1
        yVel-=1

        if xPos<=xHigh and xPos>=xLow and yPos<=yHigh and yPos>=yLow:
            return True

    return False

cap=500 #This is kind of a cheap way to do it but im to lazy to figure anything else out
count=0

for xVel in range(xHigh+1):
    for yVel in range(-1*cap, cap):
        if traj(xVel, yVel):
            count+=1

print(count)
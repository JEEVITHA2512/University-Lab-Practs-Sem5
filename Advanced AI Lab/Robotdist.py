import math
def distance(x,y,steps,direction):
    if direction== "UP":
        y+=steps
    elif direction == "DOWN":
        y-=steps
    elif direction == "LEFT":
        x-=steps
    elif direction == "RIGHT":
        x+=steps
    print(x,y)
    return math.sqrt(x**2+y**2)

if __name__=="__main__":
    x=0
    y=0
    print("Positions of x and y",x,y)
    steps=int(input("Enter the number of steps:"))
    direction=input("Enter the direction(UP,DOWN,LEFT,RIGHT):")
    print("New position of x and y are")
    distancetravelled=distance(x,y,steps,direction)
    print(distancetravelled)
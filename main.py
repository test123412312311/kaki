import math

FalseAlarm = False
RocketType = int(input("rocket type?: "))
X = float(input("X co?: "))
Y = float(input("Y co?: "))

if 1 <= RocketType <= 4:
    if 0 <= Y <= 20 and 0 <= X <= 20:
        if RocketType == 1:
            time = 30
        elif RocketType == 2:
            time = 60
        elif RocketType == 3:
            time = 120

        if Y < 10:
            if X <= 10:
                landingPos = "Open Area"
                FalseAlarm = True
            else:
                landingPos = "Area Two"
        else:
            if X <= 10:
                landingPos = "Area Three"
            else:
                landingPos = "Area One"

        if not FalseAlarm:
            print("The rocket was fired at " + landingPos + " everyone in the area have " + str(time) +
                  " seconds to get to the mamad")

            TargetHit = math.sqrt((0 - X) ** 2 + (0 - Y) ** 2) < 13
            if TargetHit:
                print("kipat barzel eliminated the threat")
            else:
                print("kipat barzel could not eliminate the threat")

        else:
            print("Azakat shav")

    else:
        print("your coordinates are kinda trash not gonna lie")

else:
    print("There is no such rocket u dumbass")

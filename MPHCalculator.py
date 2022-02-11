#Travel Calculator
#Zeke Amonoo
#The product Travel Calculator is meant to estimate the amount of time need to travel from destination to destination at an effecient rate of speed.
def TravelCalc():
    message = "Hello User, welcome to Travel Calculator, the most effecient product currently on the market!"
    print(message)
    print()
    speed = input(" Enter your speed in mph: ")
    speed = int(speed)
    distance = input("Enter your distance in miles: ")
    distance = float(distance)
    time = distance/speed
    print("At", speed, "mph, it will take", time, "hours to travel", distance, "miles.")
    input("\n\nPress the Enter key to exit")

TravelCalc()

#ISBN Identifier
#Zeke Amonoo
#The product ISBN Identifier is meant to verify the amount of time need to travel from destination to destination at an effecient rate of speed.
def isbn(number):
    try:
        numberreal = number
        numberzero = number.replace("-", "")
        number = number.replace("-", "")
        number = int(number)
        number = str(numberzero)
        print("The ISBN Number Entered is", numberreal)
        num = int(number[0]) * 10 + int(number[1]) * 9 + int(number[2]) * 8 + int(number[3]) * 7 + int(number[4]) * 6 + int(number[5]) * 5 + int(number[6]) * 4 + int(number[7]) * 3 + int(number[8]) * 2
        num = num%11
        checknum = 11 - num

        print("The checksum should be", checknum, "and the one in the code provided was", number[9])
        if int(checknum) == int(number[9]):
            print("The checksum provided is correct")
        else:
            print("The checksum provided is incorrect")
    except ValueError:
        print("Not valid number")
        error()
    except IndexError:
        print("Not a valid digit ISBN")
        error()



def error():
    print("Error")

running = True
while running == True:
    isbn(input("What is the 10 digit ISBN number? "))
    restart = input("Do you want to restart?")
    restart = restart.lower()
    if restart in ("yes", "y", "ok", "sure", ""):
        print("Restarting\n" + "-" * 34)
    else:
        print("closing Down")
        running = False

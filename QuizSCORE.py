#initialize the value of the user's response
#while the user's response starts with a Y
    #ask for a quiz score
    #if the quiz score is greater than oor equal to 6, print "passed"
    #in all other cases, print "better luck next time"
    #ask the user if they want to enter another score

userResponse = "YES"
while (userResponse[0] == "Y"):
    quizScore = float(input("Enter a quiz score: "))
    if (quizScore >= 6):
        print("You passed!")
    else:
        print("Better luck next time")
    userResponse = input("Do you want to enter another score? Y/N ")

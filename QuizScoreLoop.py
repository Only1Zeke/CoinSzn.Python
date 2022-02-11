#QuizScoreRecall
#Reads in 10 quiz scores and stores them in a list

quizscore= int(input("Enter a quiz score: "))
quizScoreList = []
quizScoreList.append(quizscore)
searchvalue=()
findHighestValue=()

count=0
while (count<10):
    quizscore= int(input("Enter a quiz score: "))
    quizScoreList.append(quizscore)
    count = count + 1

print("The list=", quizScoreList)

searchvalue=int(input("Enter a number to search for: "))

count=0
while (count<10):
    if (searchvalue==quizScoreList[count]):
       print("The value", searchvalue, "is in the list at index", count)
    count = count + 1

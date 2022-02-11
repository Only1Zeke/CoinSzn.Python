#This program stores personal contact information

nameList = []
numberList = []

name = input('Enter a name')
num = input('Enter the phone number')
nameList.append(name)
numberList.append(num)

name = input('Enter a name')
num = input('Enter the phone number')
nameList.append(name)
numberList.append(num)

name = input('Enter a name')
num = input('Enter the phone number')
nameList.append(name)
numberList.append(num)

position = 0
for name in nameList:
    print("The phone number for", name, "is", numberList[position])
    position = position + 1

print("Thanks for using this software")

#ISBN Identifier
#Zeke Amonoo
#The product ISBN Identifier is meant to verify the amount of time need to travel from destination to destination at an effecient rate of speed.

ISBN = int(input('Please enter a number for verification. Do not include spaces or dashes: ')

while len(ISBN)!= 10:

    print('Please make sure you have entered a number which is exactly 10 or 13 characters long.')
    print('The', ISBN , 'is NOT a valid digit ISBN')
    ISBN=int(input('Please re-enter the number: '))
    continue


else:

    Digit1=int(ISBN[0])*11
    Digit2=int(ISBN[1])*10
    Digit3=int(ISBN[2])*9
    Digit4=int(ISBN[3])*8
    Digit5=int(ISBN[4])*7
    Digit6=int(ISBN[5])*6
    Digit7=int(ISBN[6])*5
    Digit8=int(ISBN[7])*4
    Digit9=int(ISBN[8])*3
    Digit10=int(ISBN[9])*2
    Sum = int(number[0]) * 10 + int(number[1]) * 9 + int(number[2]) * 8 + int(number[3]) * 7 + int(number[4]) * 6 + int(number[5]) * 5 + int(number[6]) * 4 + int(number[7]) * 3 + int(number[8]) * 2
    Mod=Sum%11
    Digit11=11-Mod

    if Digit11==10:
       Digit11='X'
    ISBNNumber=str(ISBN)+str(Digit11)
    print('Your 11 digit ISBN Number is ' + ISBNNumber)

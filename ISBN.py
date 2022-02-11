#This program prints a libary book's ISBN number

ISBN=input('Please enter a number for verification. Do not include spaces or dashes: ')

while len(ISBN)!= 10:

    print('Please make sure you have entered a number which is exactly 10 or 13 characters long.')
    print('The', ISBN ,'is NOT a valid digit ISBN')
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
    Sum=(Digit1+Digit2+Digit3+Digit4+Digit5+Digit6+Digit7+Digit8+Digit9+Digit10)
    Mod=Sum%11
    checksum=11-Mod

    if checksum==10:
       checksum= Mod

    print("The checksum is", checksum)
    ISBNNumber=str(ISBN)
    print('Your 10 digit ISBN Number is ' + ISBNNumber)

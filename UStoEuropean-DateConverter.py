#date format

USDate = input("Enter a date in the format mm/dd/yyyy: ")
EuroDate = USDate[3]+USDate[4] + "/" + USDate[0]+ USDate[1] + "/" + USDate[6]+USDate[7]+USDate[8]+USDate[9]
print("The date in the format dd/mm/yyyy is: ",EuroDate)

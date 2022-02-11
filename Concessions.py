#This program calculates the total cost of concessions for a single
#Customer at a PTA fundrasier. Customers can purchase water, soda,
#candy bars, and bags of popcorn for $0.50, $0.75, $1.00, and $0.25

numWater=int(input("How many cases of water would you like to buy"))

numCandy=int(input("How many boxes of candy would you like to buy"))

numPopcorn=int(input("How many bags of popcorn would you like to buy"))

numSoda=int(input("How many boxes of soda would you like to buy"))

TotalCost=(numWater*0.5)+(numCandy*1.00)+(numPopcorn*.25)+(numSoda*.75)

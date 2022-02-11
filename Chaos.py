#This program prints a user's rating of chaotic behavior

print("This program illustrates chaotic behavior")

x = float(input("Selecting a number between 0 and 1 will determine your chaotic behavior"))

for i in range(10):
    x = 2.0 * x * (1-x)
    print(x)

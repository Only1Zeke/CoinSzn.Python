#This program prompts users to enter their favorite pizza toppings

prompt = "\nPlease enter favorite pizza toppings:"
prompt+= "\n(Enter 'quit' when you are finished.)"

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print("I'd love that pizza topping too" = pizza.title() + "!")

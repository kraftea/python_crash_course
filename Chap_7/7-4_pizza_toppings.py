prompt = "List what toppings you want on your pizza: "
prompt += "When you're done adding toppings, type 'quit.' "
toppings = ""

while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print("I'll add " + toppings + " to your pizza.")

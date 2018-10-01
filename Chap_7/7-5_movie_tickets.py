prompt = "\nTell me your age and I'll give you a ticket price:"
prompt += "\nType quit to exit the program "
age = ''
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        ticket = 'free'
    elif age < 13:
        ticket = '$10.00'
    else:
        ticket = '$15.00'
    print("Your ticket price is: " + ticket + ".")

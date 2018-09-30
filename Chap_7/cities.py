prompt = "\nPlease enter a name of a City you have visited: "
prompt += "\n(Type 'quit' to exit.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to visit " + city.title() + " too!")

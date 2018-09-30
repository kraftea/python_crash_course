prompt = "\nI will repeat what you say."
prompt += "\nEnd the program by typing 'quit.' "
active = True
while active:
        message = input(prompt)

        if message == 'quit':
            active = False
        else:
            print(message)

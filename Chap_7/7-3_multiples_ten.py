number = input("Give me a number and i'll tell you if it's a multiple" +
               " of ten. ")
number = int(number)

if number % 10 == 0:
    print("The number " + str(number) + " is a multiple of ten!")
else:
    print("The number " + str(number) + " is not a multiple of ten.")

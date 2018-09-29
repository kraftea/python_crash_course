pet_1 = {
    'pet': 'dog',
    'owner_first': 'jon',
    'owner_last': 'sano',
}
pet_2 = {
    'pet': 'cat',
    'owner_first': 'meg',
    'owner_last': 'smith',
}
pet_3 = {
    'pet': 'ferret',
    'owner_first': 'tony',
    'owner_last': 'balog',
}

pets = [pet_1, pet_2, pet_3]

print("Here is the information we have on all pets: ")
for pet in pets:
    print("\n\tPet type: " + pet['pet'].title())
    print("\tOwner full name: " + pet['owner_first'].title() +
          " " + pet['owner_last'].title())

person_1 = {
    'first_name': 'hulk',
    'last_name': 'hogan',
    'fav_hobby': 'drinking antifreeze',
}
person_2 = {
    'first_name': 'goro',
    'last_name': 'unkown',
    'fav_hobby': 'fatalities',
}
person_3 = {
    'first_name': 'Neo',
    'last_name': 'Anderson',
    'fav_hobby': 'dodging bullets',
}

people = [person_1, person_2, person_3]
print("The following characters will ruin your day: ")
for person in people:
    print("\n\tFirst Name: " + person['first_name'].title())
    print("\tLast Name: " + person['last_name'].title())
    print("\tFavorite Hobby: " + person['fav_hobby'])

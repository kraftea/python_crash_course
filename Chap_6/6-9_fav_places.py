favorite_places = {
    'brock': ['niagra', 'namibia', 'rome'],
    'angie': 'grand canyon',
    'jean': 'hell',
}

for name, places in favorite_places.items():
    if name == 'brock':
        print("\n" + name.title() + "'s favorite places are: ")
        for place in places:
            print("\t" + place.title())
    else:
        print("\n" + name.title() + "'s favorie place is: ")
        print("\t" + places.title())

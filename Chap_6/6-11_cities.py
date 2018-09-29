# store information about different cities
cities = {
    'miami': {
        'country': 'united states',
        'population': '453,579',
        'fact': 'Miami is the 76th most dangerous city in the U.S.',
    },
    'london': {
        'country': 'england',
        'population': '8,136,000',
        'fact': 'Police never caught Jack the Ripper',
    },
    'moscow': {
        'country': 'russia',
        'population': '11,920,000',
        'fact': 'Moscow has the largest number of billionaires in the world',
    },
}
# print each city and the information about them
for city, stats in cities.items():
    print("\nWe have the following information on the city of " +
          city.title() + ":")
    for info, details in stats.items():
        print("\t" + info + ": " + details)

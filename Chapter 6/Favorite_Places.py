favorite_places = {
    "JJ"  : ["Hawaii", "Portugal"],
    "KK"  : ["Boston", "Langley", "London"],
    "LL" : ["Berlin"]
}

for person, country_list in favorite_places.items():
    print(f'{person} likes to go to : ')
    for country in country_list:
        print(country)
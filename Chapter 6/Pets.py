Doggo = {
    "Name": "Doggo",
    "Kind" : "Dog",
    "Owner" : "Kolya"
}

Cato = {
    "Name": "Cato",
    "Kind" : "Cat",
    "Owner" : "Marie"
}

SarahJessicaPorker = {
    "Name": "SarahJessicaPorker",
    "Kind": "Horse",
    "Owner": "Gertrude"
}
snek = {
    "Name": "snek",
    "Kind": "Snake",
    "Owner": "Rudy"
}

invisiblePet = {
    "Name": "invisiblePet",
    "Kind" : "Cameleon",
    "Owner" : "Larry"
}

einstein = {
    "Name": "einstein",
    "Kind" : "Parrot",
    "Owner" : "Larissa"
}

pets = [Doggo, Cato, SarahJessicaPorker, snek, invisiblePet, einstein]

for animal in pets: 
    for key, value in animal.items():
        print(f'{key}, {value}')
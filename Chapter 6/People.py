jshmoe = {
    'First name' : "Joe",
    'Last name': "Shmoe",
    'age': "30",
    'city': "Los Angeles"
}

jkolya = {
    'First name': "John",
    "Last name": "Kolya",
    "age": "34",
    "city": "New Athos"
}

vbialek = {
    'First name': 'Victor',
    'Last name': 'Bialek',
    'age': '23.6',
    'city': 'Augsburg',
}

people = [vbialek, jkolya, jshmoe]

# print(people)

for person in people:
    for key, value in person.items() : 
        print(f'{key}, {value} \n')


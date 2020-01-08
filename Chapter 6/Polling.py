# Code from book: "favorite_languages.py"
# page 97

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
poll_needers = ['phil', 'sheila', 'margaret', 'sarah']
favorite_people = []
for person in favorite_languages.keys():
    favorite_people.append(person.lower())

print(favorite_people)

for person in poll_needers:
    if(person.lower() in favorite_people):
        print(f'{person.title()} thank you for having taken the poll.')
    else:
        print(f'{person.title()} please do take the poll.')


rivers = {
    'nile' : 'egypt',
    'tejo' : 'portugal',
    'thames' : 'england'
}
print("\n")

print("Rivers: \n")
for key, value in rivers.items():
    print("The " + key.title() + " runs through " + value.title() + "." )

print("\n")

print("River names: \n")
for key in rivers.keys():
    print(key.title())

print("\n")

print("Country names: \n")

for value in rivers.values():
    print(value.title())
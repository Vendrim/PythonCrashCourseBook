Glossary = {
    'list': 'A set of values.',
    'string': 'A cooler way of saying text',
    'dictionary': 'Its sort of like a map in Java, but better.',
    'argument': 'A parameter/variable from the outside (I guess)',
    'loop': 'A data flow control element, which goes through commands until a specific condition is fulfilled.',
    'integer': 'A number which is part of the natural family.',
    'double': 'Same as integer, but can also represent real numbers.',
    'float': 'Same as double, but takes less space. Is not as exact as double',
    'byte' : 'Like a integer, but very small. Stores small numbers. Was used in before times, when storage was a bit expensive.',
    'code convention' : 'A way of writing code.',
    'variable': 'A value, which may or may not change through out a program. A placeholder.'
}
print("Stuff I learned about.")

for key, value in Glossary.items():
    print(f'{key} : {value}')


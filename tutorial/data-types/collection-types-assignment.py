countries = ['India', 'USA', 'France']

countries.append('UK')
del countries[0]

countries.insert(1, 'China')
print(countries)


countries2 = {'India', 'USA', 'France'}

countries2.update(['UK'])
countries2.remove('USA')

# countries2.insert(1, 'China')
print(countries2)

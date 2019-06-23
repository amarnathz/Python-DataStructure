
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}
print(locations)

usa_sorted = sorted(locations['North America']['USA'])
print(usa_sorted)
for city in usa_sorted:
    print (city)

asia_cities=[]

for countries, cities in locations['Asia'].items():
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
print(asia_sorted)
for city in asia_sorted:
    print (city)    

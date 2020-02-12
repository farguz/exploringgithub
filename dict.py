temp_in_the_city = {
    'city': 'Moscow',
    'temperature': 20
}
print(temp_in_the_city)
print(temp_in_the_city['city'])
temp_in_the_city['temperature'] = 15
print(temp_in_the_city)
print(temp_in_the_city.get('country'))
print(temp_in_the_city.get('country', 'Russia'))
temp_in_the_city['date'] = '27.05.2019'
print(temp_in_the_city)
print(len(temp_in_the_city))
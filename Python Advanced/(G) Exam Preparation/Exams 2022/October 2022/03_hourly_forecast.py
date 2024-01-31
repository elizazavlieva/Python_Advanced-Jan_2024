def forecast(*args):
    weather_info = {}

    for city, weather in args:
        if weather not in weather_info:
            weather_info[weather] = []
        weather_info[weather].append(city)
    sorted_info = sorted(weather_info.items(), key=lambda kvp: ['Sunny', 'Cloudy', 'Rainy'].index(kvp[0]))
    result = []
    for weather, cities in sorted_info:
        if cities:
            for city in sorted(cities):
                result.append(f'{city} - {weather}')
    return "\n".join(result)


'''TESTS'''
print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))

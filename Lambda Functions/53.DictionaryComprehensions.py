# dictionary comprehensions = create dictionaries using an expression
#                             can replace for loops and certain lambda functions
# -----
# syntax : dictionary = {key: expression for (key,value) in iterable}

cities_in_F = {'New York': 33, 'Boston': 75, 'Chicago': 50, 'LA': 100}

cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

# 2. syntax: dictionary {key expression for (key,value) in iterable if conditional}
weather = {'New York': 'snowing', 'Boston': 'sunny', 'LA': 'sunny', 'Chicago': 'cloudy'}

sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# 3. syntax: dictionary {key: (if/else) for (key,value) in iterable)

cities = {'New York': 33, 'Boston': 75, 'Chicago': 50, 'LA': 100}
desc_cities = {key: ("Warm" if value >= 50 else "It is cold") for (key, value) in cities.items()}
print(desc_cities)


# 4. syntax: dictionary {key: function(value) for (key,value) in iterable}

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "Cold"


cities_in_us = {'New York': 33, 'Boston': 60, 'Chicago': 50, 'LA': 100}
desc_cities1 = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities1)




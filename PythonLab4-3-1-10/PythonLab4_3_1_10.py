# 4.3.1.10 LAB: Converting fuel consumption

# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres

# Defines the 'liters_100km_to_miles_gallon' function
def liters_100km_to_miles_gallon(litres):
    miles = 100 * 1000 / 1609.344
    gallons = litres / 3.785411784
    return miles / gallons

# Defines the 'miles_gallon_to_liters_100km' function
def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

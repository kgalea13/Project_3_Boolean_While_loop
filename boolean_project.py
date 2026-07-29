FEET = 66
METERS = 0.3048
KILOMETERS = 1000
MILES = 5280
MILES_PER_HOUR = 3.1
MINUTES = 60

enter_chains = float(input('Enter distance in chains: '))



convert_feet = enter_chains * FEET
convert_meters = convert_feet * METERS
convert_miles = convert_feet/MILES
convert_kilometers = convert_meters/KILOMETERS
calculate_walking_hours = convert_miles/MILES_PER_HOUR
calculate_time_min = calculate_walking_hours * MINUTES


print(' ')
print('Welcome to the NYC Subway distance converter!')
print(' ')
print(f'Distance: {enter_chains:.3f}')
print(f'Meters: {convert_meters:.3f}')
print(f'Feet: {convert_feet:.3f}')
print(f'Miles: {convert_miles:.3f}')
print(f'Kilometers: {convert_kilometers:.3f}')
print(f'Walking time (minuets): {calculate_time_min:.1f}')
print(' ')
print('Thank you for using the converter. Goodbye!')

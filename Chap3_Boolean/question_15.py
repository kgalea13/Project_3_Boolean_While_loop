
SECONDS = 60
MINUETS = 60
HOUR = 3600
DAYS = 86400


enter_num_sec = int(input('Enter the number of seconds: '))


if enter_num_sec < 60:
    print(f'You have {enter_num_sec} seconds')

elif enter_num_sec >= 60 and enter_num_sec < 3600:
    calc_minuets = enter_num_sec//SECONDS
    calc_seconds = enter_num_sec % SECONDS

    print(f'You have {calc_minuets} minuets and {calc_seconds:} seconds ')

elif enter_num_sec >= 3600 and enter_num_sec <= 86400:
    calc_hours = enter_num_sec // HOUR
    remaining_seconds = enter_num_sec % HOUR
    calc_minuets = remaining_seconds //SECONDS
    calc_seconds = remaining_seconds % SECONDS
    
    print(f'You have {calc_hours} hours, {calc_minuets} minuets, and {calc_seconds} seconds')

elif enter_num_sec > 86400:
    calc_days = enter_num_sec // DAYS
    remaining_seconds = enter_num_sec % DAYS
    calc_hours = remaining_seconds // HOUR
    remaining_seconds = remaining_seconds % HOUR
    calc_minuets = remaining_seconds // MINUETS
    calc_seconds = remaining_seconds % SECONDS

    print(f'{calc_days} day(s), {calc_hours} hour(s), {calc_minuets} minuet(s), and {calc_seconds} second(s).')

else:
    print('Error')
enter_year = int(input('Enter a year: '))


if enter_year % 100 == 0 and enter_year % 400 == 0:
    print('Your year is a leap year.')

elif enter_year % 100 != 0 and enter_year % 4 == 0:
    print('Your year is a leap year')

else:
    print("You don't have a leap year")
    
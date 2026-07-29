enter_coins = input('Enter what you want to count, pennies, nickles, dimes, or quarters: ')

enter_number_coins = int(input('Enter the number of pennies, nickles, dimes, or quarters that will equal 1 dollar: '))


if enter_coins == 'pennies' and enter_number_coins == 100:
    print('You have $1.00')

elif enter_coins == 'pennies' and enter_number_coins > 100:
    print(f'You have ${enter_number_coins/100:.2f}')

elif enter_coins == 'pennies' and enter_number_coins < 100:
    print(f'You have {enter_number_coins/100:.2f} cents')

elif enter_coins == 'nickles' and enter_number_coins == 20:
    print('You have $1.00')

elif enter_coins == 'nickles' and enter_number_coins > 20:
    print(f'You have ${enter_number_coins * 5/100:.2f}')

elif enter_coins == 'nickles' and enter_number_coins < 20:
    print(f'You have {enter_number_coins * 5/100:.2f} cents')

elif enter_coins == 'dimes' and enter_number_coins == 10:
    print('You have $1.00')

elif enter_coins == 'dimes' and enter_number_coins > 10:
    print(f'You have ${enter_number_coins * 10 /100:.2f}')

elif enter_coins == 'dimes' and enter_number_coins < 10:
    print(f'You have {enter_number_coins * 10/100:.2f} cents')

elif enter_coins == 'quarters' and enter_number_coins == 4:
    print('You have $1.00')

elif enter_coins == 'quarters' and enter_number_coins > 4:
    print(f'You have ${enter_number_coins * 25/100:.2f}')

elif enter_coins == 'quarters' and enter_number_coins < 4:
     print(f'You have {enter_number_coins * 25/100:.2f} cents')

else:
    print('error')




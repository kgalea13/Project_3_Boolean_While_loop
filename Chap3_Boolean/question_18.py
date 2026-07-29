enter_preference_1 = input('Is anyone in your party vegetarian? ') #VEGETARIAN T/F
enter_preference_2 = input('Is anyone in your party vegan? ') #VEGAN T/F
enter_preference_3 = input('Is anyone in your party gluten-free? ') #GLUTEN FREE T/F

if enter_preference_1 == 'yes' and enter_preference_2 == 'no' and enter_preference_3 == 'no':
    print('Here are your restaurant choices: ')
    print('Main Street Pizza Co \n Corner Cafe \n Mama\'s Fine Italian \n The chef\'s Kitchen')

elif enter_preference_1 == 'yes' and enter_preference_2 == 'yes' and enter_preference_3 == 'no':
    print('Here are your restaurant choices: ')
    print('Corner Cafe \n The chef\'s Kitchen')

elif enter_preference_1 == 'yes' and enter_preference_2 == 'yes' and enter_preference_3 == 'yes':
    print('Here are your restaurant choices: ')
    print('Corner Cafe \n The chef\'s Kitchen')

elif enter_preference_1 == 'no' and enter_preference_2 == 'no' and enter_preference_3 == 'no':
    print('Here is your restaurant choice: ')
    print('Joe\'s Gormet Burgers')

else:
    print('error')
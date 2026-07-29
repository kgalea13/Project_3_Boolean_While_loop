# Book example
# Using the if-else statement

'''
base_pay = float(input('Enter your base pay: ')) # data type: float/number

MULTIPLIER = 1.5
BASE_HOURS = 40

hours_worked = float(input('Enter the number of hours worked this week: '))

if hours_worked > BASE_HOURS:
    over_time_hours = hours_worked - BASE_HOURS
    overtime_pay = (base_pay * MULTIPLIER) * over_time_hours
    regular_pay = BASE_HOURS * base_pay
    pay_check_amount = regular_pay + overtime_pay
    print(f'Your gross pay for this week is: ${pay_check_amount:.2f}')

else:
    pay_check_amount = hours_worked * base_pay
    print(f'Your gross pay is: ${pay_check_amount:.2f}')

'''
'''

# Each character's number value is compared individually to calculate hierarchy

name1 = input('Enter a name (last name first): ')
name2 = input('Enter a another name (last name first): ')

print('Here are the names, listed alphabetically')

if name1 < name2:
    print(name1)
    print(name2)

else:
    print(name2)
    print(name1)

'''

'''

# length of the string matters, the longer string will win or be greater than

enter_high = input("Enter the word 'high': ")
enter_hi = input("Enter the word 'hi': ")

if enter_high > enter_hi:
    print(enter_high)

else:
    print(enter_hi)

'''

'''

# if elif else structure


number = int(input('Enter a number 1 through 3: '))

if number == 1:
    print('One')

elif number == 2:
    print('Two')

elif number == 3:
    print('Three')

else:
    print("I don't know that number!")
'''

'''
# Programming Questions:

# Question 1


entered_number = int(input('Enter a number between 1 and 7: '))

if entered_number == 1:
    print('Monday')

elif entered_number == 2:
    print('Tuesday')

elif entered_number == 3:
    print('Wednesday')

elif entered_number == 4:
    print('Thursday')

elif entered_number == 5:
    print('Friday')

elif entered_number == 6:
    print('Saturday')

elif entered_number == 7:
    print('Sunday')

else:
    print('Error')
'''

'''
# Areas of Rectangles

rec_1_length = int(input('Enter the length of rectangle 1 in feet: '))
rec_1_width = int(input('Enter the width of rectangle 1 in feet: '))
rec_1_area = rec_1_length * rec_1_width

rec_2_length = int(input('Enter the length of rectangle 2 in feet: '))
rec_2_width = int(input('Enter the width of rectangle 2 in feet: '))
rec_2_area = rec_2_length * rec_2_width

if rec_1_area > rec_2_area:
    print('Rectangle 1 has a greater area.')

elif rec_1_area == rec_2_area:
    print('Rectangle 1 and rectangle 2 have the same area.')

else:
    print('Rectangle 2 has a larger area than rectangle 1')

'''

'''
# Question 3

age = float(input('Enter your age, if younger than 1, then write as a decimal: '))

if age <= 1:
    print('Person is and infant.')
elif age > 1 and age < 13:
    print('Person is a child.')
elif age >= 13 and age < 20:
    print('Person is a teenager.')
elif age >= 20:
    print('Person is an adult.')
else:
    print('Error')

'''
'''
# Question 4

enter_num = int(input('Enter a number 1 through 10: '))

if enter_num == 1:
    print('I')
elif enter_num == 2:
    print('II')
elif enter_num == 3:
    print('III')
elif enter_num == 4:
    print('IV')
elif enter_num == 5:
    print('V')
elif enter_num == 6:
    print('VI')
elif enter_num == 7:
    print('VII')
elif enter_num == 8:
    print('VIII')
elif enter_num == 9:
    print('IX')
elif enter_num == 10:
    print('X')
else:
    print('Error')

'''


'''
#Question 5
enter_mass = float(input('Enter your objects mass: '))

weight = enter_mass * 9.8

if weight > 500:
    print('That is too heavy!')

elif weight < 100:
    print('That is too light')

else:
    print('error')


'''

'''

# Magic Dates
# Calculates if the date you enter is a magic date.
# A date is magic if you multiply the month and date and that product equals the year
# example 6/10/60

# Ask the user to enter a month
month = int(input('Enter a month: '))

# Ask the user to enter a date
date = int(input('Enter a date: '))

# Ask the user to enter a 2 digit year
year = int(input('Enter a 2 digit year: '))

# Multiplies the month and date and store inside month_date
month_date = month * date

# compares month_date (product) with year value. If they are equal they
# this is a magic date
# If they are not equal, program jumps to the else statement/block

if month_date == year:
    print('This is a magic date!')

else:
    print('This is not a magic year.')

'''

'''

# Color Mixer
# This program allows a user to input 2 different primary colors and it displays the secondary color
# that is the result of that mix


color1 = input('Enter a primary color, (red, blue, or yellow): ')
color2 = input('Enter another primary color different from the first, (Red, Blue, or Yellow): ')

if color1 == 'red' and color2 == 'blue':
    print('Your color is purple.')

elif color1 == 'blue' and color2 == 'red':
    print('your color is purple.')

elif color1 == 'red' and color2 == 'yellow':
    print('Your color is orange.')

elif color1 == 'yellow' and color2 == 'red':
    print('Your color is orange')

elif color1 == 'blue' and color2 == 'yellow':
    print('Your color is green.')

elif color1 == 'yellow' and color2 == 'blue':
    print('Your color is green.')

else:
    print('Error')

'''

# Hot Dog Calculator


hotdog_package = 10
bun_package = 8

# Asks user to enter the number of people attending the cookout
num_of_people = int(input('How many people are attending the cookout: ')) 
# Asks user to enter the number of hotdogs each individual person is eating
num_of_hotdogs = int(input('How many hotdogs is each person going to eat: '))

# Calculates the total number of hotdogs by multiplying the number of people attending * num of hotdogs
total_num_hotdogs = num_of_people * num_of_hotdogs

# finds out the how many full packages of hotdogs will be needed:
# by dividing the total number of hotdogs by the number of hotdogs that are in 1 package. 
# Using the integer division operator // to truncate the floating point.
# Example: If 12 % 10 = 1.2 but the // operator gives you: 1
find_full_packages = total_num_hotdogs // hotdog_package

# This will let the program know if there is a remainder by dividing the total number of hotdogs by 1 package of hotdogs
# If there is no remainder then we know that we just need the total package amount that find_full_packages gives to us
# If there is a remainder left, then we need to add 1 package of hotdogs to the amount of find_full_packages.
calculate_remainder = total_num_hotdogs % hotdog_package

find_full_packages_buns = total_num_hotdogs // bun_package
calculate_remainder_buns = total_num_hotdogs % bun_package


if calculate_remainder > 0:
    print(f'You need {find_full_packages + 1} packaages of hotdogs.')
   
elif calculate_remainder < 1:
    print(f'You need {find_full_packages} package of hotdogs')

else:
    print('Error')


if find_full_packages_buns > 0:
    print(f'You need {find_full_packages_buns + 1} packages of buns')
   
elif calculate_remainder_buns < 1:
    print(f'You need {find_full_packages_buns} package of hotdog buns.')

else:
    print('Error')


total_individual_hotdogs = find_full_packages * hotdog_package
hot_dogs_left_over =  total_num_hotdogs - total_individual_hotdogs
print(f'There are {hot_dogs_left_over} hotdogs left over')

total_individual_buns = find_full_packages_buns * bun_package
buns_left_over =  total_num_hotdogs - total_individual_buns
print(f'There are {buns_left_over} buns leftover.')
                      
 

    

   
  









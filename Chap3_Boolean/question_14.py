enter_weight = float(input('Enter how much you weigh in poinds: '))
enter_height = float(input('Enter how tall you are in inches: '))

BMI = enter_weight * (703/enter_height**2)

if BMI >= 18.5 and BMI <= 25:
    print('Your have optimal BMI')

elif BMI < 18.5:
    print('You are underweight')

elif BMI > 25:
    print('You are overweight')

else:
    print('error')
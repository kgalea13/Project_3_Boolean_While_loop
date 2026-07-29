run_again = 'y'.upper()

while run_again == 'y'.upper():

    


    employee_name = input('Enter Employee\'s name: ' )
    base_salary = float(input('Enter Monthly Base: '))

    tier = input('Enter Tier (B, M, OR P): ').upper()

    while tier != 'B' and tier != 'M' and tier != 'P':
        print(f'Tier {tier} is not a legitimate tier value')
        tier = input('Enter Tier (B, M, OR P): ').upper()

    item_sold = int(input('Enter the number of items sold: '))

    while item_sold < 1:
        print('Invalid number for Items Sold')
        item_sold = int(input('Enter the number of items sold: '))
    

    if tier == 'B':
        if item_sold > 9 and item_sold <= 15:
            commission_items = item_sold - 9
            calculate_commission = commission_items * 50
            total_salary = base_salary + calculate_commission
            print(total_salary)

        elif item_sold > 15:
            commission_items_50 = 6
            calculate_commission_50 = commission_items_50 * 50
            commission_items_75 = item_sold - 15
            calculate_commission_75 = commission_items_75 * 75
            total_salary = base_salary + calculate_commission_50 + calculate_commission_75 
            print(total_salary)

        else:
            print('WARNING: Sales must improve.')

    if tier == 'M':
        if item_sold > 14 and item_sold <= 20:
            commission_items = item_sold - 14
            calculate_commission = commission_items * 60
            total_salary = base_salary + calculate_commission
            print(total_salary)

        elif item_sold > 20:
            commission_items_60 = 6
            calculate_commission_60 = commission_items_60 * 60
            calculate_itmes_100 = item_sold - 20
            calculate_commission_100 = calculate_itmes_100 * 100
            total_salary = calculate_commission_100 + base_salary
            print(total_salary)

        else:
            print('WARNING: Sales must improve in order to stay in Tier M.')


    if tier == 'P' or tier == 'p':
        if item_sold >= 20 and item_sold <= 25:
            commission_items = 6
            calculate_commission = commission_items * 75
            total_salary = calculate_commission + base_salary
            print(total_salary)

        elif item_sold > 25:
            commission_items_75 = 6
            calculate_commission_75 = commission_items_75 * 75
            commission_items_125 = item_sold - 25
            calculate_commission_125 = commission_items_125 * 125
            total_salary = base_salary + calculate_commission_75 + calculate_commission_125
            print(total_salary)

        else:
            print('WARNING: Sales must improve to stay in Tier P.')


    run_again = input('Do you want to enter another employee? y/n: ')

    
    


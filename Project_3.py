
TIER_B_MIN = 9
TIER_B_MAX = 15
TIER_M_MIN = 14
TIER_M_MAX = 20
TIER_P_MIN = 20
TIER_P_MAX = 25

TIER_B_MIN_COMM = 50
TIER_B_MAX_COMM = 75

TIER_M_MIN_COMM = 60
TIER_M_MAX_COMM = 100

TIER_P_MIN_COMM = 75
TIER_P_MAX_COMM = 125

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
        if item_sold > TIER_B_MIN and item_sold <= TIER_B_MAX:
            commission_items = item_sold - 9
            calculate_commission = commission_items * TIER_B_MIN_COMM 
            total_salary = base_salary + calculate_commission
            print(f'{employee_name}, Tier:{tier}, Sold {item_sold}, Monthly Payment: {total_salary}')

        elif item_sold > TIER_B_MAX:
            commission_items_50 = 6
            calculate_commission_50 = commission_items_50 * TIER_B_MIN_COMM 
            commission_items_75 = item_sold - 15
            calculate_commission_75 = commission_items_75 * TIER_B_MAX_COMM 
            total_salary = base_salary + calculate_commission_50 + calculate_commission_75 
            print(f'{employee_name}, Tier:{tier}, Sold {item_sold}, Monthly Payment: {total_salary}')

        else:
            
            print('WARNING: Sales must improve.')

    if tier == 'M':
        if item_sold > TIER_M_MIN and item_sold <= TIER_M_MAX:
            commission_items = item_sold - 14
            calculate_commission = commission_items * TIER_M_MIN_COMM
            total_salary = base_salary + calculate_commission
            print(f'{employee_name}, Tier:{tier}, Sold {item_sold}, Monthly Payment: {total_salary}')

        elif item_sold > TIER_M_MAX:
            commission_items_60 = 6
            calculate_commission_60 = commission_items_60 * TIER_M_MIN_COMM
            calculate_itmes_100 = item_sold - 20
            calculate_commission_100 = calculate_itmes_100 * TIER_M_MAX_COMM
            total_salary = calculate_commission_60 + calculate_commission_100 + base_salary 
            print(f'{employee_name}, Tier:{tier}, Sold {item_sold}, Monthly Payment: {total_salary}')

        else:
            
            print('WARNING: Sales must improve in order to stay in Tier M.')


    if tier == 'P':
        if item_sold >= TIER_P_MIN  and item_sold <= TIER_P_MAX:
            commission_items = 6
            calculate_commission = commission_items * TIER_P_MIN_COMM
            total_salary = calculate_commission + base_salary
            print(f'{employee_name}, Tier:{tier}, Sold {item_sold}, Monthly Payment: {total_salary}')

        elif item_sold > TIER_P_MAX:
            commission_items_75 = 6
            calculate_commission_75 = commission_items_75 * TIER_P_MIN_COMM
            commission_items_125 = item_sold - 25
            calculate_commission_125 = commission_items_125 * TIER_P_MAX_COMM
            total_salary = base_salary + calculate_commission_75 + calculate_commission_125
            print(f'{employee_name}, Tier:{tier}, Sold {item_sold}, Monthly Payment: {total_salary}')

        else:
            
            print('WARNING: Sales must improve to stay in Tier P.')

    run_again = input('Do you want to enter another employee? y/n: ')[0].upper()

    
    


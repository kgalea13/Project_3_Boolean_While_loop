enter_num_books = int(input('Enter the number of books you bought this month: '))

if enter_num_books == 0:
    print('You earned 0 points this month.')

elif enter_num_books == 2:
    print('You earned 5 points this month.')

elif enter_num_books == 4:
    print('You earned 15 points this month.')

elif enter_num_books == 6:
    print('You earned 30 points this month')

elif enter_num_books >= 8:
    print('You earned 60 points.')

else:
    print('error')
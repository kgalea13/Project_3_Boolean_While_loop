enter_num_prog = int(input('Enter the number of program packages: '))

if enter_num_prog >= 10 and enter_num_prog <= 19:
    print('You get a 10% discount')

elif enter_num_prog >= 20 and enter_num_prog <= 49:
    print('You get a 20% discount.')

elif enter_num_prog >= 50 and enter_num_prog <= 99:
    print('You get a 30% discount')

elif enter_num_prog >= 100:
    print('You get a 40% discount.')

else:
    print('error')
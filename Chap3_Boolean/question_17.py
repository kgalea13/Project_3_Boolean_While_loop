question_1 = print('Reboot the computer and try to connect')
troubleshoot_1 = input('Did that fix the problem? ')

if troubleshoot_1 == 'no':
    print('Try and reboot the computer')

troubleshoot_2 = input('Did that fix the problem? ')

if troubleshoot_2 == 'no':
    print('Make sure the cables between the routher & modem are pluggen in firmly.')

troubleshoot_3 = input('Did that fix the problem? ')

if troubleshoot_3 == 'no':
    print('Move the router to a new location and try to connect.')

troubleshoot_4 = input('Did that fix the problem?')

if troubleshoot_4 == 'no':
    print('Get a new router')

else:
    print('error')
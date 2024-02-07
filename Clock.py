#Caleb Jergenson 2/7/24

import time


#get minutes from user
minutes = int(input('Enter number of minutes: '))
#loop for minutes and seconds
for minutes in range(0, minutes):
    for seconds in range(0,60):
        print(f'\rminutes:'f'{minutes}' +f'seconds:'f'{seconds}', end='')
        time.sleep(.1)

#more precise ending
    if minutes == (minutes - 1):
        seconds = 0
        print(f'\rminutes:'f'{minutes}' +f'seconds:'f'{seconds}', end='')
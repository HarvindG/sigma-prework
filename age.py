from datetime import datetime

year = int(input('Enter your year of birth: '))
month = int(input('Enter your month of birth: '))
day = int(input('Enter your day of birth: '))

birthdate = datetime(year, month, day)

current_date = datetime.now()

age = current_date.year - birthdate.year - \
    ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))


print('You are now ' + str(age) + ' year old')

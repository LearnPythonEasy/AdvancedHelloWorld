import random
import string
print ('Hello, World!')
person = input ('What is your name? ')
print ('Hello,',person)
age = int(input('How old are you? '))
year = 2017 - age 
print ('So, you were born in', year)
gender = input ('Are you a boy or a girl? ')
print ('So, you are a',gender,'.')
the_password = 1234
while True:
    my_password = int(input('To continue your Python experience, please input the password.'))
    if my_password == the_password :
        print ('Success!')
        break
    else :
        print ('The password is incorrect. Please try again.')
print ('Python is starting...')
def countdown(t):
    import time
    while t >= 0:
        time.sleep(1)
        t -= 1
        print ('Welcome,',person,'...')
t=5
while True:
    choice = input('What would you like to do? Your choices are: Open browser Power Off Bot Spam')
    if choice == 'Open browser':
        print ('Sorry, I cannot do that.')
    elif choice == 'Power Off':
        print ('Powering Off')
        break
    elif choice == 'Bot Spam':
        print ('Goodbye forever, human.')
        while True:
            number = random.randrange(0,2)
            binary = str(number)
            print (binary)

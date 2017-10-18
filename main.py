print ('Hello, World!')
person = input('What is your name? ')
print ('Hello,', person)
age = int(input('How old are you? '))
year = 2017 - age 
print ('So, you were born in', year,'.')
gender = input ('Are you a boy or a girl?')
print ('So, you are a ',gender,'.')
the_password = 1234
password = ['1234', '4321', '1342']
while True:
    my_password = int(input('To continue your Python experience, please input the password: '))
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
        print ('Welcome,', person, '...')


t = 5
while True:
    choice = input('What would you like to do? Your choices are: Open browser Talk to a therapist Power off')
    if choice == 'Open browser':
        print ('Sorry, I cannot do that.')
    elif choice == 'Talk to a therapist':
        print ('I am a computer, do you expect me to solve your problems?')
    elif choice == 'Power off':
        print ('Powering off')
        break
    else:
        print ('That is not an option.')


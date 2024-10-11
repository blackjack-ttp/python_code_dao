import random
from os import system
from time import sleep

def christmas_tree(height):
    colors = ['\033[1;31m', '\033[33m', '\033[1;34m']
    print('\n')
    for i in range(height):
        print(' ' * (height - i), end='')
        for i in range((2*i)+1):
            if random.random() < 0.1:
                color = random.choice(colors)
                print(color, end='')
            else:
                print('\033[32m', end='')
            print('*', end='')
        print()
    print((' ' * (height - 1)) + 'mWm')
    print((' ' * (height - 1)) + 'mWm')
    color = random.choice(colors)
    print(color, (' ' * 8) + 'Merry Christmas')
    print(color, (' ' * 14) + '2024')
    print(color, (' ' * 9) + 'BlackJack-TTP')
    
while True:
    christmas_tree(16)
    sleep(0.2)
    system('clear')
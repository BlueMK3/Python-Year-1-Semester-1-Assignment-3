def print_menu(menu, num):
    print(menu)
    choice = int(input(f'Enter your choice(0-{num}): '))
    while choice < 0 or choice > num:
        choice = int(input(f'Enter your choice(0-{num}): '))
    return choice 

import random 

def street_fighter():
    p1 = input('Player 1: ')
    p2 = input('Player 2: ')
    energy1, energy2 = 100, 100
    while True:
        print(f'{p1}: {energy1}\n{p2}: {energy2}')
        input('Press <Enter> to fight...')
        energy1 -= random.randint(5, 20)
        energy2 -= random.randint(5, 20)
        if energy1 <= 0 and energy2 <= 0:
            print(f'Double K.O. !!!')
            break
        elif energy1 <= 0: 
            print(f'{p2} Win!')
            break
        elif energy2 <= 0:
            print(f'{p1} Win!')
            break

def math_quiz():
    mini, maxi = int(input('Minimum: ')), int(input('Maximum: '))
    n = int(input('Questions: '))
    correct, total = 0, 0
    for k in range(n):
        x = random.randint(mini, maxi)
        y = random.randint(mini, maxi)
        op = random.randint(1, 4)
        op_str = '+' if op == 1 else '-' if op == 2 else \
            '*' if op == 3 else '/'
        key = x + y if op == 1 else x - y if op == 2 else \
            x * y if op == 3 else x // y
        answer = int(input(f'Question#{k + 1}: {x} {op_str} {y} = ')) 
        if answer == key:
            correct += 1
            print('Correct!')
        else: print(f'Incorrect, the answer is {key}')
    print(f'Quiz is over, your mark is {correct} / {n}')

def math_games():
    pass 
def bet_games():
    pass 

import math
def draw_sin():
    for x in range(360):
        y = 40 + int(math.sin(math.radians(x)) * 30)
        for n in range(y): print(' ', end='')
        print('$')


def draw_games():
    pass 

def main():
    main_menu = '==== Main Menu ====\n' + \
                '1-Street Fighter\n2-Math Games\n3-Bet Games\n' + \
                '4-Draw Games\n0-Exit\n===================\n'
    while True:
        choice = print_menu(main_menu, 4)
        if choice == 0: break 
        if choice == 1: street_fighter()
        elif choice == 2: math_games()
        math_menu = '==== Math Menu ====\n' + \
                '1-Draw Sin\n2-Math Games\n3-Bet Games\n' + \
                '4-Draw Games\n0-Exit\n===================\n'
                if math_menu = 
        elif choice == 3: bet_games()
        elif choice == 4: draw_games()
        else: print('Invalid Choice')

    print('Thank you, Bye-Bye')
main()



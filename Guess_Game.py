print('Welcome to this number guessing game \nThanks to downloading my repository . Jamali da putr aa ')
print('1: Try this game')
print('2: Exit')
Enter = int(input('Please choose a number : '))
if Enter==1:
    import random
    Num = random.randint(1,100)
    guess = 1
    while True:
        Winning = int(input('Enter a number between 1 to 100: '))
        if Winning==Num:
            print(f'You Win 😎😎😎😎')
            break
        else:
                if Winning<Num:
                    print('Low')
                    print('Try again')
                    guess+=1
                else:
                    print('High')
                    print('Try again')
                    guess+=1
    print(f'You guessed this number in {guess} times')
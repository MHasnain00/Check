print('Welcome to this games menu.\n')
print('1: Try Guessing game')
print('2: Printing tool')
print('3: Your Lucky number')
print('4: Character count in Paragraph')
print('5: True or False')
print('6: Exit')
print('...........................\n')
Enter = int(input('Please choose a number : '))
if Enter==1:
    import random
    Num = random.randint(1,100)
    guess = 1
    while True:
        Winning = int(input('Enter a number between 1 to 100: '))
        if Winning==Num:
            print(f'You Win 😎')
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
elif Enter==3:
        import random
        print('Here you can find your lucky number ')
        Luck = input('Input your name : ')
        Lucky= random.randint(1,10)
        print(f'{Luck}! Your lucky number is {Lucky}')
elif Enter==4:
    Para=input('Type or Paste a Paragraph to count the words :\n')
    print(f'Your paragraph length is {len(Para)}')
elif Enter==5:
    print('\nA Palindrome is a word which can be read same from end as we read from beginning\nFor Example mam , Madam etc.')
    print('Guess a Palindrome word and let me check your word is Right or wrong\n')
    print('\n..............................\n')
    Check= input('Type a Palindrome word if you know more :')
    def Palindrome_func(a):
        Lower=a.lower()
        Inverse= Lower[::-1]
        if Lower==Inverse:
            print('\n😎Your word is Palindrome and You are intelligent👌🏻\n')
        else:
            print('Your word is not Palindrome.Try again...')
    Palindrome_func(Check)
elif Enter==6:
    print('Good bye ')
else:
     if Enter==2:
         input_Num =input('What you want to write multiple times : ')
         count = (input('How much time you want to write ? : '))
         count= int(count)
         i = 1
         while i <= count:
             print(f'{input_Num} {i}')
             i +=1
             

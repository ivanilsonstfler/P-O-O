secret_number = 20

while True:
    number = input('Guess the number: ')
    
    try:
        number = int(number)
    except ValueError:
        print('Sorry, that is not a valid number.')
        continue
    
    if number != secret_number:
        if number > secret_number:
            print(number, 'is greater than the secret number.')
        else:
            print(number, 'is less than the secret number.')
    else:
        print('You guessed the number:', secret_number)
        break

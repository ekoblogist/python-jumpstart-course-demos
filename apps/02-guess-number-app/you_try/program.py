import random

print('-'*30)
print('    GUESS THE NUMBER GAME')
print('-'*30)
print()

random_number = random.randint(1, 1000)

number_input = 0

while number_input != random_number:
    number_input = int(input('Please enter the number between 1 and 1000:  '))

    if number_input < random_number:
        print(f'Number you are trying to guess is bigger than {number_input}. Please try again.')
    elif number_input > random_number:
        print(f'Number you are trying to guess is smaller {number_input}. Please try again.')
        
print(f'Congratulations! You guessed the number! It is {random_number}.')
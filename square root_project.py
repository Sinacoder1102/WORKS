# Importing models
from delay_write import delay
import math
from colored import fg

# Using colored model
yellow = fg('yellow')
reset = fg('white')
red = fg('red')
green = fg('green')

# Main code
def main_program():
    try:
        print('============================================================================')
        radical = float(input('Please enter the number you want to take its square root: '))
        sqr = math.sqrt(radical)
        print(green , end='')
        delay(f'The square root of your number is {sqr}')

        # Check if the number is a perfect square
        if sqr.is_integer():
            print(green , end='')
            delay('+ The numbers has a perfect square.')
            print(green , end='')
        else:
            print(red , end='')
            delay("- The number doesn't have a perfect square.")
            print(reset , end='')
        print(reset , end='')

    except BaseException:
        print(red , end='')
        delay('Error! Please write a number.')
        print(reset , end='')

    finally:
        print(yellow , end='')
        delay('Operation done!')
        print(reset , end='')

# Using a while loop to make the program repeatable
while True:
    main_program()
    question = input('Do you want to calculate again? (y/n): ').lower()
    if question in ['y', 'yes']:
        continue
    elif question in ['n', 'no']:
        break

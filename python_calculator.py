import sys

class Calculator:
    def sum(self, first_number, second_number):
        try:
            print(f'Result: {first_number} + {second_number} = {first_number + second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to sum {first_number} and {second_number}...\n{type(exc).__name__}: {exc}\n')

    def sub(self, first_number, second_number):
        try:
            print(f'Result: {first_number} - {second_number} = {first_number - second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to subtract {second_number} from {first_number}...\n{type(exc).__name__}: {exc}\n')

    def mult(self, first_number, second_number):
        try:
            print(f'Result: {first_number}*{second_number} = {first_number*second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to multiply {first_number} and {second_number}...\n{type(exc).__name__}: {exc}\n')

    def div(self, first_number, second_number):
        try:
            print(f'Result: {first_number}/{second_number} = {first_number/second_number}\n')
        except ZeroDivisionError as exc:
            print(f'Cannot divide by zero...\n{type(exc).__name__}: {exc}')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to divide {first_number} by {second_number}...\n{type(exc).__name__}: {exc}\n')

def main():
    try:
        number_1 = float(input('\nType the first number: ').replace(',', '.'))
    except (TypeError, ValueError, OverflowError) as exc:
        print(f'{type(exc).__name__}: {exc}\n')
        sys.exit(1)

    try:
        number_2 = float(input('Type the second number: ').replace(',', '.'))
    except (TypeError, ValueError, OverflowError) as exc:
        print(f'{type(exc).__name__}: {exc}\n')
        sys.exit(1)

    operation = int(input(f'\nChoose an option:\
            \n1. SUM numbers\
            \n2. SUBTRACT {number_2} from {number_1}\
            \n3. SUBTRACT {number_1} from {number_2}\
            \n4. MULTIPLY numbers\
            \n5. DIVIDE {number_1} by {number_2}\
            \n6. DIVIDE {number_2} by {number_1}\
            \nYour option: '))

    print()

    calculator = Calculator()  # Create a new Calculator instance
    if operation == 1:
        calculator.sum(number_1, number_2)
    elif operation == 2:
        calculator.sub(number_1, number_2)
    elif operation == 3:
        calculator.sub(number_2, number_1)
    elif operation == 4:
        calculator.mult(number_1, number_2)
    elif operation == 5:
        calculator.div(number_1, number_2)
    elif operation == 6:
        calculator.div(number_2, number_1)
    else:
        print('Invalid option selected...\n')

if __name__ == '__main__':
    raise SystemExit(main())

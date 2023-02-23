"""
This module contains a simple calculator class that can perform basic
arithmetic operations on two numbers.

The Calculator class has four methods:
- sum: Adds two numbers
- sub: Subtracts one number from another
- mult: Multiplies two numbers
- div: Divides one number by another

All methods take two arguments of type float and return None.
If any of the arguments is not a float, a TypeError is raised.
If the division by zero is attempted, a ZeroDivisionError is raised.

Example usage:
>>> calculator = Calculator()
>>> calculator.sum(2.5, 3.7)
6.2
>>> calculator.sub(10, 5)
5
>>> calculator.mult(2.5, 3)
7.5
>>> calculator.div(10, 2)
5.0
"""
import sys

class Calculator:
    """A simple calculator class that can perform basic mathematical operations"""
    def sum(self, first_number: float, second_number: float) -> None:
        """
        Calculates the sum of two numbers and prints the result

        Args:
            number_1 (float): The first number.
            number_2 (float): The second number.
        """
        try:
            print(f'Result: {first_number} + {second_number} = \
                {first_number + second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to sum {first_number} and \
                {second_number}...\n{type(exc).__name__}: {exc}\n')

    def sub(self, first_number: float, second_number: float) -> None:
        """
        Calculates the subtraction of two numbers and prints the result

        Args:
            number_1 (float): The first number.
            number_2 (float): The second number.
        """
        try:
            print(f'Result: {first_number} - {second_number} = \
                {first_number - second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to subtract {second_number} \
                from {first_number}...\n{type(exc).__name__}: {exc}\n')

    def mult(self, first_number: float, second_number: float) -> None:
        """
        Calculates the multiplication between two numbers and prints the result

        Args:
            number_1 (float): The first number.
            number_2 (float): The second number.
        """
        try:
            print(f'Result: {first_number}*{second_number} = \
                {first_number*second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to multiply {first_number} and \
                {second_number}...\n{type(exc).__name__}: {exc}\n')

    def div(self, first_number: float, second_number: float) -> None:
        """
        Calculates the division between two numbers and prints the result

        Args:
            number_1 (float): The first number.
            number_2 (float): The second number.
        """
        try:
            print(f'Result: {first_number}/{second_number} = \
                {first_number/second_number}\n')
        except ZeroDivisionError as exc:
            print(f'Cannot divide by zero...\n{type(exc).__name__}: {exc}')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to divide {first_number} by \
                {second_number}...\n{type(exc).__name__}: {exc}\n')

    def pow(self, first_number: float, second_number: float) -> None:
        """_summary_

        Args:
            first_number (float): _description_
            second_number (float): _description_
        """
        try:
            print(f'Result: {first_number}**{second_number} = \
                {first_number**second_number}\n')
        except (TypeError, ValueError, OverflowError) as exc:
            print(f'It was not possible to pow {first_number} by \
                {second_number}...\n{type(exc).__name__}: {exc}\n')

def main():
    """Main function called when __name__ == '__main__'"""
    try:
        number_1 = float(input('\nType the first number: ')\
            .replace(',', '.'))
    except (TypeError, ValueError, OverflowError) as exc:
        print(f'{type(exc).__name__}: {exc}\n')
        sys.exit(1)

    try:
        number_2 = float(input('Type the second number: ')\
            .replace(',', '.'))
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

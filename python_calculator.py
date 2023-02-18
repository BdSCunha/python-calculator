class Calculator:
    def sum(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        print(n1 - n2)

    def mult(self, n1, n2):
        print(n1*n2)

    def div(self, n1, n2):
        print(n1/n2)

def main():
    number_1 = float(input('\nType the first number: '))
    number_2 = float(input('Type the second number: '))

    operation = int(input(f'\nChoose an option:\
            \n1. SUM numbers\
            \n2. SUBTRACT {number_2} from {number_1}\
            \n3. SUBTRACT {number_1} from {number_2}\
            \n4. MULTIPLY numbers\
            \n5. DIVIDE {number_1} by {number_2}\
            \n6. DIVIDE {number_2} by {number_1}\
            \nYour option: '))

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

if __name__ == '__main__':
    raise SystemExit(main())

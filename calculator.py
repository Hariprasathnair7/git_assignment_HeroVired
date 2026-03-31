
import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    # Square root function
    # Square root feature supposed to be added as part of feature/sqrt branch 
    # but added earlier. So inserting num4 to calculate sqrt in new branch
    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()

    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")
    num4 = 36
    print(f"The square root of {num4} = {calculator.square_root(num4)}")
            
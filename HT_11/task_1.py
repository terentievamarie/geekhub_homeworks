"""
1. Створити клас Calc, який буде мати атрибут last_result та 4 методи. 
Методи повинні виконувати математичні операції з 2-ма числами, 
а саме додавання, віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися 
до атрибута last_result він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повинен 
повернути результат виконання ПОПЕРЕДНЬОГО методу.
    Example:
    last_result --> None
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...
- Додати документування в клас (можете почитати цю статтю:
"""


class Calc:
    """
    A class for basic arithmetic operations and tracking the last result.

    Attributes:
        last_result: Holds the result of the last operation. Initialized to None.
    """
    def __init__(self):
        self.last_result = None
        self.operations = [self.last_result]


    def add(self, x, y):
        """
        Adds two numbers and updates last_result.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            The result of operation x and y.
        """
        result = x + y
        self.operations.append(result)
        self.last_result = self.operations[-2]
        return result


    def subtract(self, x, y):
        """
        Subtracts y from x and updates last_result.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            TThe result of operation x and y.
        """
        result = x - y
        self.operations.append(result)
        self.last_result = self.operations[-2]
        return result


    def multiply(self, x, y):
        """
        Multiplies two numbers and updates last_result.

        Args:
            x: The first number.
            y: The second number.

        Returns:
            The result of operation x and y.
        """
        result = x * y
        self.operations.append(result)
        self.last_result = self.operations[-2]
        return result


    def divide(self, x, y):
        """
        Divides x by y and updates last_result.

        Args:
            x: The numerator.
            y: The denominator.

        Returns:
            The result of operation x and y.
        """
        if y != 0:
            result = x / y
            self.operations.append(result)
            self.last_result = self.operations[-2]
            return result
        else:
            raise ValueError("Cannot divide by zero.")


obj = Calc()
print(obj.last_result)
print(obj.add(1, 1))
print(obj.last_result)
print(obj.multiply(2, 3))
print(obj.last_result)
print(obj.multiply(3, 4))
print(obj.last_result)
obj.multiply(3, 5)
print(obj.last_result)
obj.subtract(2, 5)
print(obj.last_result)
obj.multiply(2, 1)
print(obj.last_result)
 
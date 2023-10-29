"""
Повинна бути 1 ф-цiя, яка б приймала 3 аргументи - один з яких операцiя,
яку зробити!
Аргументи брати від юзера (можна по одному - 2, окремо +, окремо 2;
можна всі разом - типу 1 + 2). Операції що мають бути присутні:
 +, -, *, /, %, //, **. 
Не забудьте протестувати з різними значеннями на предмет помилок!
"""


def calculator():
    result = None
    
    try:
        number_1 = int(input("Enter the first operand: "))
        number_2 = int(input("Enter the second operand: "))
        operation = input("Enter the operation: ")
        
        if operation == "+":
            result = number_1 + number_2
        elif operation == "-":
            result = number_1 - number_2
        elif operation == "*":
            result = number_1 * number_2
        elif operation == "/":
            if number_2 == 0:
                print("Division by zero is not allowed.")
            else:
                result = number_1 / number_2
        elif operation == "%":
            result = number_1 % number_2
        elif operation == "//":
            if number_2 == 0:
                print("Floor division by zero is not allowed.")
            else:
                result = number_1 // number_2
        elif operation == "**":
            result = number_1 ** number_2
        else:
            print("Invalid operation. Try again.")

        if result is not None:
            print(f"{number_1} {operation} {number_2} = {result}")
        
    except ValueError:
        print("Enter an integer value, please.")
    except Exception as e:
        print(f"Oops! An error occurred: {e}")

calculator()
 
"""
2. Написати функцію, яка приймає два параметри: 
ім'я (шлях) файлу та кількість символів. 
Файл також додайте в репозиторій. 
На екран повинен вивестись список із трьома блоками 
- символи з початку, із середини та з кінця файлу. 
Кількість символів в блоках - та, яка введена в другому параметрі. 
Придумайте самі, як обробляти помилку, наприклад, 
коли кількість символів більша, ніж є в файлі або, 
наприклад, файл із двох символів і треба вивести по одному символу, 
то що виводити на місці середнього блоку символів?). 
Не забудьте додати перевірку чи файл існує.
"""


class NoSymbolsException(Exception):
    def __str__(self):
        return f"No symbols in this file. Nothing to read"
    
    
class LargerSymbolsException(Exception):
    def __str__(self):
        return f"The quatity of input symbols is larger than lenght of your file"
    

class CenterSymbolsException(Exception):
    def __str__(self):
        return f"The number of middle symbols cannot be determined due to the mismatch in parity."


def print_symbols(files_name, symbols_quantity):
    if symbols_quantity <= 0:
        raise NoSymbolsException
    try:
        with open(files_name) as file:
            content = file.read()

        if len(content) == 1:
            print([content[0]])
        
        if len(content) == 2:
            print([content[0], 'There is no center symbol', content[1]])
        
        if len(content) < symbols_quantity:
            raise LargerSymbolsException
        
        if len(content) % 2 != symbols_quantity % 2:
            raise CenterSymbolsException

        start_symbols = content[:symbols_quantity]
        center = len(content) // 2
        center_symbols = content[center - (symbols_quantity // 2): center + (symbols_quantity // 2) + 1]
        end_symbols = content[-symbols_quantity:]
        print([start_symbols, center_symbols, end_symbols])
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except (NoSymbolsException,LargerSymbolsException, CenterSymbolsException) as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    try:
        print_symbols('HT_09/task_2_files/rubaiyat.txt', 5)
    except (NoSymbolsException, LargerSymbolsException, CenterSymbolsException) as e:
        print(f"Error: {e}")
 
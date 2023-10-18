#3. Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.

number = int(input("Please, enter a number: "))
res = sum(i for i in range(1, number + 1))
print(res)

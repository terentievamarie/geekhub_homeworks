# 2. Write a script which accepts two sequences of comma-separated colors from user. 
#Then print out a set containing all the colors from color_list_1 which are not present in color_list_2.

colors_list_1 = input(
    "Please, enter a sequence of comma-separated colors: ").split(", ")
colors_list_2 = input(
    "Please, enter another sequence of comma-separated colors: ").split(", ")
colors_set_1 = set(colors_list_1)
colors_set_2 = set(colors_list_2)
result = colors_set_1.difference(colors_set_2)
print(result)
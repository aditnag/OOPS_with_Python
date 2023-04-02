# 19. From a list containing ints, strings and floats, make three lists to store them separately

mixed_list = [1, 2.0, 'three', 4, 'five', 6.0]

int_list = []
float_list = []
str_list = []

for element in mixed_list:
    if isinstance(element, int):
        int_list.append(element)
    elif isinstance(element, float):
        float_list.append(element)
    elif isinstance(element, str):
        str_list.append(element)

for i in int_list:
    print(i, end=" ")
print()

for i in float_list:
    print(i, end=" ")
print()

for i in str_list:
    print(i, end=" ")
print()

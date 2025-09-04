my_dict = {}  # Avoid using 'dict' as a variable name
n = int(input("How many numbers do you want to add in Dictionary: "))
for x in range(1, n + 1):
    my_dict[x] = x * x
print(my_dict)

number = [12, 34, 2, 5, 6, 76]
first = number[0]
second = number[0]
for i in number:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print("second", second)



liniya = input()
count = 0
for z in liniya:
    if z == '*' or z == ';' or z == ':':
        count += 1
print(count)
liniya = input()
opens = liniya.find('(')
closes = liniya.find(')')
if opens != -1 and closes != -1:
    result = liniya[opens+1:closes]
    print(result)
else:
    print('да')
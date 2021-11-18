fizz = 4
buzz = 6
for x in range(1,26):
    if x % 4 == 0 and x % 6 == 0:
        print('FB', end=" ")
    elif x % 4 == 0:
        print('F', end=" ")
    elif x % 6 == 0:
        print('B', end=" ")
    else:
        print (x, end=" ")










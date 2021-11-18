
a = int(input('Enter the you one number'))
b = int(input('Enter the you two number'))
if a % b == 0:
    print(a,'divided entirely into', b)
    print("Remainder -", a % b)
else:
    print(a,' not divisible by', b )
    print("Remainder -", a % b)


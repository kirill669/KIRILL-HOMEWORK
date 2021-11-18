list_ = [3, 7, 19, 101, 56, 4, 88, 31]
def square_(x):
    i = 2
    while x % i != 0:
        i = i + 1
        if x <= i:
            return x*x
result = list(map(square_, list_))
print(result)
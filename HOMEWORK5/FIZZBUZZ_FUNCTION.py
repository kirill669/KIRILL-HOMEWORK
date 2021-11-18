def fizzbuzz(n):
    result = []
    onenumber = int(input('Please enter the first number'))
    twonumber = int(input('Please enter the second number'))
    for i in range(1, n+1):
        if i % onenumber == 0 and i % twonumber == 0:
            result.append("FB")
        elif i % onenumber == 0:
            result.append('F')
        elif i % twonumber == 0:
            result.append('B')
        else:
            result.append(str(i))
    return result
thenumber = int(input('Please enter the number of digits'))
def main():
    print(', '.join(fizzbuzz(thenumber)))
main()
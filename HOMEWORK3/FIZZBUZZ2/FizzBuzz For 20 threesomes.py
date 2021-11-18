numbers_fizzbuzz = 'fizbuzz.txt'
result_fizzbuzz = 'result.txt'
filenumbers_ = open(numbers_fizzbuzz, 'r')
fileresult = open(result_fizzbuzz, 'w')
for line in filenumbers_:
    fizz, buzz, stop = line.split()
    fizz = int(fizz)
    buzz = int(buzz)
    stop = int(stop)
    for i in range(1, stop + 1 ):
        if i % fizz == 0 and i % buzz == 0:
            fileresult.write(' FB ')
        elif i % fizz == 0:
            fileresult.write(' F ')
        elif i % buzz == 0:
            fileresult.write(' B ')
        else:
            fileresult.write(' ' + str(i) + ' ')
    fileresult.write('\n')
filenumbers_.close()
fileresult.close()

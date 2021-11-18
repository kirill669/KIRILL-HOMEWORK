nominals = [1000,500,200,100,50,20,10]
summa = int(input('Enter your amount'))
for i in nominals:
    if summa // i:
        count = summa // i
        summa = summa - i*count
        print(count,' nominal ', i)
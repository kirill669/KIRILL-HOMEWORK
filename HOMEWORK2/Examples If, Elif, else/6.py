a = int(input('salary this month'))
b = int(input('salary last month'))
if a > b:
    print('Salary more by', a - b, 'dollars')
elif a < b:
    print('In that month, the salary was more', b - a, 'dollars')
elif a == 0 and b == 0:
    print('Did I work at all?')
else:
    print('I earned that month and that month the same')
print ('In two months I have earned',a + b,'dollars')


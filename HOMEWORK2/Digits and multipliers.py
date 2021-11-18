a = int(input('Number'))
s = 0
res =[]
while a > 10:
    s = a // 10
    res.append(a - s*10)
    a = s

res.append(a)
out = []
for i, id_ in enumerate(res):
    out.append(f'{id_}*10**{i}')
out.reverse()
print(out)

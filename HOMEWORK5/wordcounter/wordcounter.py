text_vicing = open('vicing.txt', 'r')
text = text_vicing.read().lower().split()

def wordcount(word):
    if word in res:
        res[word] += 1
    else:
        res[word] = 1

res = dict()
list(map(wordcount, text))
print(res)


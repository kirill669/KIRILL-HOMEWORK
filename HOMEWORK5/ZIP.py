hero_ = ['Kirill', 'Batman', 'Avatar', 'Naruto']
where = ['Real life', 'DC', 'Cartoon', 'Anime' ]
# create a dictionary using "dict computing"
d1 = {i: name for i, name in zip(hero_, where)}
print(d1)
update_hero_ = ['Spider-Man']
update_where = ['Marvel']
print('Updating information')
d1.update(zip(update_hero_, update_where))
print(d1)


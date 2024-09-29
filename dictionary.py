#dictionary ois the unorderd collection of key and value pair
#create dictionary
d={
    'name':'bholeram',
    'class':'iv',
    'school':'shree sai public school',
    'city':'mandsaur',
    'subject':'maths'
}
print(d)
c=d['city']
print(c)
for n in d:
    print(n,d[n])

#to get the values with the help of key
print(d.get('name'))
print(d.get('city'))
print(d.get('subject'))
print(d.get('school'))

#keys
print(d.keys())
print(d.values())
print(d.items())

#delete in dictionary
del(d['name'])
print(d)
del(d['city'])
print(d)
p=d.pop('school')
print(p)
print(d)
d['school']='excellence'
print(d)
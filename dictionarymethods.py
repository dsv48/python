#clear
car = {"brand": "Ford","model": "Mustang","year": 1964}
car.clear()
print(car)

#copy dict to new
dict = { "name": "srinivbas","dob": "15-07-1990","ph": 9666441065}
x = dict.copy

#fromkeys to form dict
x = ('key1', 'key2', 'key3')
y = 1,2,3
thisdict = dict.fromkeys(x, y)
print(thisdict)

#get the value from dict
dict = {"brand": "Ford", "model": "Mustang","year": 1964}
x = dict.get("model")
print(x)

#pop delete specific item
dict = {"name": "srinivas","dob": "15-07-1990","ph": 9666441065}
dict.pop("dob")
print(dict)

#keys
dict = {"name": "srinivas","dob": "15-07-1990","ph": 9666441065}
x = dict.keys()
print(x)

#items
dict = {"name": "srinivas","dob": "15-07-1990","ph": 9666441065}
x = dict.items()
print(x)




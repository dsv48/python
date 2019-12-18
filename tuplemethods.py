#count:count the given element occurence in a tuple
tuple = ('a','i','e','o','i','u','i',)
count = tuple.count('i')
print('count of i is :', count)

#index:index of the given element
tuple = ('a','i','e','o','i','u','i',)
index = tuple.index('e')
print('index of e is :', index)

#any:returns True if any element of an iterable is True. If not, false
s = "This is good"
print(any(s))
# 0 is False
# '0' is True
# s = '000'
print(any(s))
s = ''
#empty iterable gives false
print(any(s))

#len
atuple = (1,2,3,4,5,6)
print(len(atuple))

#slicing
t = (1,2,3,4,5)
print(t[2:])

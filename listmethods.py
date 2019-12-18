# Adds List Element as value of List.
List = ['srinivas', 'parepalli', '1990',]
List.append(2019)
print(List)

#insert a value in particular index
List = ['srinivas', 'parepalli','goud']
List.insert(3,1990)
print(List)

#extend:content add one list to another list
List1 = [1, 2, 3]
List2 = [2, 3, 4, 5]
List1.extend(List2)
print(List1)

#sum of the list
list = [1,2,3,4,5]
print(sum(list))

#count given element total occurence
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(List.count(1))

#length:total lenth of list

List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1]
print(len(List))

#min:minimum of elememts of list
List = [2,3.5,4,5.33, 1.054, 2.5]
print(min(List))

#max:max of elements of list
List = [1,2.3,3.5,4.6,5,5.56,448.9]
print(max(List))

#pop:print the specific index
List = [1,2,3,4,5,6,7,8,9,10]
print(List.pop())#empty will take last index
print(List.pop(4))

#delete the element in a list
list = [1,2,3,4,5]
del list[2]
print(list)





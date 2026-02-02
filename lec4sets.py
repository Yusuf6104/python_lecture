# Sets in python
collection= set()
collection = {1, 2, 3, 4, 'world', 'hello'}
print(collection)
print(list(collection))
print(len(list(collection)))

#set method
collection = set()
collection.add(1) # set.add() method 
collection.add(2)
collection.add("yusuf")
collection.add((1,2,3,4))
collection.remove(1)#set.remove()method
collection.clear()#set.clear () method

print(collection)

#set.pop()
collection = {"hello", "world", "yusuf","coding","python"}
print(collection.pop())
print(collection.pop())


#set.union()method

collection1 = {1,2,3,4}
collection2={3,4,5,6}
print(collection1.union(collection2))
print(collection1)
print(collection2)

#set.intersection method

ollection1 = {1,2,3,4}
collection2={3,4,5,6}
print(collection1.intersection(collection2))
print(collection1)
print(collection2)



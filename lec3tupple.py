# tupples in python
tup= (1,2,3)
print(tup)
print(type(tup))

#empty tupple
tup = ()
print(tup)
print(type(tup))

#single tupple
tup = (1,)
print(tup)
print(type(tup))

#multipe value
tup = (1,2,1,3,)
print(tup[1:3]) #tupple slicing
print(type(tup))

#tupple method

tup = (1,2,1,3,)
print(tup.index(2))

tup = (1,2,1,3,)
print(tup.count(2))

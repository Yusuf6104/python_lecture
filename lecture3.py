# list 
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
len = len(marks)
print(marks)
print(len)
print(marks[0])
print(marks[1])

student = ["yusuf",87.3,19,"lucknow"]
print(student[0])
print(student)

#list slicing

marks = [87, 78, 90, 95, 55]
print(marks[1:4]) #positive indexing
print(marks[-3:-1]) # negative indexing

# list methods

list = [2,3,1]
list.append(4)
list.sort()#acending order
list.sort(reverse=True)#decending order
print(list)

list = [2,3,1]
list.reverse()
print(list)

list = [2,3,1]
list.insert(1,5)
print(list)

list = [2,3,1]
list.remove(1)
print(list)

list = [2,3,1]
list.pop(2)
print(list)

list = [2,3,1]
list.copy()
print(list)




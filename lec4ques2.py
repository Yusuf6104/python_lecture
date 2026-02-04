#Wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subjects name as key & marks as values.
marks={}
x= input("marks of sub1:")
marks.update({"sub1":x})

x= input("marks of sub2:")
marks.update({"sub2":x})

x= input("marks of sub3:")
marks.update({"sub3":x})
   
print(marks)

# Figure out a way to store 9 & 9.0 uas seprate vallues in the set. 

val = set()
val={
    ("float",9.0),
    ("int",9)
}    
print(val)
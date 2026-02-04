# python
*Basic
  .print-function
  .("hello world")-output
  .name ="yusuf" (name- variable, "yusuf"-value with string")
  .age=20(age-variable,20-value)
  .age2=age(age=20 assign in age2)

*Identifier
 -combination of uppercase and lowercase letters, digits or an underscore(_).
 So (type(_))-Identifier

# Datatypes

  .Integer - (925,-25,0)
  .String -"yusf",','''
  .Float - 3.14,2.5,3.4
  .Boolean - True,False
  .None - a=None

# Keywords
 and,as,assert,break,class,continue,def,del,elif,else,except,finally,False,for,from,global,if,import,in,is,lambda,nonlocal,None,not,or,pass,raise,return,True,try,with,while,yeild

*Python is a case sensetive language
   ex- Apple,apple are different in python.

*For comment
 -('')for single line
-("""
 multiline
 """)   

*Types of Operators in python
 An operator is a symbol that performs a certain operation between operands.

 .Arthimetic Operators (+,-,*,/,%,**)
 .Relation/Comparison Operators (==,!=,>,<,>=,<=)
 .Assignment operators (=,+=,-=,*=,/=,%=,**=)
 .Logical Operators ( not,and,or)

*Type conversion

-type conversion means automtic conversion

*Type casting
 Datatype(val)
 ex- a,b 

*Input in python

 input() #result for input() is always a str 
 int (input ()) #int 
 float(input()) #float


# String 
String is a data type stores a sequence of character.

Basic operations 

# concatenation

"hello" + "world" - "helloworld"

*length of str

 len(str)

# indexing 
H e l l o _ W o r l d
0 1 2 3 4 5 6 7 8 9 10

str[0] is 'H' , str[1] is 'e' ...

str[0] = 'H' *not allowed

# Slicing
 str[ starting_idx : ending_idx] *ending idx is not included.

 str = "Hello"

 str[1:4] is "ell"

 str[ : 4] is same as str[0:4]
 str[1 : ]is same as str[1:len(str)]
 
 *Negative Index

 A p p l e
-5-4-3-2-1

str = "Apple"
str[-3 :-1] is "pl"

# String function
  str.endswith()
  str.find()
  str.count()
  str.replace()

# Conditional Statements
if-elif-else(syntax)

if(condition):
    Statement1
elif(condition):
    Statement2
else:
    Statement

# List in python    

A built-in data type that stores set of values 
it can store elements of different types (integers,    float,string, etc )

  *marks = [87, 64, 33, 44, 76]  marks[0], marks[1]...

  *student = ["Karan",85,"delhi"] student[0],student[1]..

  *student[0] = "Arjun"   -alloweded in python
   
  *len(student)

list-> mutable
string-> immutable  

# List Slicing

list_name[ starting_idx : ending_idx ] #ending idx is not included
Similar to String Slicing

marks = [87, 64, 33, 95, 76]

marks[ 1 : 4 ] is [64, 33, 95]

marks[ : 4 ] is same as marks[ 0 : 4]

marks[ 1 : ] is same as marks[ 1 : len(marks) ]

marks[ -3 : -1 ] is [33, 95]

# List Methods

list.append(4) #adds one element at the end
list = [2, 1, 3]

list.insert( idx, el ) #insert element at index
list.sort( ) #sorts in ascending order

list.reverse( ) #reverses list
list.sort( reverse=True ) #sorts in descending order
[1, 2, 3]

[2, 1, 3, 4]

[3, 2, 1]

[3, 1, 2]

# List Methods

list.remove(1) #removes first occurrence of element
list = [2, 1, 3, 1]

list.pop( idx ) #removes element at idx

# Tuples in Python

A built-in data type that lets us create immutable sequences of values.

tup = (87, 64, 33, 95, 76) #tup[0], tup[1]..

tup[0] = 43 #NOT allowed in python

tup1 = ( )

tup2 = ( 1, )

tup3 = ( 1, 2, 3 )

# Tuple Methods

tup.index( el ) #returns index of first occurrence
tup = (2, 1, 3, 1)

tup.count( el ) #counts total occurrences tup.count(1) is 2

tup.index(1) is 2

# Dictionary in Python

Dictionaries are used to store data values in key:value pairs

“key” : value

They are unordered, mutable(changeable) & don’t allow duplicate keys

dict[”name”], dict[”cgpa”], dict[”marks”]

dict[”key”] =

“value” #to assign or add new

# Dictionary in Python

Nested Dictionaries

student[”score”][”math”]

# Dictionary Methods

myDict.keys( ) #returns all keys
 
myDict.values( ) #returns all values

myDict.items( ) #returns all (key, val) pairs as tuples

myDict.get( “key““ ) #returns the key according to value

myDict.get( “key““ ) #re

myDict.update( newDict ) #inserts the specified items to the dictionary\

# Set in python

Set is the collection of the unordered items.

Each element in the set must be unique & immutable.

nums = { 1, 2, 3, 4 }

set2 = { 1, 2, 2, 2 }
#repeated elements stored only once, so it resolved to {1,2} 

null_set = set( ) #empty set syntax

set pases tuple but
set can't store list and dictionary

# Set Methods

set.add( el ) #adds an element

set.remove( el ) #removes the elem an

set.clear( ) #empties the set

set.pop( ) #removes a random value

set.union( set2 ) #combines both set values & returns new

set.intersection( set2 ) #combines common values & returns new

# Loops in Python

Loops are used to repeat instructions.

#while loop
while condition :
#some work

print hello 5 times
print numbers from 1 to 5

show infinite, iterator

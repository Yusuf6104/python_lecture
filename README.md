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

if(condition):Statement1
elif(condition):Statement2
else:StatementN

 

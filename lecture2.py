#chapter 2

#strings
str1="This is a stirng"
str2='yusufabdullah'
str3="""this is a string"""
#escape sequence 
str1 = "This is a sting.\nwe are creating it in python"
str2 = "this is a string. \twe are creating it in python" 

#concatenation
str1= "hello"
str2= "world"
final_str= str1 + "" + str2
print(final_str) 
#length
str1 = "hello"
len1 = len(str1)
print(len1)

str2 = "world"
len2 = len(str2)
print(len2)
final_str= str1+ " " +str2
print(final_str)
print(len(final_str))

#indexing
str = "hello world"
print(str[6])

#slicing
str = "hello"
print(str[0:5])
print(str[0:len(str)])
print(str[0:])
print(str[:4])

#negative index
str = "apple"
print(str[-5 : -2])

#string function 
str= " i am yusuf abdullah"
print(str.endswith("lah"))

str= "i am yusuf abdullah"
str= str.capitalize()# for capital first letter ever time
print(str.capitalize())

str= " i am yusuf abdullah"
print(str.replace("u","s"))
print(str.replace("yusuf","abdullah"))

str= " i am yusuf abdullah"
print(str.find("a"))
print(str.find("abdullah"))

str= " i am yusuf abdullah"
print(str.count("a"))


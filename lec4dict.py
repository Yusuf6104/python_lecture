# Dictionary python

info = {
    "key" : "value",
    "name" : "yusuf abdullah",
    "learning" : "coding" ,
    "age": 20,
    "is_adult": True,
     23.3 : 9.6,
}
    
print(info)
print (info["name"])
print(info["age"])

info["name"]= " Yusuf "
info["surname"] = "abdullah"
print(info)

#empty dictionary
null_dict = {}
null_dict ["name"]= "yusufabdullah"
print(null_dict)

#nested dictionary

student = {
    "name": "yusuf" ,
    "subjects":  {
        "phy": 87,
        "chem":97,
        "maths": 99,
    }
}
print(student)

#dictionary method 

student = {
    "name": "yusuf" ,
    "subjects":  {
        "phy": 87,
        "chem":97,
        "maths": 99,
    }
}
student.update({"city": "lucknow"})
new_dict ={"enroll": 2400123,}
student.update(new_dict) # dict.update() method
print(student.keys())# dict.keys() method
print(len(list(student.keys()))) 
print(student.values()) # dict.values() method
print(list(student.values()))
print(student.items()) # dict.items() method
print(list(student.items()))
print(student.get("subjects")) #dict.get() method
print(student)


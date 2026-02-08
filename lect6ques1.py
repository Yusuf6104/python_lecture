# wap to print the length of a list.(list is the parameter)
list= [1,2,3,4,5,6]
heroes = ["thor","ironman","spiderman"]
def cal_len(list): # parameter
     print(len(list))

cal_len(heroes)    

def print_list(list):
     for item in list:
       print(item, end=" ")   

print_list(list)
print()
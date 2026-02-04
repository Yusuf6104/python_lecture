nums = (1,4,9,16,25,36,49,64,81,100)
x = 9
# traverse tuple
idx = 0
while idx < len(nums):
     if(nums[idx]== x):
         print("FOUND at idx", idx)
         break #break
     else:     
        print("finding..") 
        idx += 1
print("end of loop")        
        
 
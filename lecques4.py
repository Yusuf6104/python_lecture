#wap to find the greatest 0f 3 numbers entered by user.
num1 = int (input("enter the first no:"))
num2 = int (input("enter the second no:"))
num3 = int (input("enter the third no:"))
if(num1 >= num2 and num1>=num3):
   print("the greatest no:",num1)
elif(num2 >= num1 and num2>=num3 ):
    print("the greatest no:",num2)
elif(num3 >= num1 and num3>=num2):
     print("the greatest no:",num3)
   

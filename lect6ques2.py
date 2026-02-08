# Waf to find the factorial of n.(n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)    
cal_fact(5)


#waf to convert usd to ind

def cal_inr(usd_val):
     inr_val= usd_val *91.87
     print(usd_val,"USD=",inr_val,"INR")
cal_inr(58)     
                        


#waf to input n number to print in string odd or even 

i = 0
def print_num(n):
    for i in range(1,n*1):
        if(i == n/2):
            print(str,"EVEN")
            break
    else:
        print(str,"ODD")
        

print_num(n= int(input("enter no:",)))

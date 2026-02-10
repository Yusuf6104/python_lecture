# recurrsion (work on call stack )
# recursive function
def show(n):
    if(n == 0): #base case
        return
    print(n)
    show(n-1)
    print("END")

show(3)   
 



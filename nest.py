light = "red"

if(light=="red"):
    if(light=="blinking"): #nesting
        print("go")
    else:
        print("stop")    
elif(light=="green"): #if first statement is false
    print("go")
elif(light=="yellow"):
    print("wait") #indentation{}:proper spacing       
else:
    print("traffic light is off")    
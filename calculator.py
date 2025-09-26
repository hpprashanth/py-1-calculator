def add(a,b):
    return a+b 

def sub(a,b):
    return a-b 

def mul(a,b):
    return a*b 

def div(a,b):
    if b==0:
        return "Error: Division By Zero"
    return a/b 

op=input()
a=float(input())
b= float(input())

if op=="+":
    result= add(a,b)
elif op=="-":
    result= sub(a,b)
elif op=="*":
    result= mul(a,b)
elif op=="/":
    result = div(a,b) 
else:
    result= 'Enter valid input'  

print("Result :", result)                 
d={}
n=int(input("Enter the number of key value pairs:"))

for i in range(n):
    
    key=input("Enter key:")
    value=input("Enter value:")
    
    d[key]=value
    
    print("user defined dictionary:",d) 
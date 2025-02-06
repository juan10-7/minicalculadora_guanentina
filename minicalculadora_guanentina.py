import math
x=int(input("ingrese un numero : "))

y=int(input("ingrese otro numero: "))

opc=int(input("ingrese una opc: "))

##procesing

if opc==1:
    r=(x+y) 

if opc==2:
    r=(x-y) 

if opc==3:
    r=(x*y) 

if opc==4:
    r=(x/y) 

if opc==5:
    r=(x**y) 

if opc== 6:
    r = math.log(x,y) 

# output

print("resultado:"+str(r))








#salary
basic=int(input("Enter the basic salary : "))
if basic >=30000:
    hra=(85*basic)/100
    da=(89*basic)/100
elif basic<=20000:
     hra=(76*basic)/100
     da=(78*basic)/100
else:
    hra=(79*basic)/100
    da=(82*basic)/100
gross=basic+hra+da
print("your gross salary : ",gross)
   


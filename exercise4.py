#code with harry pattern printing exercise
num= int(input("enter number of lines= "))

num2= int(input("any number= "))
num3= bool(num2)
if num3==True:
    for i in range(0,num+1):
        print("*"*i)
elif num3==False:
    for i in range(num,0,-1):
        print("*"*i)



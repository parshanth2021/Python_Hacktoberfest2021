# code with harry if else practice
Age= int(input("Enter your age= "))

if Age<18:
    print("you are under 18, you can't drive")
    
elif Age==18:
    print("you are 18, we will consider after examination you can drive or not")
elif Age<7:
    print("not a valid age")
elif Age>100:
    print("not a valid age")
else :
    print("you can drive")

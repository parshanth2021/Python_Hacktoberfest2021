#modules- random module and its functions

import random
#random()
a=random.random()
print("a=",a)

#randint()
b= random.randint(1,1000)
print("b= ",b)

#randrange()
c= random.randrange(1,20,2)
print("c= ",c)

#choice()
d= random.choice("knowlegde")
print("d= ",d)

#shuffle
numbers= [23,12,56,78,65,54,90,60]
random.shuffle(numbers)
print("e= ",numbers)


class Employee :
    no =4
    pass
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
    def toprint(self):
        return ("name is" ,self.name ,"age is", self.age ,"pay is", self.pay)

    @classmethod   # do use @
    def change_no(cls, new_no):
        cls.no = new_no

harry= Employee("harry",21,321)
larry= Employee("larry",22,432)
parry= Employee("parry",23,543)

print(harry.toprint())
#phle instance variable me dhundega agr nhi mila to class variable p jaega...."no" is class variable.."name/pay/age are instance variable....harry/larry/parry are objects
#we can print "no" by calling harry/larry/parry also
print(harry.no)
print(Employee.no)
harry.no=6
print("______")
print(harry.no)
print(larry.no)
print(parry.no)
print(Employee.no)
#but if we try to chnge the value of "no" by calling objects then it will not get chnged it will create a new attribute
#we can chnge the value of "no" using class only
Employee.no=8
print("______")
print(harry.no)
print(larry.no)
print(parry.no)
print(Employee.no)
print("______")
#now we can change value of class variable by any instance using class method...(harry vala chnge nhi hoga bcz humne esko phele hi nya variable bna dia...
# ar phele hmesha instance variable m dhundta h..bd m class vale m)
harry.change_no(45)
print("_____")
print(harry.no)
print(larry.no)
print(parry.no)
print(Employee.no)






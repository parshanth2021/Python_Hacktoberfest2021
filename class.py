class Employee :
    no =4
    pass
    def toprint(self):
        return ("name is" ,self.name ,"age is", self.age ,"pay is", self.pay)
harry= Employee()
larry= Employee()
parry= Employee()
parry.name="parry"
harry.name="harry"
larry.name="larry"
parry.age=23
harry.age=24
larry.age=25
parry.pay=234
harry.pay=235
larry.pay=236
print(harry.toprint())





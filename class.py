# class person:
#     name = 'abc'
#     gender= 'male'
     
#     def showinfo(self):
#         print('Name: ', self.name )
#         print('gender: ', self.gender)

# p1=person()
# p1.showinfo()
class person:
    counter=0
    def __init__(self, a='Ravi', b= 'male'):
        self.name= a
        self.gender= b
        person.counter= person.counter+1
    def showinfo(self):
        print('Name: ', self.name)
        print('Gender: ', self.gender)
    @classmethod
    def showcount(cls):
        print('No. of persons so far= ', cls.counter)
p1= person('sophie', 'female')
p1.showinfo()
p2= person('stefen', 'male')
p2.showinfo()
p3= person()
p3.showinfo()
person.showcount()
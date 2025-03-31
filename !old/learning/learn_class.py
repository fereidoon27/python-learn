class person :
    count = 0
    # init method or constructor 
    def __init__(self , name , age ):
        # سلف همیشه به خود اون اینستنسه اشاره میکنه، (مثلا جادی)
        # class variable رو همه‌ی نمونه ها میبینن و براشون مشترکه
        self.age = age
        self.name = name 
        person.count += 1
    # Sample Method
    def get_age(self) :
        print ('age is : %s ' % self.age)
    def get_name(self):
        print ('age is : %s ' % self.name)
    def birthday(self) :
        self.age += 1
        print ('happy bithday man your age is : %s'  % self.age)
        
class daneshjoo(person) :
    pass


arash = person ( 'arash' , 20 )
mahdi = person ('mahdi' , 25)
print (arash.age)   
arash.get_age()
arash.birthday() 


# arash.color = 'black'
# print (arash.color)

sima = daneshjoo('sima', 28 )
sima.get_age()
print (person.count)


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

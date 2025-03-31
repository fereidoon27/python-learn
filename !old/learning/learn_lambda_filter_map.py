from operator import itemgetter, attrgetter
def myFunc(dic):
  return dic['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'VW', 'year': 2011},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
       ]

cars.sort(key = myFunc)
print('1: sort by year : '.ljust(50) , cars)

#lambda function#
a=[ (5,10) , (20,1) , (4,3) , (15,14)]
a.sort(reverse=1 , key = lambda x : x[1])
print('2: sort by second element : '.ljust(50) ,a)

car = ['Ford', 'Mitsubishi', 'BMW', 'VW']
car.sort(reverse=True, key= lambda x : len(x))
print('3: sort by length_name : '.ljust(50) ,car)

print('-' * 50)
#map(functions_to_apply, list_of_inputs)
z = list( map(lambda x: x*2 , a  ) ) 
print('4: map effect *2 : '.ljust(50) ,z)

zz = list( map(lambda x: x*2 , [1,2,3,4,5]  ) ) 
print('5: map effect *2 : '.ljust(50) , zz)

##funny if :
zzz=list ( map( lambda x: 'big' if x>5 else 'small' , zz))
print('6: map biig : '.ljust(50) , zzz)

#filter
zzzz=list(filter( lambda x:   x % 3 == 1  , zz))
print('7: filter (mode 3 == 1) : '.ljust(50) , zzzz)


###example1
print('-' * 50)
print ('example 1: ')

student_tuples = [
     ('john', 'A', 15),
     ('aane', 'B', 12),
     ('zave', 'B', 10),
     ('pare', 'z', 20),
     ('namw', 'y', 16)
                 ]
#metod 2 that we can use : key=lambda student: student[0]
sor = sorted( student_tuples ,  key=itemgetter(0) , reverse = 1  )   # sort by age
print ('9: sorted student tuple by name is : '.ljust(50) , sor)

sor = sorted( student_tuples,  key=itemgetter(1,2))   # sort by age
print ('10: sorted student tuple by grade then age : '.ljust(50) , sor)

###example2
print('-' * 50)
print ('example 2: ')

lis = [{"name": "zivar", "age": 20},
       {"name": "ali", "age": 20},
       {"name": "samad", "age": 19}]
 
# using sorted and itemgetter to print list sorted by age
print ("sorting by age: ".ljust(50) ,  sorted(lis, key=itemgetter('age')) )
# notice that "Manjeet" now comes before "Nandini" in next print 
print ("sorting by age and name: ".ljust(50) , sorted(lis, key=itemgetter('age', 'name')))
print ("sorting by age in descending order: ".ljust(50) , sorted(lis, key=itemgetter('age'), reverse=True)) 

print('-' * 50)
print ('example 3: ')
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
         return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 22),
    Student('dave', 'B', 9),
]

print ('sorting student_objects by age reversed'.ljust(50) ,sorted(student_objects, key=attrgetter('age'), reverse=True))

# SAME OUTPUT FOR 2 LINE BLOW:
my_list = [1,2,3,4,5,6,7,8,9]
list4 = [i for i in my_list if i % 2 != 0 ]
list3 = list(filter(lambda i :   i % 2 != 0   , my_list ))

print (list4)
print (list3)
from bdb import GENERATOR_AND_COROUTINE_FLAGS
import csv
from statistics import mean 
with open('C:\\Users\Mohammad Amin\Documents\\0VSC\\grade.csv') as f:
    reader = csv.reader(f)
    for row in reader : 
        name=row[0]
        grade_list=[]
        for grade in row [1:]:
            grade_list.append(int(grade))
        
        print ('name is %10s and average is %5.2f' % (name ,mean(grade_list) ) )

import csv

count_of_std=0
suum=[]
average=[]
with open('c:\\Users\Mohammad Amin\documents\\0vsc\\grade.csv') as f:
    reader=csv.reader(f)
    with open ('d:\\averageeeee.csv' , 'w' , newline='') as outfile :
        writer = csv.writer(outfile)
        for row in reader:
            name=row[0]
            new_sum=0
            new_ave=0
            count_of_grades=0
            for i in row[1:]:
                new_sum+=int(i)
                count_of_grades+=1
            
            suum.append(new_sum)
            new_ave=suum[count_of_std]/count_of_grades
            average.append(new_ave)
            
            print('sum of "%10s" grade is "%5i" and average is "%5.2f" ' %(name , suum[count_of_std] ,average[count_of_std] ))
            count_of_std+=1
            writer.writerow( name  )
            #outfile.close()
            
            



            

        
        

        

        
import random
random.seed()


our=int(input(" adade to bede aan agha: "))
y=random.randint(1,100)
print("computer guess your num is: ",y)
min_y=0
max_y=100

while y !=our :
    if y<our:
        min_y=y
        print("adade man bozorg tar az hads pc ast")
        y=random.randint(min_y+1 , max_y-1)
        print("new computer guess your num is: ",y)
    else:
        max_y=y
        print("adade man koochik tar tar az hads pc ast")
        y=random.randint(min_y+1 , max_y-1)
        print("new computer guess your num is: ",y)

print ("you did it man , my number was: ", our)
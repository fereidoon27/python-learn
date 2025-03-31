arr_size = input()
boundaries = input()

i = int(boundaries.split(" ")[0])
end = int(boundaries.split(" ")[1])

inputdata = input()

result = 0

while (i < end):
    if (inputdata[2*i] == inputdata[2*i + 2]):
        result = result + 1
    i = i + 1
print(result)
nq = list (map (int, input().split(' ') ) )
n , q = nq


### test 
# 8 6
# 3 2 5
# 1 2 5
# 3 2 5
# 2 4 7
# 2 1 2
# 3 1 7
# n = 8 
# q = 6
keys = set()
for i in range (1,n+1):
    keys.add(i)
### type1
# graph = dict.fromkeys(keys, None)
### type2
# graph = {}
# for i in keys:
#     graph[i] = None
### type3
graph = dict([(key, set() ) for key in keys])
# print (graph)

for i in range (q) :
    opp = list (map (int, input().split(' ') ) )
    op = opp[0]
    x = opp[1]
    y = opp[2]

    if op == 1 :
        graph[x].add(y)
        graph[y].add(x)  
        graph[x].update(list(graph[y]))
        graph[y].update(list(graph[x]))

        for j in graph[x] :
            graph[j].update(list(graph[x]))

        # for k in graph[y] :
        #     graph[k].update([graph[y]])
         

    elif op == 2 :
        # l = opp[1]
        # r = opp[2]
        x = opp[1]
        y = opp[2]
        graph[x].add(y)
        graph[y].add(x)  
        graph[x].update(list(graph[y]))
        graph[y].update(list(graph[x]))

        temp_list = list(range(x, y+1))

        for k in range (x , y+1):
            graph[k].update(temp_list)
            # graph[k].remove(k)

            for z in graph[k] :
                graph[z].update(list(graph[k]))


    elif op == 3 :
        if opp[2] in graph[opp[1]] :
            print ('YES')
        else :
            print ('NO')
    # print ('stage %s : ' , i, graph)




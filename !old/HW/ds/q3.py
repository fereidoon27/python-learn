from collections import defaultdict

graph = defaultdict(list)
final_DFS_comp = defaultdict(list)
vertexes = set()
   
def add_edge(s, d, gr, ver):
    # global graph, vertexes
    gr[s].append(d)
    ver.update([s])
nm = list (map (int, input().split(' ') ) )
n = nm[0]
m = nm[1] 

for i in range (m):
    # b = list(map(lambda x : x - 1 , a))
    new_edge = list (map (int , input().split(' ')))
    add_edge(new_edge[0], new_edge[1],graph, vertexes )

def DFS (gra , sort_ver ):  

    starting_time , finishing_time = 0 , 0
    timing = defaultdict(list)
    parent = defaultdict(list)

    def visit (s) :
        nonlocal starting_time , finishing_time 
        starting_time += 1
        timing[s].append(starting_time)
        for v in gra[s]:
            if v not in parent:
                parent[v] = s
                # final_DFS_comp[counter_component].append(v)
                visit(v)
        finishing_time += 1
        timing[s].append(finishing_time)

    # counter_component = 0
    for s in list(sort_ver):
        if s not in parent:
            # counter_component += 1
            # final_DFS_comp[counter_component] = [s]
            parent[s] = None
            visit(s)
    # timing = {1: [1, 4], 4: [2, 2], 5: [3, 1], 3: [4, 3], 2: [5, 5]}
    # timing = {1: [1, 3], 2: [2, 2], 3: [3, 1]}

    l =[]
    for k in timing :
        l.append([k, timing[k][1]])  
    
    # format final_res : [ number of component : [number of nodes wich is member in component ] ]
    return  l , dict(parent)
print ('NO')
def DFS2 (gra , sort_ver ):  
    parent = defaultdict(list)
    def visit (s) :
        for v in gra[s]:
            if v not in parent:
                parent[v] = s
                final_DFS_comp[counter_component].append(v)
                visit(v)

    counter_component = 0
    for s in list(sort_ver):
        if s not in parent:
            counter_component += 1
            final_DFS_comp[counter_component] = [s]
            parent[s] = None
            visit(s)
    # timing = {1: [1, 4], 4: [2, 2], 5: [3, 1], 3: [4, 3], 2: [5, 5]}
    # timing = {1: [1, 3], 2: [2, 2], 3: [3, 1]}
    
    # format final_res : [ number of component : [number of nodes wich is member in component ] ]
    return  final_DFS_comp , dict(parent)


def transpose(gra):
    gt = defaultdict(list)
    ver_gt = set()
    # self.Sort(list(dict(self.DFS()[0]).values()))
    for i in gra:
        for j in gra[i]:
            add_edge(j, i, gt, ver_gt )
    return gt

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of sublist lambda has been used
    sub_li.sort(key = lambda x: x[1], reverse = 1)
    return sub_li

# n=3
# cost = [1, 2, 3]
# m = 3
# add_edge(1, 2, graph, vertexes)
# add_edge(2, 3, graph, vertexes)
# add_edge(3, 2, graph, vertexes)

# n=5
# cost = [ 2, 8, 0, 6, 0]
# m = 6
# add_edge(1, 4, graph, vertexes)
# add_edge(1, 3, graph, vertexes)
# add_edge(2, 4, graph, vertexes)
# add_edge(3, 4, graph, vertexes)
# add_edge(4, 5, graph, vertexes)
# add_edge(5, 1, graph, vertexes)

# ###test3
# n , m = 4 , 2
# cost = [100, 2 , 200, 10]
# add_edge(1, 2, graph, vertexes)
# add_edge(4, 3, graph, vertexes)




# print (transpose(graph))

# final_res = list(DFS(graph, vertexes))
# print ('final_res: ' ,final_res)
# start_finish = Sort(final_res[0])

# print ('start_finish: ' , start_finish)
# sorted_sf = [el[0] for el in start_finish]
# print ('sorted_sf: ', sorted_sf)

# tr_gra = transpose(graph)
# print ('transpose(graph): ' ,tr_gra)
# final_res = list(DFS2(tr_gra, sorted_sf))
# print ('final_res2: ' ,final_res)

# print (list(final_DFS_comp.values()))


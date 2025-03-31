from collections import defaultdict


class Graph:
    def __init__(self, vertex):       
        self.V = vertex
        self.graph = defaultdict(list)
        self.vertexes = set()
        self.final_DFS_comp = defaultdict(list)
        self.final_DFS_STRONGLY_Ccomp = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)
        self.vertexes.update([s, d])

    def func_vertex1(self) :
        self.c=set()
        for i in self.graph.values() :
            self.c.update(i)
        self.c = set (self.graph.keys()) | self.c
        return (self.c)       
    def func_vertex2(self) :
        verrrr=set()
        for i in self.graph.values() :
            verrrr.update(i)
        verrrr = set (self.graph.keys()) | verrrr
        return (verrrr)

    def DFS (self ):
        
        Adj =   self.graph
        starting_time , finishing_time = 0 , 0
        timing = defaultdict(list)
        parent = defaultdict(list)

        def visit (s) :
            nonlocal starting_time , finishing_time 
            starting_time += 1
            timing[s].append(starting_time)
            for v in Adj[s]:
                if v not in parent:
                    parent[v] = s
                    self.final_DFS_comp[counter_component].append(v)
                    visit(v)
            finishing_time += 1
            timing[s].append(finishing_time)

        counter_component = 0
        for s in list(Adj.keys()):
            if s not in parent:
                counter_component += 1
                self.final_DFS_comp[counter_component] = [s]
                parent[s] = None
                visit(s)
        # a = {1: [1, 4], 4: [2, 2], 5: [3, 1], 3: [4, 3], 2: [5, 5]}

        l =[]
        for k in timing :
            l.append([k, timing[k][1]])  

        return [l , dict(parent)]

    def DFS2 (self, sorted_time):
        
        # Adj =   self.graph
        Adj = (self.transpose().graph)
        print ('Adj is : ', Adj)
        parent = defaultdict(list)

        def visit (s) :
            for v in Adj[s]:
                print ('v and parent is : ', v, parent)
                if v not in parent:
                    parent[v] = s
                    self.final_DFS_comp[counter_component].append(v)
                    visit(v)

        counter_component = 0
        for s in sorted_time:
            if s[0] not in parent:
                counter_component += 1
                self.final_DFS_comp[counter_component] = [s[0]]
                parent[s[0]] = None
                visit(s[0])

        return dict(self.final_DFS_comp) , dict(parent)



    # transpose the matrix
    def transpose(self):
        gt = Graph(self.V)
        # self.Sort(list(dict(self.DFS()[0]).values()))

        for i in self.graph:
            for j in self.graph[i]:
                gt.add_edge(j, i)
        return gt

    
    # Python code to sort the tuples using second element of sublist Inplace way to sort using sort()  
    def Sort(self,sub_li):
        # reverse = None (Sorts in Ascending order)
        # key is set to sort using second element of sublist lambda has been used
        sub_li.sort(key = lambda x: x[1], reverse = 1)
        return sub_li
        

    def scc(self):
        # gt = self.transpose()
        # start_finish = self.Sort(list(dict(self.DFS()[0]).values()))
        start_finish = self.Sort(self.DFS()[0])
        # print ('start_finish is :' , start_finish)

        return self.DFS2(start_finish)
        
# n = int (input())
# cost = list (map (int, input().split(' ') ) )
# m = int (input())   
# g = Graph(n)

# for i in range (m):
#     # b = list(map(lambda x : x - 1 , a))
#     new_edge = list (map (int , input().split(' ')))
#     g.add_edge(new_edge[0], new_edge[1])




# n=3
# g = Graph(n)
# cost = [1, 2, 3]
# m = 3
# g.add_edge(1, 2)
# g.add_edge(2, 3)
# g.add_edge(3, 2)

# n=5
# g = Graph(n)
# cost = [ 2, 8, 0, 6, 0]
# m = 6
# g = Graph(n)
# g.add_edge(1, 4)
# g.add_edge(1, 3)
# g.add_edge(2, 4)
# g.add_edge(3, 4)
# g.add_edge(4, 5)
# g.add_edge(5, 1)


####test3
n , m = 4 , 2
cost = [100, 2 , 200, 10]
g = Graph(n)
g.add_edge(1, 2)
g.add_edge(4, 3)

# print(dict(g.graph))

# print (g.final_DFS_comp)

# print (list(g.scc()[0].values()))
# print (g.transpose().graph())
# g.scc()
print (g.scc())
#### format final_res : [ number of component : [number of nodes wich is member in component ] ]
final_res = list(g.scc()[0].values())
print (final_res)
final_cost = 0

for entry in final_res :
    min =  float('inf')
    for i in entry :
        # print ('cost[%i-1]:%i ' %(i , cost[i-1]))
        if cost[i-1] < min :
            min = cost[i-1]
            # print ('min is : ' , min)
        
    final_cost += min 
# print (final_res)
print (final_cost)

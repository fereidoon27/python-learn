# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:
    finalscc = defaultdict(list)
    counter_scc = 0

    def __init__(self, vertex):
        
        self.V = vertex
        self.graph = defaultdict(list)
        # self.finalscc = defaultdict(list)
        # self.counter_scc = 0

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)
        
    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        # print(d, end='')
        
        # self.finalscc[self.counter_scc].append(d)
        # print (dict(self.finalscc))
        Graph.finalscc[Graph.counter_scc].append(d)

        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

        # self.counter_scc += 1
        # print (list(self.finalscc.values()))

        Graph.counter_scc += 1
        # print (list(Graph.finalscc.values()))



    def fill_order(self, d, visited_vertex, stack):
        
        # Mark the current node as visited 
        visited_vertex[d] = True
        #Recur for all the vertices adjacent to this vertex
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)
        # print('stack is :' , stack)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                # print("")
                

    def get_values (self):
        # print (self.finalscc.values())
        # print ('----------' , list(Graph.finalscc.values()))
        return list(Graph.finalscc.values())

                
                # print ('counter_scc: ' , self.counter_scc)
                # print (self.finalscc)

# n = int (input())
# cost = list (map (int, input().split(' ') ) )
# m = int (input())   
# g = Graph(n)

# for i in range (m):
#     # b = list(map(lambda x : x - 1 , a))
#     new_edge = list (map (int , input().split(' ')))
#     g.add_edge(new_edge[0]-1, new_edge[1]-1)

# n=3
# g = Graph(n)
# cost = [1, 2, 3]
# m = 3
# g.add_edge(0, 1)
# g.add_edge(1, 2)
# g.add_edge(2, 1)

n=5
g = Graph(n)
cost = [2, 8, 0, 6, 0]
m = 6
g = Graph(n)
g.add_edge(0, 3)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 0)


# print("Strongly Connected Components:")
g.print_scc()
lalala = g.get_values()
# print (lalala)

sum_cost = 0
for i in lalala :
    list_cost = []
    for j in i :  
        # print(list_cost) 
        list_cost.append(cost[j])
    sum_cost += min (list_cost)

print (sum_cost)
# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# https://codebunk.com/b/3071100684234/

'''

Connected Components in an Undirected Graph

Given an undirected graph, the task is to print all the connected components line by line. 

'''


class graph:
    def __init__(self, val=0, neighbors=[]):
         self.val = val
         self.neighbors = neighbors
         self.visited = False

def add_edge(adj, t, f):
    adj[t].append(f)
    adj[f].append(t)

'''def dfs(node):
node.visited = True
    if not node:
        return
    print (node.val)
    if node.neighbors:
        for n in node.neighbors:
            if not n.visted:
                dfs(n)'''
                
def dfs(adj, visited, s):
    visited[s] = True
    print (s)
    
    for i in adj[s]:
        if not visited[i]:
            dfs(adj, visited, i)

node_1 = graph(4)
node_2 = graph(5)
arr = [node_1]
node_3 = graph(2, arr)
arr = [node_2]
node_4 = graph(3, arr)
root = graph(1, [node_3, node_4])

edges = [[1, 2], [1, 3], [2, 0], [2, 3], [3, 4]]

adj = [[] for _ in range(5)]
visited = [False for _ in range(5)]

for e in edges:
    add_edge(adj, e[0], e[1])

print (adj)
    
dfs(adj, visited, 1)

#dfs(root)

'''

1----2----0
|    /
|   /
|  /
3/-------4'''

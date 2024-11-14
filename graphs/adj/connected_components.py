'''
Connected Components in an Undirected Graph:

1---0      3
|	       |
|	       |
2          4
Should print: {0,1,2} and {3,4}
'''
from collections import deque

def add_to_edge(adj, l, r):
    # Undirected
    adj[l].append(r)
    adj[r].append(l)


def dfs(adj, unvisited, n, cur_arr):
    if n is None:
       return
    cur_arr.append(n)
    for a in adj[n]:
       if  a in unvisited:
           unvisited.remove(a)
           dfs(adj, unvisited, a, cur_arr)

num = 5
edges = [[0,1], [1,2], [3,4]]
adj = [[] for _ in range(num)]
unvisited = set([r for r in range(num)])
curr_arr = []
for e in edges:
    add_to_edge(adj, e[0], e[1])

q = deque()
q.append(unvisited.pop())
while q:
   dfs(adj, unvisited, q.popleft(), curr_arr)
   if unvisited:
      print (curr_arr)
      curr_arr = []
      q.append(unvisited.pop())
if curr_arr:
   print (curr_arr)




from collections import defaultdict

def dfs(graph, source, n):
    distances = [-float("inf") for _ in range(n)]
    parents = [-1 for _ in range(n)]
    def traverse(node, parent, dist):
        parents[node] = parent
        distances[node] = dist
        
        for nb, weight in graph[node]:
            if nb == parent:
                continue
            traverse(nb, node, dist + weight)
            
    traverse(source, -1, 0)
    return distances, parents

# Input edges
edges = [
    (1, 2, 3),
    (2, 3, 4),
    (4, 5, 2),
    (4, 6, 3),
    (2, 4, 6),
]

adjacency_list = defaultdict(list)

for u, v, w in edges:
    adjacency_list[u].append((v, w))
    adjacency_list[v].append((u, w))  
    
n = len(edges) + 2
    
d, p = dfs(adjacency_list, 1, n )
f_node1 = d.index(max(d))
d1, p1 = dfs(adjacency_list, f_node1, n)
f_node2 = d1.index(max(d1))



curr_node = f_node2

ans = []


while curr_node != -1:
    ans.append(curr_node)
    curr_node = p1[curr_node]
print(ans)
    





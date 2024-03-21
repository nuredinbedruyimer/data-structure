from collections import defaultdict, deque

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = self.build_graph()
    def build_graph(self):
        graph = defaultdict(list)
        for u, v in self.edges:
            
            graph[u].append(v)
            graph[v].append(u)
        return graph
    def bfs(self, source):
        bfs_arr = []
        queue = deque([source])
        visted = set()
        visted.add(source)
        
        while queue:
            curr_node = queue.popleft()
            bfs_arr.append(curr_node)
            for nb in self.graph[curr_node]:
                if nb not in visted:
                    visted.add(nb)
                    queue.append(nb)

        return bfs_arr
    
    



if __name__== "__main__":
    
 edges = [
  [1, 2],
  [1, 3],
  [2, 4],
  [2, 5],
  [3, 6],
  [4, 5],
  [5, 6]
]
ob = Graph(edges)
print(ob.bfs(1))
            
        
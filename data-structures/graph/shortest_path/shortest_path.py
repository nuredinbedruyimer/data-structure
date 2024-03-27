from heapq import heapify, heappop, heappush

def shortest_path(graph, start, n):
    distance = [float("inf") for _ in range(n)]
    
    distance[start] = 0
    min_heap = [(0, start)]
    
    
    while min_heap:
        curr_dist , curr_node = heappop(min_heap)
        
        if curr_dist > distance[curr_dist]:
            continue
        for nb , weight in graph[curr_node]:
            if curr_dist + weight < distance[nb]:
                distance[nb] = curr_dist + weight
                heappush(min_heap, (curr_dist + weight, nb ))
                
    return distance
graph = [
    [(1, 4), (2, 1)], 
    [(3, 1)],          
    [(1, 2), (3, 5)],  
    []                
]


print(shortest_path(graph, 0, 6))

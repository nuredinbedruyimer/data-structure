from collections import defaultdict, deque


test = int(input())


for _ in range(test):
    n = int(input())
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        u -= 1
        v-= 1
        graph[u].append(v)
        graph[v].append(u)
        
    # do some Bfs and fin the value of all level width and take the top 2
    
    
    level_lengths = []
    
    queue = deque([0])
    
    visted = set()
    visted.add(0)
    
    while queue:
        size = len(queue)
        
        for _ in range(size):
            curr_node = queue.popleft()
            
            for nb in graph[curr_node]:
                if nb not in visted:
                    queue.append(nb)
                    visted.add(nb)
        level_lengths.append(size)
    level_lengths.sort()
    
    ans = level_lengths[-1] + level_lengths[-2]
    
    if sum(level_lengths) <= 2:
        print(0)
    else:
        print(ans)
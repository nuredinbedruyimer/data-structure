import sys
from collections import deque

def solve():
    q = int(sys.stdin.readline().strip())
    
    for _ in range(q):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))
        
        a.insert(0, 0)  # To match 1-based indexing
        dq = deque()
        f = [0] * (n + 1)
        
        mex = 0
        total_sum = 0
        
        for i in range(1, n + 1):
            f[a[i]] += 1
            while mex < len(f) and f[mex]:
                mex += 1
            dq.append((mex, 1))
            total_sum += mex
        
        ans = total_sum
        
        for i in range(1, n):
            me = [a[i], 0]
            total_sum -= dq[0][0]
            dq[0] = (dq[0][0], dq[0][1] - 1)
            if dq[0][1] == 0:
                dq.popleft()
            
            while dq and dq[-1][0] >= a[i]:
                total_sum -= dq[-1][0] * dq[-1][1]
                me[1] += dq[-1][1]
                dq.pop()
            
            dq.append(tuple(me))
            total_sum += me[0] * me[1]
            dq.append((n, 1))
            total_sum += n
            ans = max(ans, total_sum)
        
        print(ans)

if __name__ == "__main__":
    solve()
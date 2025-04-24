from bisect import bisect_right

def solve():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    intelligence_list = []
    strength_list = []

    prev_row = [0] * (m + 1)
    curr_row = [0] * (m + 1)
    
    total_score = 0

    for curr_value in arr:
        if curr_value == 0:
            intelligence_list.sort()
            strength_list.sort()
            total_score += 1

            for strength in range(total_score + 1):
                if strength != 0:
                    pass_intelligence = bisect_right(intelligence_list, strength - 1)
                    pass_strength = bisect_right(strength_list, total_score - strength)
                    pass_count = pass_intelligence + pass_strength
                    curr_row[strength] = max(prev_row[strength - 1] + pass_count, curr_row[strength])
                
                if total_score > strength:
                    pass_intelligence = bisect_right(intelligence_list, strength)
                    pass_strength = bisect_right(strength_list, total_score - strength - 1)
                    pass_count = pass_intelligence + pass_strength
                    curr_row[strength] = max(prev_row[strength] + pass_count, curr_row[strength])
            
            intelligence_list.clear()
            strength_list.clear()
            prev_row, curr_row = curr_row, [0] * (m + 1)  # Swap and reset current row

        elif curr_value > 0:
            intelligence_list.append(curr_value)
        else:
            strength_list.append(-curr_value)

    ans = 0
    intelligence_list.sort()
    strength_list.sort()

    for curr_value in range(m + 1):
        pass_intelligence = bisect_right(intelligence_list, curr_value)
        pass_strength = bisect_right(strength_list, m - curr_value)
        ans = max(ans, prev_row[curr_value] + pass_intelligence + pass_strength)
    
    print(ans)

if __name__ == "__main__":
    solve()

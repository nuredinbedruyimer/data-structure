test = int(input())

for _ in range(test):
    p, m, f = list(map(int, input().split()))
    problems  = list(map(int, input().split()))
    models = list(map(int, input().split()))
    functions = list(map(int, input().split()))
    #  it have motre than one max diff we can ot do anything
    
    models.sort()
    functions.sort()
    
    #  find the max_diff
    
    max_diff = 0
    start_index = -1 
    
    
    for index in range(1, p):
        curr_diff = problems[index] - problems[index - 1]
        
        if curr_diff > max_diff:
            max_diff = curr_diff
            start_index = index - 1
    
    #  the we can fid the optimal minimization between the two larger one
    
    #  find thing which nearest to the target value
    
    target = (problems[start_index] + problems[start_index + 1]) // 2
    
    
    min_diff = max_diff
    for model in models:
        #  find the remaining thing from the functions one
        
        low = 0
        high = f - 1
        
        while high > low  + 1:
            take_index = (low + high) // 2
            function_value = functions[take_index]
            
            if function_value + model < target:
                low = take_index
            else:
                high = take_index
                
        max_radius1 = max(problems[start_index + 1] - (model + functions[low]), (model + functions[low])- problems[start_index])
        max_radius2 = max(problems[start_index + 1] - (model + functions[high]), (model + functions[high])- problems[start_index])

        min_diff = min(min_diff, max_radius1, max_radius2)
    for i in range(1, p):
        if i != start_index + 1:
            min_diff = max(min_diff, problems[i] - problems[i - 1])
    
    print(min_diff)
        
        
        
        
    
test = int(input())

for _ in range(test):
    n, m, k = list(map(int, input().split()))
    mrr = list(map(int, input().split()))
    krr = list(map(int, input().split()))
    all_questions = [i for i in range(1, n + 1)]
    unknown_question = []
    
    for question in all_questions:
        if question not in krr:
            unknown_question.append(question)
    
    #  case one
    ans = ""
    if len(unknown_question) >= 2:
        for _ in range(m):
            ans += "0"
    elif len(unknown_question) == 0:
        for _ in range(m):
            ans += "1"
    else:
        for ques in all_questions:
            ans += "1" if ques == unknown_question[0] else "0"
    print(ans)
            
        
            
    
    

                
                    
            
        
            
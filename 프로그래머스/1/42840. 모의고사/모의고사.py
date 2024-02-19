def solution(answers):
    one_p = [1, 2, 3, 4, 5]
    two_p = [2, 1, 2, 3, 2, 4, 2, 5]
    three_p = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    
    for idx, ans in enumerate(answers):
        score[0] += (ans == one_p[idx%len(one_p)])
        score[1] += (ans == two_p[idx%len(two_p)])
        score[2] += (ans == three_p[idx%len(three_p)])
    
    max_score = max(score)
    
    return [i+1 for i in range(3) if score[i] == max_score]
    
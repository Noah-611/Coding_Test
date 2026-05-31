def solution(dots):
    def is_parrellel(a,b,c,d):
        x1, y1 = dots[a]
        x2, y2 = dots[b]
        x3, y3 = dots[c]
        x4, y4 = dots[d]
        
        return (y2-y1)*(x4-x3)==(y4-y3)*(x2-x1)
    answer = 0
    if is_parrellel(0,1,2,3):
        answer = 1
    if is_parrellel(0,2,1,3):
        answer = 1
    if is_parrellel(0,3,1,2):
        answer = 1
    
    return answer

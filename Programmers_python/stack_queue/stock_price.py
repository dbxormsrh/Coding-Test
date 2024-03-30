from collections import deque

def solution(prices):
    answer = []
    l = len(prices)
    qprices = deque(prices)

    for i in range(l):
        p = qprices.popleft()
        t = 0
        for i in qprices:
            t += 1
            if p > i:
                break
            
        answer.append(t)
    
    return answer

if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))
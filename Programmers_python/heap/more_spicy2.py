import random
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        if a >= K:
            break
        b = heapq.heappop(scoville)
        
        heapq.heappush(scoville, a + b*2)
        answer += 1

    if heapq.heappop(scoville) < K:
        return -1

    return answer

if __name__ == "__main__":
    scoville = [1,2,3,9,10,12]
    K = 7
    print(solution(scoville, K))

    x = [random.randint(1, 100) for i in range(20) ]
    y = random.randint(min(x), max(x))
    print(x)
    print(y)
    print(solution(x, y))
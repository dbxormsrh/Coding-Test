import random
from queue import PriorityQueue

def solution(scoville, K):
    answer = 0
    pq = PriorityQueue(maxsize = len(scoville))

    for i in scoville:
        pq.put(i)

    while True:
        a = pq.get()
        if a >= K:
            break
        b = pq.get()
        x = a + 2 * b
        if x < K:
            pq.put(x)
            answer += 1
            continue
        else:
            answer += 1
            continue

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
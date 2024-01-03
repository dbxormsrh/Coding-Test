import heapq as hp

def solution(jobs):
    time = 0
    total_time = 0
    len_jobs = len(jobs)

    heap = []

    while (True):
        temp_jobs = jobs.copy()
        if not jobs and not heap:
            break

        for i in temp_jobs: 
            if i[0] <= time:
                hp.heappush(heap, [i[1], i[0]])
                jobs.remove(i)
            
        if not heap:
            time += 1
            continue
        else:
            work = hp.heappop(heap)
            time += work[0]
            total_time = total_time + time - work[1]

    answer = total_time // len_jobs

    return answer

if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]]))
    print(solution([[7, 8], [3, 5], [9, 6]]))   #jobs의 배열이 job의 요청 시간 순으로 정렬이 되어있지 않음을 고려하지 않음.
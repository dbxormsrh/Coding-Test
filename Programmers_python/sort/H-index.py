def solution(citations):
    citations.sort(reverse = True)
    for times in range(max(citations)):
        n = 0
        for i in citations:
            if i >= times:
                n +=1
        if times <= n:
            return times

    return 0


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    citations3 = [6, 5, 3, 3, 0]
    citations2 = [0,0,0,0,0]
    print(solution(citations))
    print(solution(citations2))
    print(solution(citations3))

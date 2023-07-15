def solution(s, N):
    answer = 0
    num_list = []
    subs = ""
    n = []

    for i in range(N):
        n.append(str(i + 1))

    for i in range(len(s) - N + 1):
        ss =s[i:i + N] 
        x = 0
        for j in n:
            if j in ss:
                x += 1
                continue
            else:
                break

        if x == N:
            num_list.append(ss)

    if len(num_list) == 0:
        return -1
    
    for i in num_list:
        if answer < int(i):
            answer = int(i)

    return answer


if __name__ == "__main__":
    print(solution("1451232125", 2))
    print(solution("313253123", 3))
    print(solution("12412415", 4))
def solution(n, lost, reserve):
    cloth = {i+1:1 for i in range(n)}
    for i in lost:
        cloth[i] -= 1

    for i in reserve:
        cloth[i] += 1
    print(cloth)
    for k in cloth.keys():
        if k == 1:
            if cloth[k] == 0 and cloth [k+1] >= 2:
                cloth[k] += 1
                cloth[k+1] -= 1
            continue
        if k == n:
            if cloth[k] == 0 and cloth [k-1] >= 2:
                cloth[k] += 1
                cloth[k-1] -= 1
            continue
        if cloth[k] == 0 and cloth [k-1] >= 2:
            cloth[k] += 1
            cloth[k-1] -= 1
        elif cloth[k] == 0 and cloth [k+1] >= 2:
            cloth[k] += 1
            cloth[k+1] -= 1

    answer = 0
    for _, v in cloth.items():
        if v != 0:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
    print(solution(4, [2, 3], [1,4]))
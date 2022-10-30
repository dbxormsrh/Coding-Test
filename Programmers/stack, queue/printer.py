import random
def solution(priorities, location):
    answer = 0

    while True:
        if location != 0:
            if priorities[0] >= max(priorities):
                priorities.pop(0)
                location -= 1
                answer += 1
            else:
                priorities = priorities[1:] + [priorities[0]]
                location -= 1

        else:
            if priorities[location] == max(priorities):
                return answer + 1
            else :
                priorities = priorities[1:] + [priorities[0]]
                location = len(priorities) - 1

    return answer + 1


if __name__ == "__main__":
    print(solution([2,1,3,2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
    x = [random.randint(1, 100) for i in range(20) ]
    y = random.randint(1, 19)
    print(x)
    print(y)
    print(x[y])
    print(solution(x, y))

def solution(progresses, speeds):
    c = 0
    answer = []
    while True:
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        print(progresses)
        while progresses[c] >= 100:
            c += 1
            try:
                progresses[c]
            except IndexError:
                answer.append(len(progresses))
                return answer

        if c != 0:
            answer.append(c)
            progresses = progresses[c:]
            speeds = speeds[c:]
            c = 0

    return answer

if __name__ == "__main__":
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
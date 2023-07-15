def solution(jobs):
    answer = 0
    l = len(jobs)

    while True:
        min = 0
        sub_list = []
        for i in range(len(jobs)):
            if jobs[min][0] > jobs[i][0]:
                min = i

        for i in range(len(jobs)):
            if jobs[i][0] <= jobs[min_idx][1] + answer:
                sub_list.append[i]

        min_pro = jobs[sub_list[0]][1]
        min_pro_idx = 0

        for i in sub_list:
            if min_pro > jobs[i][1]:
                min_pro = jobs[i][1]
                min_pro_idx = i
        

    return answer



if __name__ == "__main__":
    print(solution([[0, 3], [1, 9], [2, 6]]))
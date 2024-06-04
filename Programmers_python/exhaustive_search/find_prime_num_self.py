from itertools import permutations

def solution(numbers):
    answer = []

    num = [s for s in numbers]
    num_list = set()
    temp = set()

    for i in range(1, len(num) + 1):
        temp.add((permutations(num, i)))

    for l in temp:
        for i in l:
            s = ''
            for a in i:
                s = s + a
            num_list.add(int(s))

    for n in num_list:
        n_share = 0

        if n == 2:
            answer.append(n)
            continue

        if n % 2 == 0:
            continue

        for i in range(1, n, 2):
            if n % i == 0:
                n_share += 1

        if n_share == 1:
            answer.append(n)

    return answer
        
if __name__ == "__main__":
    print(solution("121"))
from itertools import permutations

def solution(numbers):
    str_num = list(map(str, numbers))
    

    while len(str_num):
        n = 9

        print(len(str_num))
        str_num.pop()
    return max(list(map(''.join,permutations(list(map(str, numbers))))))

if __name__ =="__main__":
    numbers = [3, 30, 34, 5, 9]

    print(solution(numbers))
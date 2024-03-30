from itertools import permutations

def solution(numbers):
    return max(list(map(''.join,permutations(list(map(str, numbers))))))

if __name__ =="__main__":
    numbers = [3, 30, 34, 5, 9]

    print(solution(numbers))
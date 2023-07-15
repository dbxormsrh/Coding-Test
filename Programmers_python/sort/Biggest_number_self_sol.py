from itertools import permutations

def solution(numbers):
    for i in numbers:
        if i<0:
            return "negative number in parameter"

    return str(sorted(list(map(''.join,permutations(list(map(lambda x: str(x), numbers))))), reverse=True)[0])

if __name__ =="__main__":
    numbers = [3, 30, 34, 5, 9]

    print(solution(numbers))
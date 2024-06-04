import math
def check_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False

    return True

number_set = set()
def permutation(base, array):       #permutation 통해 가능한 숫자의 set 구함
    if base:
        number_set.add(int(base))

    for i, s in enumerate(array):
        permutation(base + s, array[:i] + array[i+1:])

def solution(numbers):
    answer = 0

    permutation("", list(numbers))

    answer = len(list(filter(check_prime, number_set)))     #filter() 통해 number_set 내에서 prime number 찾기

    return answer
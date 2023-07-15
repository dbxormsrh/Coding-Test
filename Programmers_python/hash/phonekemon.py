def solution(nums):
    answer = 0
    l = len(nums)
    nums_set = set(nums)
    print(nums_set)
    if int(l/2) > len(nums_set):
        answer = len(nums_set)
    else:
        answer = int(l/2)
    return answer


if __name__ == "__main__":
    print(solution([3,1,2,3]))
    print(solution([3,3,3,2,2,4]))
    print(solution([3,3,3,2,2,2]))
from itertools import permutations

def solution(k, dungeons):
    max_num_dun = 0
    cases =  permutations(dungeons, len(dungeons))

    for case in cases:
        num_dun = 0
        temp_k = k
        for req_tire, spend_tire in case:
            if temp_k >= req_tire and temp_k >= spend_tire:
                temp_k = temp_k - spend_tire
                num_dun += 1
                if len(dungeons) == num_dun:
                    return len(dungeons)
            else:
                if max_num_dun < num_dun:
                    max_num_dun = num_dun
                break

    return max_num_dun

print(solution(80, [[80,20],[50,40],[30,10]]))

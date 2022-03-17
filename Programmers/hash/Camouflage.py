def solution(clothes):
    genre = {}
    answer = 1
    for i in range(len(clothes)):
        if clothes[i][1] in genre:
            genre[clothes[i][1]].append(clothes[i][0])
        else:
            genre[clothes[i][1]] = [clothes[i][0]]
    for i in genre:
        answer = answer * (len(genre[i])+1)
    return answer-1

if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

    print(solution(clothes))
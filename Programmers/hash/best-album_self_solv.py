def solution(genres, plays):
    ans = dict()
    answer = list()
    playtime = dict()
    pt_list = list()

    for i in range(len(genres)):
        if genres[i] in ans:
            ans[genres[i]].update({i: plays[i]})
            playtime[genres[i]] += plays[i]
        else:
            ans[genres[i]] = {i:plays[i]}
            playtime[genres[i]] = plays[i]

    sorted_pt = sorted(playtime.items(), key = lambda item: item[0], reverse = True)

    for i in range(len(playtime)):
        x = max(playtime, key = playtime.get)
        playtime.pop(x)
        pt_list.append(x)

    for i in pt_list:
        sorted_ans = sorted(ans[i].items(), key = lambda item: item[1], reverse = True)        
        answer.append(sorted_ans[0][0])
        try:
            answer.append(sorted_ans[1][0])
        except IndexError:
            pass        
    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop", "opera"]
    plays = [500, 600, 150, 800, 2500, 1111]

    print("answer = ", solution(genres, plays))

def solution(word):
    if word == "A":
        return 1
    elif word == "AA":
        return 2
    elif word == "AAA":
        return 3
    elif word == "AAAA":
        return 4
    elif word == "AAAAA":
        return 5
    
    word_map = {"A" : 1, "E" : 2, "I" : 3, "O" : 4, "U" : 5}
    num = 0

    dic = 11111
    idx = 5

    for i in range(len(word)):
        num += word_map[word[i]] * (10 ** (4-i))

    while(dic != num):
        while('0' in str(dic)):
            i = str(dic).find('0')
            dic += 10 ** (4 - i)
            idx += 1
            if dic == num:
                return idx
        dic += 1
        idx += 1

        while('6' in str(dic)):
            i = str(dic).find('6')
            dic += 10 ** (5 - i)
            dic -= 6 * (10 ** (4 - i))

    return idx


if __name__ == "__main__":
    print(solution('AAAAE'))
    print(solution('AAAE'))
    print(solution('AAEAA'))
    print(solution('I'))
    print(solution('EIO'))
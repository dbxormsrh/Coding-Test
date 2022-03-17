def solution1(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    #map함수를 통해서 commands의 원소들을 사용, array의 원소를 가져온 후
    #정렬 후 list를 통해서 바로 원하는 정답을 도출해냈다.
    #map 함수를 통해서 for문을 대체한 부분이 인상적이었다.

def solution2(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
    #commands의 원소들을 직접 지정하지 않고, i,j,k로 가져와서 사용한 부분에 있어서
    #파이썬을 잘 사용했다라는 인상을 받았다.


if __name__ == "__main__":
    array = [1,5,2,6,3,7,4]
    commands = [[2,5,3],[4,4,1],[1,7,3]]

    print(solution1(array, commands))
    print(solution2(array, commands))

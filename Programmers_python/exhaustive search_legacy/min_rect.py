def solution(sizes):

    sorted_sizes = [[],[]]
    for i in sizes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
        sorted_sizes[0].append(i[0])
        sorted_sizes[1].append(i[1])

    return max(sorted_sizes[0]) * max(sorted_sizes[1])


if __name__ == "__main__":
    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

    print(solution(sizes))
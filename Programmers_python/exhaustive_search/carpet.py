def solution(brown, yellow):
    divs = []
    t = brown + yellow
    for d in range(1, t + 1, 1):
        if t % d == 0:
            divs.append(d)

    for i in range(len(divs)):
        w = divs[-(i+1)]
        h = divs[i]

        if w < h:
            w = temp
            w = h
            h = temp
        print(w, h)
        b = 2*h + 2*(w-2)
        y = (h-2)*(w-2)
        if b == brown and y == yellow:
            return [w, h]



print(solution(24, 24))
def solution(money,  cost):
    answer = 0
    won = [500,100,50,10,5,1]
    money_re = []
    for i, j in zip(cost, won):
        money_re.append(i*j)
    
    print(money_re)
    print(money_re.index(min(money_re)))
    return answer



if __name__ == "__main__":
    money = 4578
    cost = [1,4,99,35,50, 1000]
    print(solution(money, cost))

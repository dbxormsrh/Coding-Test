import copy
def solutions(operations):

    #operator = True
    answer = []
    for i in operations:
        cmp = i.split()
        operator = cmp[0]
        print(cmp)

        if cmp[0] == 'I':
            num = int(cmp[1])
            if len(answer) == 0:
                answer.append(num)
            elif len(answer) == 1:
                if int(answer[0]) <= num:
                    answer.append(num)
                else:
                    answer.insert(0, num)    
            else:
                if int(answer [-1]) <= num:
                    answer.append(num)
                elif int(answer[0]) >= num:
                    answer.insert(0, num)
                else:
                    for i in range(len(answer) - 1):
                        if num > int(answer[i]) and num < int(answer[i+1]):
                            answer.insert(i+1, num)
                            break
        else:
            if len(answer) == 0:
                continue

            if '-' in cmp[1]:
                del answer[0]
            else:
                del answer[-1]
    
    if len(answer) == 0:
        return [0, 0]
    elif len(answer) == 1:
        return [answer[0], answer[0]]
    else:
        return [answer[-1], answer[0]]
    return answer


if __name__ == "__main__":
    print(solutions(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solutions(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))
import numpy as np


class Node:
    def __init__(self, num):
        self.num = num
        self.connected_node = []

class Tree:
    def __init__(self):
        self.nodes = []
    def insert(self, node):
        self.nodes.append()


def solution(n, wires):
    answer = len(wires) + 1

    tops = {}

    for i in wires:
        if i[0] not in tops:
            tops[i[0]] = [i[1]]
        else:
            tops[i[0]].append(i[1])
        if i[1] not in tops:
            tops[i[1]] = [i[0]]
        else:
            tops[i[1]].append(i[0])

    for i in wires:
        temp_tops = tops
        print(temp_tops, i)

        temp_tops[i[0]].remove(i[1])
        temp_tops[i[1]].remove(i[0])

        for k, v in temp_tops:
            

        if not a_wires or not b_wires:
            answer = abs(len(a_wires) - len(b_wires))

        a_set = set(np.reshape(a_wires, (-1)))
        b_set = set(np.reshape(b_wires, (-1)))

        #print(a_set.intersection(b_set))

        a_set = a_set.union(b_set)

        temp = abs(len(a_set) - len(b_set))
        if answer > temp:
            answer = temp

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))       #3
print(solution(4, [[1,2],[2,3],[3,4]]))                                     #0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))                   #1
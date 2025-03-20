import copy
def check_depth(tree, idx, com):
    num_pole = 0
    if len(tree[idx]) == 0:
        return 1
    else:
        for v in tree[idx]:
            if v != com:
                num_pole += check_depth(tree, v, idx)
        return num_pole + 1
    
def solution(n, wires):
    tree = {i+1 : [] for i in range(n)}
    
    for i, j  in wires: 
        tree[i].append(j)
        tree[j].append(i)

    # cut a, b -> remove b in connected a, remove a in connected b
    answer = n+1
    for cut in wires:
        temp_tree = copy.deepcopy(tree)
        temp_tree[cut[0]].remove(cut[1])
        temp_tree[cut[1]].remove(cut[0])
        print(temp_tree)
        print(tree)
        
        a_depth = check_depth(temp_tree, cut[0], cut[0])
        b_depth = check_depth(temp_tree, cut[1], cut[1])
        print(cut, a_depth, b_depth)

        if abs(a_depth - b_depth) < answer:
            if answer == 0:
                return 0
            answer = abs(a_depth - b_depth)
        #print(answer)
    return answer

if __name__ == "__main__":
    res = solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
    print(res)
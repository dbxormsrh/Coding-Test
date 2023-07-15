def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = [0 for i in range(bridge_length)]
    bridge_weight = truck_weights[0]
    bridge.pop(0)
    bridge.append(truck_weights[0])
    i = 1

    while(i< len(truck_weights)):
        bridge_weight -= bridge.pop(0)
        answer += 1
        if bridge_weight + truck_weights[i] <= weight:
            bridge.append(truck_weights[i])
            bridge_weight += truck_weights[i]
            i += 1
        else:
            bridge.append(0)
    return answer + bridge_length

if __name__ == '__main__':
    print(solution(2,	10,	[7,4,5,6]))
    print(solution(100,	100,	[10]))
    print(solution(100,	100,	[10,10,10,10,10,10,10,10,10,10]	))
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = 0
    c = bridge_length
    while truck_weights:
        if(weight > truck_weights[0] and bridge_length != 0):
            truck = truck_weights.pop()
            bridge_length -= 1
            weight -= truck
        else:
            bridge_length -= 1
            weight -= truck


    return answer


if __name__ == '__main__':
    solution(2,	10,	[7,4,5,6])
import heapq

def solutions(operations):

    operator = True
    heap = []
    for i in operations:
        l = i.split()

        if l[0] == 'I':
            heapq.heappush(heap, int(l[1]))
        else:
            if '-' in l[1]:
                operator = False
            else:
                break
        
        print(l)
    return 0


if __name__ == "__main__":
    print(solutions(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
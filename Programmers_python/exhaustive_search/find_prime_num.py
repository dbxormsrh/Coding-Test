from itertools import permutations

def solution(numbers):
    num = [s for s in numbers]
    num_list = []
    temp = []

    for i in range(1, len(num) + 1):
        temp.append(list(permutations(num, i)))

    print(temp)
    for i in range(len(num)):
        for j in temp:
            
        
    
        

if __name__ == "__main__":
    solution("17")
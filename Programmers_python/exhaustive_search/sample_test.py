def solution(answer):
    st = 0
    nd = 0
    rd = 0

    for idx in range(len(answer)):
        st_answer = [1, 2, 3, 4, 5]
        nd_answer = [2, 1, 2, 3, 2, 4, 2, 5]
        rd_answer = [3, 1, 2, 4, 5]

        if answer[idx] == st_answer[idx % 5]:
            st += 1

        if answer[idx] == rd_answer[int(idx / 2) % 5]:
            rd += 1

        if answer[idx] == nd_answer[idx % 8]:
            nd += 1

    m = -1
    if st > m:
        m = st
    if m < nd:
        m = nd
    if m < rd:
        m = rd
    print(f"st : {st}, nd : {nd}, rd : {rd}")
    ans = []

    if m == st:
        ans.append(1)
    if m == nd:
        ans.append(2)
    if m == rd:
        ans.append(3)

    return ans



if __name__ == "__main__":
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))
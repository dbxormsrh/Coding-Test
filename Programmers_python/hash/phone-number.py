def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for i, j in zip(phoneBook, phoneBook[1:]):
        if j.startswith(i):
            return False
    return True

if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]
    print(solution(phone_book))
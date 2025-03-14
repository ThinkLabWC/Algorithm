def solution(phoneBook):
    phoneBook.sort()
    # print(phoneBook)
    # print(dict(zip(phoneBook, phoneBook[1:])))
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        # print(p1, p2)
        if p2.startswith(p1):
            return False
    return True

# {
#     "123": FAlse
# }
solution(["119", "97674223", "1195524421"]) #	false
# solution(["123","456","789"]) #	true
# solution(["12","123","1235","567","88"]) #	false

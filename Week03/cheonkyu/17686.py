def solution(files):
    answer = []
    tmp = []
    for i in range(len(files)):
        file = files[i]
        _file = file.upper()
        item = {
            "header": None,
            "number": None, 
            "tail": None,
            "index": i,
            "file": file
        }
        header = ''
        number = ''
        for c in _file:
            # print(c)
            if item["header"] == None and not c.isnumeric():
                header += c
            elif c.isnumeric():
                item["header"] = header 
                number += c
            else:
                # print(number)
                item["number"] = int(number)
                break
        item["number"] = int(number)
        tmp.append(item)
        # print(item)
    # print(tmp)
    tmp.sort(key = lambda x: (x.get("header", ""), x.get("number", 0), x.get("index", 0))) 
    # print(tmp)
    answer = list(map(lambda x: x.get("file"), tmp))
    print(answer)
    return answer

# solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]

# solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

# solution(["F ---  10.txt", "B   10.txt", "A 10.txt", "F-- 22.txt"])
# solution(["img2.png", "img02.png", "img1.png"]) # ["img1.png", "img2.png", "img02.png"]

solution(["file00.txt1", "file0.txt1", "file0000000.txt1"])
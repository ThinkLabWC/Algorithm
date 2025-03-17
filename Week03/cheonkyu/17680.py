from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    time = 0
    for city in cities:
        val = city.lower()
        if (len(cache) >= cacheSize or val in cache) and len(cache) != 0:
            if val in cache:
                i = cache.index(val)
                del cache[i]
                time += 1
            else:
                cache.popleft()
                time += 5
            cache.append(val)
        else:
            if cacheSize != 0: 
                cache.append(val)
            time += 5
        # print(city)
    answer = time
    # print(time)
    return answer

# solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
# solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
# solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
# solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
# solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
# solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
# solution(3, ["a", "b", "a", "c", "d", "a"]) #  22
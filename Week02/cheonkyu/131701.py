# O(n^2)
def solution(elements):
    answer = 0
    s = set([])
    e = [[] * len(elements) for i in range(len(elements))]
    e[0] = elements
    for i in range(1, len(elements)):
        for j in range(0, len(elements)):
            e[i].append(e[i - 1][(j + 1) % len(elements)] + elements[j])
    answer = len(set(sum(e, [])))
    # print(answer)
    return answer

# solution([7,9,1,1,4]) # 18

# O(n^3)
# def get_circle_sum(elements, a, b):
#     result = 0
#     for a in range(a, b):
#         result += (elements[a % len(elements)])
#     return result
# def total_sum(elements, step):
#     s = set([])
#     for i in range(0, len(elements)):
#         _sum = get_circle_sum(elements, i, i+step+1)
#         s.add(_sum)
#     # print(s)
#     return s
# def solution(elements):
#     answer = 0
#     s = set([])
#     for i in range(0, len(elements)):
#       s.update(total_sum(elements, i))
#     answer = len(s)
#     return answer

# solution([7,9,1,1,4]) # 18
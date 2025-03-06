def solution(n, arr1, arr2):
    answer = []
    data = []
    for i in range(0, len(arr1)):
      data.append(arr1[i] | arr2[i])
    data = list(
       map(lambda x: bin(x)[-n:]
           .replace('0', ' ')
           .replace('1', '#')
           .replace('b', ' ')
          , data)
    )
    answer = data
    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
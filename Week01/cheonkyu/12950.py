def solution(arr1, arr2):
    answer = [[]]
    for i in range(0, len(arr1)):
        for j in range(0, len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    answer = arr1
    print(answer)
    return answer

solution([[1,2],[2,3]], [[3,4],[5,6]])
solution([[1],[2]],	[[3],[4]]) # [[4],[6]]
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]
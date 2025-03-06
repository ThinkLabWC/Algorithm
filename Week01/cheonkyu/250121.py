def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    indexDict = {
      'code': 0,
      'date': 1,
      'maximum': 2,
      'remain': 3 
    }
    result = []
    for d in data:
        i = indexDict.get(ext, 0)
        if d[i] <= val_ext:
            result.append(d)
    sort_index = indexDict.get(sort_by)
    result.sort(key = lambda x: x[sort_index])
    answer = result
    return answer


solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
         ,	"date",	20300501.,	"remain")
	# [[3,20300401,10,8],[1,20300104,100,80]]
def solution(clothes):
    answer = len(clothes)
    clothe_dict = {}
    for c in clothes:
        [name, clothe_type]= c
        if clothe_type in clothe_dict:
          clothe_dict[clothe_type].append(name)
        else:
          clothe_dict[clothe_type] = [name]
    # print(clothe_dict)
    if len(clothe_dict) > 1:
      tmp = 1
      len(clothe_dict)
      for key, val in clothe_dict.items():
        tmp = tmp * len(val)
      answer += tmp
    print(answer)
    return answer


{
   "headgear": ["a", 'b'],
   "eyewear": ["c", 'd'],
   "face": ["e", 'f']
}
# solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]) #	5
# solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]) #	3
# solution([["crow_mask", "face"]]) #	1
solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]]) # 26
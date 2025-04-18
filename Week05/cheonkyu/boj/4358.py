# from collections import Counter
# data = [
# 'Red Alder',
# 'Ash',
# 'Aspen',
# 'Basswood',
# 'Ash',
# 'Beech',
# 'Yellow Birch',
# 'Ash',
# 'Cherry',
# 'Cottonwood',
# 'Ash',
# 'Cypress',
# 'Red Elm',
# 'Gum',
# 'Hackberry',
# 'White Oak',
# 'Hickory',
# 'Pecan',
# 'Hard Maple',
# 'White Oak',
# 'Soft Maple',
# 'Red Oak',
# 'Red Oak',
# 'White Oak',
# 'Poplan',
# 'Sassafras',
# 'Sycamore',
# 'Black Walnut',
# 'Willow',
# ]
# # print(round(1/1000000, 4))
# # data = list(map(str, input().split(' ')))
# total = len(data)
# c = Counter(data)
# tmp = sorted(c.items(), key=lambda pair: pair[0])
# for key, val in tmp:
#   print("%s %.4f" % (key, val/total * 100))
import sys

dict_info = {}
count = 0 

while (1) :
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    if word in dict_info :
        dict_info[word] += 1
        count += 1
    else :
        dict_info[word] = 1
        count += 1

sorted_list = sorted(dict_info.items(), key = lambda x : x[0])
for key, value in sorted_list :
    print('%s %.4f' %(str(key), round((value/count) * 100, 4)))

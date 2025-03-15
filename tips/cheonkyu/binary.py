# 10진수를 base진수로 변환하기
def to_str(n, base):
  converter = "0123456789ABCDEF"
  if n < base:
    return converter[n]
  else:
    return to_str(n // base, base) + converter[n % base]

# print(to_str(10,3))
# print(to_str(1010,16))
while True:
  [name, age, weight] = input().split()
  if name == '#':
    break
  grade = 'Junior'
  if int(age) > 17 or int(weight) >= 80:
    grade = 'Senior'
  print(f"{name} {grade}")
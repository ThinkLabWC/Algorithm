def solution(wallpaper):
    answer = []
    data = []
    for str in wallpaper:
        data.append(list(map(lambda x: 0 if x == '.' else 1, list(str))))
    
    sx = []
    sy = []
    for x in range(0, len(data)):
      for y in range(0, len(data[0])):
         if data[x][y] == 1:
            print(x, y)
            sx.append(x)
            sy.append(y)
    answer = [min(sx), min(sy), max(sx) + 1, max(sy) + 1]
    # print(answer)
    return answer

# solution([".#...", "..#..", "...#."])
# solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
# solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
# solution(["..", "#."])

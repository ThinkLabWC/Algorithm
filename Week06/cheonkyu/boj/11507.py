card = input()

cs = {
  "P": [1 for i in range(0, 13)],
  "K": [1 for i in range(0, 13)],
  "H": [1 for i in range(0, 13)],
  "T": [1 for i in range(0, 13)]
}
# P01K02H03H04
ok = True
for i in range(0, len(card), 3):
  id = int(card[i+1:i + 3]) - 1
  key = card[i]
  cs[key][id] = cs[key][id] - 1
  if cs[key][id] < 0:
    ok = False
    break
  
if not ok:
  print("GRESKA")
else:
  print(f"{sum(cs.get("P"))} {sum(cs.get("K"))} {sum(cs.get("H"))} {sum(cs.get("T"))}")

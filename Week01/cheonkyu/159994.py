def solution(cards1, cards2, goal):
    target = []
    for g in goal:
        if cards1 and cards1[0] == g:
            cards1.pop(0)
            target.append(g)
        elif cards2 and cards2[0] == g:
            cards2.pop(0)
            target.append(g)
    if target == goal:
        return "Yes"
    else:
        return "No"

# a = solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]) # "Yes"
# a= solution(["i", "water", "drink"],	["want", "to"],	["i", "want", "to", "drink", "water"]) # "No"
# a = solution(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["string", "or", "integer"], ["string", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) #  "Yes"

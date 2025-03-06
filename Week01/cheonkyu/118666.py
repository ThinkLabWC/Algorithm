def get_survey(a, b):
    return [(a, 3), (a, 2), (a, 1), ('-', 0), (b, 1), (b, 2), (b, 3)]

def solution(survey, choices):
    total_score = {}
    surveyDict = {
       'RT' : get_survey('R', 'T'),
       'TR' : get_survey('T', 'R'),
       'CF' : get_survey('C', 'F'),
       'FC' : get_survey('F', 'C'),
       'JM' : get_survey('J', 'M'),
       'MJ' : get_survey('M', 'J'),
       'AN' : get_survey('A', 'N'),
       'NA' : get_survey('N', 'A'),
    }
    for i in range(0, len(survey)):
        type, score = surveyDict.get(survey[i])[choices[i] - 1]
        if not total_score.get(type):
            total_score[type] = int(score)
        else:
            total_score[type] += int(score)

    a = 'R' if total_score.get('R', 0) >= total_score.get('T', 0) else 'T'
    a1 = 'C' if total_score.get('C', 0) >= total_score.get('F', 0) else 'F'
    a2 = 'J' if total_score.get('J', 0) >= total_score.get('M', 0) else 'M'
    a3 = 'A' if total_score.get('A', 0) >= total_score.get('N', 0) else 'N'
    # print(total_score)
    answer = a + a1 + a2 + a3
    # print(answer)
    return answer


# solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]) # TCMA
# solution(["TR", "RT", "TR"], [7, 1, 3]) # RCJA
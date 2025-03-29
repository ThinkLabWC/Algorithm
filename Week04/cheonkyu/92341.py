import math
def get_minutes(time):
    [h, m] =map(int, time.split(':'))
    return m + (h * 60)

def get_price(fees, minutes):
    [basic_time, basic_price, unit_time, unit_price] = fees
    if minutes <= basic_time:
        return basic_price
    else:
        return basic_price + (math.ceil((minutes - basic_time) / unit_time) * unit_price)
    
def solution(fees, records):
    answer = []
    history = {}
    parking_time = {}
    
    for record in records:
        [time, car, cmd] = record.split(' ')
        if cmd == 'IN':
            history[car] = time
        elif cmd == 'OUT':
            start = get_minutes(history[car])
            end = get_minutes(time)
            diff = end - start
            del history[car]
            
            if not car in parking_time:
                parking_time[car] = diff
            else:
                parking_time[car] += diff
    for car, time in history.items():
        start = get_minutes(time)
        end = get_minutes('23:59')
        diff = end - start
        if not car in parking_time:
            parking_time[car] = diff
        else:
            parking_time[car] += diff
    result = [parking_time[key] for key in sorted(parking_time.keys())]
    # print(result)
    answer = list(map(lambda x : get_price(fees, x), result))
    return answer

# solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
# [180, 5000, 10, 600]	
# ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]) # [0, 591]
# solution([1, 461, 1, 10], ["00:00 1234 IN"]) # [14841]
# [120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
# [1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
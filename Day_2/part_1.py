import numpy as np

def increasing_decreasing(numbers):
    
    arr = np.array(numbers)
    diff = np.diff(arr)
    is_increasing = np.all(diff > 0)
    is_decreasing = np.all(diff < 0)
    if is_increasing or is_decreasing:
        return True
    return False


reports_list = []

open('Day_2/result.txt', 'w').close()

with open('Day_2/puzzle_input.txt', 'r') as reports:
    for report in reports:
        report = report.replace('\n', '')
        reports_list.append([int(num) for num in report.split()])

count = 0
status = False

for report in reports_list:
    if len(set(report)) < len(report):
        with open('Day_2/result.txt', 'a') as out:
            out.write(f'{report} : UnSafe\n') 
        continue
    dec_or_inc = increasing_decreasing(report)
    if dec_or_inc:
        length = len(report) - 1

        for num in range(1, length+1):
            dif = report[num -1] - report[num]
            if 1 <= abs(dif) <= 3:
                status = True
            else:
                status = False
                break

    if status:
        with open('Day_2/result.txt', 'a') as out:
            out.write(f'{report} : Safe\n')
        count += 1
    else:
        with open('Day_2/result.txt', 'a') as out:
            out.write(f'{report} : UnSafe\n')            


print(count)
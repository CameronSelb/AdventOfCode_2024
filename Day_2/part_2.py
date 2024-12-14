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

def check_report(current_report):

    if increasing_decreasing(current_report):
        length = len(current_report)
        if len(set(current_report)) < length:
            return False

        for num in range(1, length):
            dif = current_report[num -1] - current_report[num]
            if abs(dif) < 1 or abs(dif) > 3:
                return False
            
        return True
    return False

count = 0                   
for report in reports_list:
    status = check_report(report)
    if status:
        with open('Day_2/result.txt', 'a') as out:
            out.write(f'{report} : Safe\n')
        count += 1
    else: 
        for i in range(len(report)):
            copy_report = report.copy()
            copy_report.pop(i)
            if check_report(copy_report):
                count += 1
                break

        with open('Day_2/result.txt', 'a') as out:
            out.write(f'{report} : UnSafe\n')        

print(count)
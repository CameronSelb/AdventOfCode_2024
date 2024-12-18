def split_input() -> list[list]:
    calibrate = []
    with open('Day_7/puzzle_input.txt', 'r') as c:
        for line in c:
            numbers = []
            line = line.replace('\n', '')
            result = int(line[:line.index(':')])
            line = line[line.index(':') + 2:]
            numbers = [int(num) for num in line.split()]
            calibrate.append([result, numbers])
    return calibrate

def check_equal(target, numbers):
    def backtracking(index, current_value):
        if index == len(numbers):
            return current_value == target
        
        if backtracking(index + 1, current_value + numbers[index]):
            return True
        
        if backtracking(index + 1, current_value * numbers[index]):
            return True

        return False
    
    return backtracking(1, numbers[0])

total = 0
calibrations = split_input()

for line in calibrations:

    target = line[0]
    numbers = line[1]
    if check_equal(target, numbers):
        total += target

print(total)
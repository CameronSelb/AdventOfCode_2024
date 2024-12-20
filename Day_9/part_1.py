def get_input() -> list:
    with open('Day_9/puzzle_input.txt', 'r') as disk_file:
        disk = [int(num) for num in list(disk_file.read())]

    return disk

def create_file_map(d_map) -> str:
    f_index = 0
    f_map = []

    for i, num in enumerate(d_map):
        if i % 2 == 0:
            for _ in range(num):
                f_map.append(f_index)
            f_index += 1
        else:
            for _ in range(num):
                f_map.append('.')
    
    return f_map

disk_map = get_input()
file_map = create_file_map(disk_map)

for i in range(len(file_map)-1 , 0, -1):
    end_file = file_map[i]
    file_before = file_map[:i]

    if end_file == '.':
        continue

    if '.' not in file_before:
        break

    if '.' in file_before:
        file_map[file_before.index('.')] = file_map[i]
        file_map[i] = '.'

checksum = 0

with open('Day_9/output.txt', 'w') as out:
    file_new = [str(sym) for sym in file_map if sym != '.']
    str_map = ''.join(file_new)
    out.write(str_map)

for i in range(len(file_map)):
    if file_map[i] == '.':
        break
    checksum += i * file_map[i]

print(checksum)
def check_horizontal(current_grid : list[str]) -> int:
    count = 0
    for line in current_grid:
        count += line.count('XMAS') + line.count('SAMX')
    return count

def rotate_grid(grid_to_rot : list[str]) -> list[str]:
    rotated_grid = []
    for row in range(len(grid_to_rot)-1,-1,-1):
        flipped_line = '' 
        for col in range(len(grid_to_rot)):
            flipped_line += grid_to_rot[col][row]

        rotated_grid.append(flipped_line)

    return rotated_grid

def move_diagonal_to_horizontal(grid_to_transfor:list[str]) -> list[str]:
    result = []
    length = len(grid_to_transfor) - 1
    col = length
    row = 0

    while col >= 0:
        line = ''
        while col <= length and row <= length:
            line += grid_to_transfor[row][col]
            row += 1
            col += 1

        result.append(line)
        col = length - row
        row = 0
    
    col = 0
    row = 1
    count = 0
    while True:
        count += 1
        if count > length:
            break

        line = ''
        while row <= length and col <= length:
            line += grid_to_transfor[row][col]
            row += 1
            col += 1

        result.append(line)
        row = abs(row - length + count)
        col = 0

    return result

def flip_grid(grid_to_flip):
    fliped_grid = []
    for row in range(len(grid_to_flip)):
        line = ''
        for col in range(len(grid_to_flip)-1, -1, -1):
            line += grid_to_flip[row][col]
        fliped_grid.append(line)

    return fliped_grid 
        
grid = []

with open('Day_4/puzzle_input.txt', 'r') as grid_file:
    for line in grid_file:
        line = line.replace('\n','')
        grid.append(line)

xmas_count = 0
xmas_count += check_horizontal(grid)
normal_count = check_horizontal(grid)

for line in grid:
    print(line)
print()

transformed_grid = rotate_grid(grid) 
xmas_count += check_horizontal(transformed_grid)
vertical_count = check_horizontal(transformed_grid)
for line in transformed_grid:
    print(line)
print()

transformed_grid = move_diagonal_to_horizontal(grid)
xmas_count += check_horizontal(transformed_grid)
pos_diagonal_count = check_horizontal(transformed_grid)

transformed_grid = flip_grid(grid)
transformed_grid = move_diagonal_to_horizontal(transformed_grid)
xmas_count += check_horizontal(transformed_grid)
neg_diagonal_count = check_horizontal(transformed_grid)

print(normal_count, vertical_count, pos_diagonal_count,neg_diagonal_count)
print(xmas_count)
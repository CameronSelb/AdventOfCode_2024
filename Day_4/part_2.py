def check_horizontal(words : list, coords : list, current_grid : list[str], grid_loc:list[list]) -> int:
    for row,line in enumerate(current_grid):
        if 'MAS' in line:
            for _ in range(line.count('MAS')):
                words.append('MAS')
                coords.append(grid_loc[row][line.index('MAS') + 1])
                line = line[:line.index('MAS')] + '_' + line[line.index('MAS') + 1:]
        if 'SAM' in line:
            for _ in range(line.count('SAM')):
                words.append('SAM')
                coords.append(grid_loc[row][line.index('SAM') + 1])
                line = line[:line.index('SAM')] + '_' + line[line.index('SAM') + 1:]
    return words, coords

def move_diagonal_to_horizontal(grid_to_transfor:list[str]) -> list[str]:
    result = []
    length = len(grid_to_transfor) - 1
    col = length
    row = 0

    while col >= 0:
        if type(grid_to_transfor[row][col]) is list:
            line = []
        else:
            line = ''
        while col <= length and row <= length:
            if type(grid_to_transfor[row][col]) is list:
                line.append(grid_to_transfor[row][col])
            else:
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

        if type(grid_to_transfor[row][col]) is list:
            line = []
        else:
            line = ''
        while row <= length and col <= length:
            if type(grid_to_transfor[row][col]) is list:
                line.append(grid_to_transfor[row][col])
            else:
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

def flip_grid_list_elements(grid_to_flip):
    fliped_grid = []
    for row in range(len(grid_to_flip)):
        line = []
        for col in range(len(grid_to_flip)-1, -1, -1):
            line.append(grid_to_flip[row][col])
        fliped_grid.append(line)

    return fliped_grid 
        
def create_coords(coords_for_grid : list[str]):
    coords = []
    
    for i in range(len(coords_for_grid)):
        line = []
        for j in range(len(coords_for_grid)): 
            line.append([i,j])

        coords.append(line)

    return coords

grid = []
words = []
coords = []

with open('Day_4/puzzle_Input.txt', 'r') as grid_file:
    for line in grid_file:
        line = line.replace('\n','')
        grid.append(line)

grid_coords = create_coords(grid)

xmas_count = 0

transformed_grid = move_diagonal_to_horizontal(grid)
transformed_coords = move_diagonal_to_horizontal(grid_coords)
words, coords = check_horizontal(words, coords, transformed_grid, transformed_coords)

transformed_grid = flip_grid(grid)
transformed_coords = flip_grid_list_elements(grid_coords)
transformed_grid = move_diagonal_to_horizontal(transformed_grid)
transformed_coords = move_diagonal_to_horizontal(transformed_coords)
words, coords = check_horizontal(words, coords, transformed_grid, transformed_coords)

used_nums = []
print(coords)
for i, num1 in enumerate(coords):
    for j, num2 in enumerate(coords):
        if num1 == num2 and num1 not in used_nums and i != j: 
            xmas_count += 1
            used_nums.append(num1)
            break

print(xmas_count)
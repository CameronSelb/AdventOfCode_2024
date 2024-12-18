def get_input(grid : list) -> list:

    with open('Day_6/test.txt', 'r') as input_file:
        for line in input_file:
            line = line.replace('\n', '')
            grid.append(list(line))
        
    return grid

def move_guard(guard_loc : list, grid : list[list], degrees : int, move : int) -> list:

    while True:
        move = -1 if degrees == 0 or degrees == 270 else 1

        if guard_loc[0] + move >= len(grid) or guard_loc[1] + move >= len(grid) or guard_loc[0] + move < 0 or guard_loc[1] + move < 0:
            grid[guard_loc[0]][guard_loc[1]] = '|' if degrees == 0 or degrees == 180 else '-'
            break

        if degrees == 0 or degrees == 180:
            if grid[guard_loc[0] + move][guard_loc[1]] == '#':
                degrees += 90
                grid[guard_loc[0]][guard_loc[1]] = '+'
                continue

            grid[guard_loc[0]][guard_loc[1]] = '|' if grid[guard_loc[0]][guard_loc[1]] == '.' else '+' 
                
            guard_loc[0] += move
    
        elif degrees == 90 or degrees == 270:
            if grid[guard_loc[0]][guard_loc[1] + move] == '#':
                degrees += 90
                grid[guard_loc[0]][guard_loc[1]] = '+'
                continue

            grid[guard_loc[0]][guard_loc[1]] = '-' if grid[guard_loc[0]][guard_loc[1]] == '.' else '+'
                
            guard_loc[1] += move
        
        degrees -= 360 if degrees == 360 else 0

    return grid

def main():
    map_grid = []
    facing = 0
    direction = -1

    map_grid = get_input(map_grid)

    for i, line in enumerate(map_grid):
        if '^' in line:
            initail_pos = [i, line.index('^')]
            break

    saved = initail_pos.copy()

    map_grid = move_guard(initail_pos, map_grid, facing, direction)

    str_out = ''

    map_grid[saved[0]][saved[1]] = '^'

    for line in map_grid:
        str_out += ''.join(line) + '\n'


    with open('Day_6/output.txt', 'w') as out:
        out.write(str_out)

if __name__ == '__main__':
    main()
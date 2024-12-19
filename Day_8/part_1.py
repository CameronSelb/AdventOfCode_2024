def get_input() -> list[list]:
    grid = []
    with open('Day_8/puzzle_input.txt', 'r') as map:
        for line in map:
            line = line.replace('\n', '')
            grid.append(list(line))

    return grid

def get_nodes(grid) -> dict[list]:

    nodes_loc = {}
    for i, line in enumerate(grid):
        for j, sym in enumerate(line):
            if sym != '.':
                if grid[i][j] in nodes_loc:
                    nodes_loc[grid[i][j]].append((i,j))
                else:
                    nodes_loc[grid[i][j]] = [(i,j)]

    return nodes_loc

def create_antinodes(node1, node2, lgth, hght) -> list:

    if node1 == node2:
        return

    y1, x1 = node1
    y2, x2 = node2
    
    new_x = x2 + (x2 - x1)
    new_y = y2 + (y2 - y1)

    if lgth > new_x >= 0 and hght > new_y >= 0:
        antinodes.add((new_y, new_x))


nodes_map = get_input()
height = len(nodes_map)
length = len(nodes_map[0])
nodes = get_nodes(nodes_map)


antinodes = set()

for key in nodes:
    nodes_list = nodes[key]
    for n1 in nodes_list:
        for n2 in nodes_list:
            create_antinodes(n1, n2, length, height)
            create_antinodes(n2, n1, length, height)

for an in antinodes:
    y, x = an
    if nodes_map[y][x] == '.':
        nodes_map[y][x] = '#' 

print(len(antinodes))
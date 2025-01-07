import heapq
import copy

def map_read(input):
    ori_map = []
    byte_on_grid_all= []
    with open(input, 'r') as f:
        for line in f:
            ori_map.append(line.strip())
            position = tuple(map(int, line.rstrip().split(",")))[::-1]
            byte_on_grid_all.append(position)
    return ori_map, byte_on_grid_all

def grid_generate(byte_on_grid_all, bytes_fallen, ro, co):

    grid = {}   
    byte_on_grid = byte_on_grid_all[0:bytes_fallen]
    for r in range(ro):
        grid[r]={}
        for c in range(co):
            grid[r].setdefault(c," ")
            if (r,c) in byte_on_grid:
                grid[r][c]="#"
    return grid

def grid_generate_from_base(base_grid, fallenbase, target):
    my_grid = copy.deepcopy(base_grid)
    byte_on_grid = byte_on_grid_all[fallenbase:target]
    for position in byte_on_grid:
        r,c=position
        my_grid[r][c]="#"
    return my_grid    

    
def my_queue(grid):
    global total_search_behevior
    total_search_behevior += 1
    
    queue = [(0, start[0], start[1], 0, 1,[start])] 

    # min_cost_state = {}
    min_cost_E = None
    all_paths = []
    visited = set()
    visited.add((0, 0, 0, 1))

    while queue:
        cost, r, c, dr, dc , path = heapq.heappop(queue)
        if (r, c) == end:
                min_cost_E = cost
                all_paths.append(path)
                break
            
        for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr,nc,dr,dc) not in visited:
                    heapq.heappush(queue, (cost + 1, nr, nc, dr, dc, path + [(nr,nc)]))
                    visited.add((nr,nc,dr,dc))

    # print(min_cost_E, "mininum steps")
    return min_cost_E, path

def print_paths_to_file(grid, path):

    grid_str = ""
    for r in range(rows):
        for c in range(cols):
            if (r, c) in path:
                grid_str += "o"
            elif grid[r][c] == "#":
                grid_str += "."
            else:
                grid_str += " "
        grid_str += "\n"
    return grid_str

start = (0,0)

input="input1.txt"
rows = 7
cols = 7
end = (6,6)
fallen_base = 12
fallen_range = [12,25]

input="input2.txt"
rows = 71
cols = 71
end = (70,70)
fallen_base = 1024
fallen_range = [1024,3450]

found = 0
current = False
total_search_behevior = 0

ori_map, byte_on_grid_all = map_read(input)

base_grid = grid_generate(byte_on_grid_all, fallen_base, rows, cols)    
min_cost_E, path = my_queue(base_grid)

if min_cost_E:
    print (f"after {fallen_base} bytes fallen, steps to go: {min_cost_E}")
    # grid_str = print_paths_to_file(base_grid , path)
    # with open(f"output.txt", 'w', encoding='utf-8') as f:
    #     f.write(grid_str)

    min = fallen_range[0]
    max = fallen_range[1]
    

    while (True):
        fallen_target = (max + min) //2  ## bisection method ##
        my_grid = grid_generate_from_base(base_grid, fallen_base, fallen_target)
        current = my_queue(my_grid)[0]
        if current: #current true
            base_grid = grid_generate_from_base(base_grid, fallen_base, fallen_target) ##dynamically move base_grid to min bytes fallen
            min = fallen_target
            fallen_base = min
        else:   #current false
            max = fallen_target 
        if max - min == 1:
            if current:
                found = fallen_target +1
            else:
                found = fallen_target
            break
else:
    print("no path can be found")

    
print (f"after {found} bytes fallen, fallen Byte postion: {ori_map[found-1]}")
    
print("total queue searching times is", total_search_behevior)
    
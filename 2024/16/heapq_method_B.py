import heapq
import time, copy

# 读取网格数据
input="input1.txt"
input="input2.txt"
input="input3.txt"
with open(input, 'r') as f:
    grid = [list(line.rstrip('\n')) for line in f]  # 将每行转换为字符列表，方便修改

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# 查找起始点 "S"
start = None
end = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)

queue = [(0, start[0], start[1], 0, 1,[start])]  # 初始方向设为向右（dr=0, dc=1）

min_cost_state = {}
min_cost_E = None
all_paths = []

while queue:
    cost, r, c, dr, dc , path = heapq.heappop(queue)
    state = (r, c, dr, dc)
    
    if state in min_cost_state:
        if cost > min_cost_state[state]:
            continue
    else:
        min_cost_state[state] = cost
    
    if grid[r][c] == 'E':
        if not min_cost_E:
            min_cost_E = cost
        if cost == min_cost_E:
            all_paths.append(path)
        continue
        
    # 尝试直行
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' :
        heapq.heappush(queue, (cost + 1, nr, nc, dr, dc, path+[(nr, nc)]))

    # 尝试转弯（左转和右转）
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
            fr, fc = r + ndr, c + ndc
            if 0 <= fr < rows and 0 <= fc < cols and grid[fr][fc] != '#':
                heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc, path))

print(min_cost_E)
print(len(all_paths))
print(len(set(position for path in all_paths for position in path)))



def print_paths_to_file(grid, path):
    rows = len(grid)
    cols = len(grid[0])

    # 创建网格的副本
    display_grid = copy.deepcopy(grid)
    # 将 '#' 和 '.' 替换为空格
    for r in range(rows):
        for c in range(cols):
            if display_grid[r][c] == '.':
                display_grid[r][c] = ' '
            if display_grid[r][c] == '#':
                display_grid[r][c] = '.'
    # 标记路径上的点
    for r, c in path:
        if display_grid[r][c] == ' ':
            display_grid[r][c] = '*'
        elif display_grid[r][c] == 'S' or display_grid[r][c] == 'E':
            pass  # 保留起点和终点的标记
        else:
            display_grid[r][c] = '*'
    # 将网格转换为字符串
    grid_str = '\n'.join(''.join(row) for row in display_grid)
    # 将网格字符串写入文件，覆盖原内容
    return grid_str


# for index, path in enumerate(all_paths):
#     if index > 30:
#         break
#     print(index)
#     # time.sleep(5)
#     grid_str = print_paths_to_file(grid , path)
#     with open(f"paths_min_score/output_{index:03d}.txt", 'w', encoding='utf-8') as f:
#         f.write(grid_str)
    
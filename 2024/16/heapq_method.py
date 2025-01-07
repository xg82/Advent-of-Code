import sys
import heapq

# 读取网格数据
with open("input3.txt", 'r') as f:
    grid = [list(line.rstrip('\n')) for line in f]  # 将每行转换为字符列表，方便修改

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# 查找起始点 "S"
start = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    if start is not None:
        break

if start is None:
    print('起始点 "S" 未在网格中找到。')
    sys.exit(1)

# 初始化优先队列和访问集合
# 状态：cost, r, c, dr, dc
queue = [(0, start[0], start[1], 0, 1)]  # 初始方向设为向右（dr=0, dc=1）
seen = set()
seen.add((start[0], start[1], 0, 1))

# 添加 parents 字典来记录路径
parents = {}  # key: (r, c, dr, dc), value: (prev_r, prev_c, prev_dr, prev_dc)

# 主循环
part1 = None
end_state = None
while queue:
    cost, r, c, dr, dc = heapq.heappop(queue)
    if grid[r][c] == 'E':
        part1 = cost
        end_state = (r, c, dr, dc)
        break

    # 尝试直行
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc, dr, dc) not in seen:
        heapq.heappush(queue, (cost + 1, nr, nc, dr, dc))
        seen.add((nr, nc, dr, dc))
        parents[(nr, nc, dr, dc)] = (r, c, dr, dc)

    # 尝试转弯（左转和右转）
    for ndr, ndc in [(-dc, dr), (dc, -dr)]:
        if (r, c, ndr, ndc) not in seen:
            # 检查转弯后前方是否有障碍
            fr, fc = r + ndr, c + ndc
            if 0 <= fr < rows and 0 <= fc < cols and grid[fr][fc] != '#':
                heapq.heappush(queue, (cost + 1000, r, c, ndr, ndc))
                seen.add((r, c, ndr, ndc))
                parents[(r, c, ndr, ndc)] = (r, c, dr, dc)


###########
#export the map#

if part1 is not None:
    print(f'Part 1: {part1}')

    # 1. 重新构建路径
    path = []
    state = end_state
    while state != (start[0], start[1], 0, 1):
        path.append(state)
        state = parents.get(state)
        if state is None:
            break  # 正常情况下不会发生
    path.append((start[0], start[1], 0, 1))
    path.reverse()  # 将路径顺序反转，起点到终点

    # 2. 在网格上标记路径
    direction_symbols = {
        (0, 1): '→',   # 向右
        (0, -1): '←',  # 向左
        (1, 0): '↓',   # 向下
        (-1, 0): '↑'   # 向上
    }

    for idx in range(len(path) - 1):
        r, c, dr, dc = path[idx][0], path[idx][1], path[idx][2], path[idx][3]
        nr, nc = path[idx + 1][0], path[idx + 1][1]
        # 计算移动的方向（下一步的位置减去当前的位置）
        move_dr = nr - r
        move_dc = nc - c
        symbol = direction_symbols.get((move_dr, move_dc))
        if symbol:
            # 不覆盖起点和终点
            if grid[nr][nc] not in ('S', 'E'):
                grid[nr][nc] = symbol

    # 3. 将网格写入文件
    with open('output.txt', 'w', encoding='utf-8') as f:
        for row in grid:
            f.write(''.join(row) + '\n')

    print('最小路径已输出到 "output.txt" 文件中。')

else:
    print('无法找到从 "S" 到 "E" 的路径。')

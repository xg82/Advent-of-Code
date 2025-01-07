
from collections import deque

inp = "input1.txt"
inp = "input2.txt"
grid = [list(line.strip()) for line in open(inp)]
rows=len(grid)
cols=len(grid[0])
start = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'S':
            start = (r, c)
            break
    if start:
        break

dists = [[-1]*cols for _ in range(rows)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q=deque([start])
while q:
    cr,cc=q.popleft()
    for dr,dc in dirs:
        nr, nc = cr + dr, cc + dc
        if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]=="#" or dists[nr][nc] != -1 : 
            continue
        dists[nr][nc] = dists[cr][cc]+1 
        q.append((nr,nc))

# 预先计算满足条件的相对偏移量
offsets = []
for dc in range(-20, 21):
    for dr in range(0, 21):
        if 2 <= abs(dr) + abs(dc) <= 20:
            if (dr, dc) > (0,0) :  ## only search for neighbours in one direction
                offsets.append((dr, dc))

count = 0
for r in range(rows):
    for c in range(cols):
        if dists[r][c] != -1:
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if  0 <= nr < rows and 0 <= nc < cols and dists[nr][nc] != -1:
                    if abs(dists[r][c] - dists[nr][nc]) >=  100 + abs(dr) + abs(dc):
                        count += 1
print(count)
            
    

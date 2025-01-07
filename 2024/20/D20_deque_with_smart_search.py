
from collections import deque

input = "input1.txt"
input = "input2.txt"
grid = [list(line.strip()) for line in open(input)]

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
    
    for row in grid:
        print("".join(row))

dists = [[-1]*cols for _ in range(rows)]
count=0
q=deque([start])

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    cr,cc=q.popleft()
    for dr,dc in dirs:
        nr, nc = cr + dr, cc + dc
        if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]=="#" or dists[nr][nc] != -1 : continue
        dists[nr][nc] = dists[cr][cc]+1 
        q.append((nr,nc))
        
for r in range(rows):
    for c in range(cols):
        if dists[r][c] != -1:
            for nr,nc in ((r+2, c), (r,c+2)): #only look for half directions (right and down)
                if nr<0 or nc<0 or nr>=rows or nc>=cols or dists[nr][nc]==-1:continue
                if abs(dists[r][c]-dists[nr][nc])>=102: count+=1
                
print(count)
            
    

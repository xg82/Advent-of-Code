#Python
import pprint

mychar={}
myposition={}
lines,cols=0,0
# with open("input0.txt",'r') as inp:
# with open("input1.txt",'r') as inp:
with open("input2.txt",'r') as inp:
# with open("input3.txt",'r') as inp:
# with open("input4.txt",'r') as inp:
    for x, line in enumerate(inp):
        # line.strip()
        # print(line)
        cols=len(line)
        for y,char in enumerate(line.strip()):
            mychar.setdefault(char,set()).add((x,y))
            myposition[(x,y)]=char
            lines=y+1
            []
# pprint.pprint(mychar)
# pprint.pprint(myposition)
# print(lines, cols)
char_within_region = {}
for char, all_posions in mychar.items():
    #seperate each char into regions
    position=set()
    def search_for_char(pos):
        if myposition[pos] != char:
            return
        adjecent_positions=[(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1)]
        for next_position in adjecent_positions :
            if 0<=next_position[0]<lines and 0<=next_position[1]<cols and myposition[next_position]==char and next_position not in position:
                position.add(next_position)
                search_for_char(next_position)
        return position
    index = 0
    char_within_region[char] = {}
    char_within_region[char][index] = set()
    while(all_posions):
        each_position = list(all_posions)[0]
        position_got={each_position,}.union(search_for_char(each_position))
        char_within_region[char][index] = position_got
        all_posions -= position_got
        position=set() ####!!!!
        index += 1

with open("thedict.txt", 'w') as out:
    pprint.pprint(char_within_region, stream=out)

def cal_side(region):

    total_side_vertital=0
    side_found = False
    block_on_left = False
    block_on_right = False
    for y in range(cols+1):
        flag_for_block_side = 0
        side_change = True
        for x in range(lines):
            #check its left block
            block_on_left = True if y-1>=0 and (x,y-1) in region else False
            #check its right block
            block_on_right = True if y+1<=cols and (x,y)  in region else False
            #check if it is a side
            side_found=True if (block_on_left or block_on_right) and not (block_on_left and block_on_right) else False
            
            flag = 0
            if block_on_left and not block_on_right:
                flag = 1
            if block_on_right and not block_on_left:
                flag = 2
            if not side_found or (side_found and flag_for_block_side and flag_for_block_side != flag):  #consider block one side and next block on another side
                side_change = True
            flag_for_block_side = flag

            if side_found and side_change:  
                total_side_vertital+=1
                side_change = False
                
    # print(total_side_vertital)

    total_side_horizontal=0
    side_found = False
    block_on_top = False
    block_on_bottom = False
    for x in range(lines+1):
        flag_for_block_side = 0
        side_change = True
        for y in range(cols):
            #check its left block
            block_on_top = True if x-1>=0 and (x-1,y) in region else False
            #check its right block
            block_on_bottom = True if x+1<=lines and (x,y) in region else False
            #check if it is a side
            if (block_on_top or block_on_bottom) and not (block_on_top and block_on_bottom):
                side_found=True
            else:
                side_found=False

            flag = 0
            if block_on_top and not block_on_bottom:
                flag = 1
            if block_on_bottom and not block_on_top:
                flag = 2
            if not side_found:
                side_change = True
            if side_found and flag_for_block_side and flag_for_block_side != flag:
                side_change = True

            flag_for_block_side = flag

            if side_found and side_change:
                total_side_horizontal+=1
                side_change = False


    # print(total_side_horizontal)

    total = total_side_vertital+total_side_horizontal
    # print(total)
    return total
    
total_cost=0
for key, value in char_within_region.items(): #value - regions
    regions_cost = 0
    for region in value.values():
        area_region = len(region)
        region_perimeter = cal_side(region)
        regions_cost += region_perimeter * area_region

        # print(region, "\n", area_region, region_perimeter)

    total_cost += regions_cost

print(total_cost)
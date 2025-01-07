#Python
import pprint

def main():
    
    mychar={}
    myposition={}
    lines,cols=0,0
    # with open("input0.txt",'r') as inp:
    # with open("input1.txt",'r') as inp:
    with open("input2.txt",'r') as inp:
        for x, line in enumerate(inp):
            cols=len(line)
            for y,char in enumerate(line.strip()):
                mychar.setdefault(char,set()).add((x,y))
                myposition[(x,y)]=char
                lines=y+1
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
    
    # pprint.pprint(char_within_region)


    from itertools import combinations
    garden_dict = {}
    total_cost=0
    for key, value in char_within_region.items(): #value - regions
        regions_cost = 0
        for region in value.values():
            region_pairs = 0
            area_region = len(region)
            for position1, position2 in list(combinations(region, 2)):
                if position1 != position2:
                    pos = position1
                    if position2 in [(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0],pos[1]-1),(pos[0],pos[1]+1)]:
                        region_pairs+=1
            region_perimeter = area_region*4-region_pairs*2
            # print(key, area_region, region_pairs, region_perimeter)
            regions_cost += region_perimeter * area_region
        garden_dict[key] = (area_region, region_pairs, regions_cost)
        total_cost += regions_cost

    print(total_cost)


    # pprint.pprint(garden_dict)



if __name__ == "__main__":
    main()


    

#Python
import pprint

def main():
    
    mymap={}
    myposition={}
    lines,cols=0,0
    # with open("input1.txt",'r') as inp:
    with open("input2.txt",'r') as inp:
        for x, line in enumerate(inp):
            cols=len(line)
            for y,char in enumerate(line.strip()):
                mymap.setdefault(int(char),set()).add((x,y))
                myposition[(x,y)]=int(char)
                lines=y+1

    total_score=0
    for postion in mymap[0]:
        
        def steps(current_position, current_num,position_9s):
            if current_num==9:
                position_9s.add(current_position)
                return 
            adjecent_positions=[(current_position[0]-1,current_position[1]),(current_position[0]+1,current_position[1]),(current_position[0],current_position[1]-1),(current_position[0],current_position[1]+1)]
            for next_position in adjecent_positions:
                if 0<=next_position[0]<lines and 0<=next_position[1]<cols and myposition[next_position]==current_num+1:
                    steps(next_position,current_num+1,position_9s)
        
        position_9s=set()
        steps(postion,0,position_9s)
        # print(postion, ">",position_9s)
        total_score+=len(position_9s)

    print(total_score)


if __name__ == "__main__":
    main()


    

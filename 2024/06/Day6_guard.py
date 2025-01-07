#Python
import time
import random

def define_map():

# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
    
    Xmax=0
    Ymax=0
    # obs_position={(7,1),(1,2),(9,3),(2,4),(8,6),(3,7),(10,9),(5,10)}
    obs_position={}
    line_num=0
    with open("input1.txt",'r') as input:
    # with open("input2.txt",'r') as input:
        for line in input:
            line_num+=1
            for index, value in enumerate(line):
                if value=="#":
                    obs_position[(index+1,line_num)]=True
                elif value=="^":
                    start_position=(index+1,line_num)
        Xmax=len(line)
        Ymax=line_num
    # print(Xmax,Ymax)
    return obs_position, start_position, Xmax,Ymax


def next_step(obs_position,current_postion,current_direction):
    Xc,Yc=current_postion
    Xd,Yd=current_direction
    #next facing postion: Xf, Yf
    Xf, Yf = Xc, Yc
    Xf += 1 if Xd==1 else 0
    Xf -= 1 if Xd==-1 else 0
    Yf += 1 if Yd==1 else 0
    Yf -= 1 if Yd==-1 else 0
    
    #change direction if facing obstacle
    if (Xf, Yf) in obs_position:  
        if Xd==1:
            Xd=0
            Yd=1
        elif Yd==-1:
            Xd=1
            Yd=0
        elif Xd==-1:
            Xd=0
            Yd=-1
        elif Yd==1:
            Xd=-1
            Yd=0

    #make 1 step forward
    Xc += 1 if Xd==1 else 0
    Xc -= 1 if Xd==-1 else 0
    Yc += 1 if Yd==1 else 0
    Yc -= 1 if Yd==-1 else 0

    return (Xc,Yc),(Xd,Yd)


def draw_map(obs_position,visited_map,current_postion,current_direction, Xmax,Ymax):
    Xc,Yc=current_postion
    Xd,Yd=current_direction
    for y in range(1,Xmax+1):
        line=""
        for x in range(1,Ymax+1):
            if (x,y)==(Xc,Yc):
                if Xd==1:
                    line += " →"
                if Xd==-1:
                    line += " ←"
                if Yd==1:
                    line += " ↓"
                if Yd==-1:
                    line += " ↑"
            elif (x,y) in obs_position:
                line += " #"
            elif (x,y) in visited_map:
                line += " ."
            else:
                line += "  "
        print(line+"\n")


def case(obs_position, current_postion, current_direction, Xmax,Ymax):
    visited_map={}
    visited_map[current_postion]=True
    visited_distinct=1
    
    draw_map(obs_position,visited_map,current_postion,current_direction, Xmax,Ymax) #print initial map
    input("press to continue...")
    # print("Begain in 3 seconds...")
    # time.sleep(3)

    while True:
        current_postion, current_direction = next_step(obs_position,current_postion,current_direction)
        Xc,Yc=current_postion[0],current_postion[1]
        if 1 <= Xc <= Xmax and 1 <= Yc <= Ymax:
            print("-"*10,visited_distinct+1,"-"*10)
            if not (Xc,Yc) in visited_map:
                visited_map[(Xc,Yc)] = True
                visited_distinct += 1
            draw_map(obs_position,visited_map,current_postion,current_direction, Xmax,Ymax)
            time.sleep(1)
        else:
            break
    
    return visited_distinct


if __name__ == "__main__":
    
    obs_position,current_postion, Xmax,Ymax=define_map()

    # current_postion = (5,4) #initial position
    current_direction=(0,-1) #initial direction
    
    # current_postion = (1,9) # max of 42 distincts position
    # current_direction = (1,0) # max of 42 distincts direction

    # deirecions = ((1,0),(-1,0),(0,1),(0,-1))
    # while True:
    #     current_postion = (random.randint(1,10),random.randint(1,10)) #initial random position
    #     current_direction=random.choice(deirecions) #initial random direction
    #     if current_postion not in obs_position:
    #         break

    num=case(obs_position,current_postion,current_direction, Xmax,Ymax)
    print("total distincts visited is ",num)
    
    def max_distinct():
        total_case=0
        max_distinct=0
        max_distinct_start_positon=()
        max_distinct_start_direction=()
        for x in range(1,11):
            for y in range(1,11):
                if (x,y) in obs_position:
                    next
                for dir in ((1,0),(-1,0),(0,1),(0,-1)):
                    total_case += 1
                    distrinct=case(obs_position,(x,y),dir)
                    if max_distinct<distrinct:
                        max_distinct=distrinct
                        max_distinct_start_positon=(x,y)
                        max_distinct_start_direction=dir

        print (f"There are {total_case} cases.\n")
        print (f"Case with maximum disticts {max_distinct} is in position {max_distinct_start_positon} and direction {max_distinct_start_direction}\n")

    # max_distinct()

    

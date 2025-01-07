#Python
import time

def define_map():
    
    Xmax=0
    Ymax=0
    obs_position={}
    line_num=0
    # with open("input1.txt",'r') as input:
    with open("input2.txt",'r') as input:
        for line in input:
            line_num+=1
            for index, value in enumerate(line):
                if value=="#":
                    obs_position[(index+1,line_num)]=True
                elif value=="^":
                    start_position=(index+1,line_num)
        Xmax=len(line)
        Ymax=line_num
    return obs_position, start_position, Xmax,Ymax


def next_step(obs_position,current_postion,current_direction):
    Xc,Yc=current_postion
    Xd,Yd=current_direction

    while True:
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
        else:
            break

    #make 1 step forward
    Xc += 1 if Xd==1 else 0
    Xc -= 1 if Xd==-1 else 0
    Yc += 1 if Yd==1 else 0
    Yc -= 1 if Yd==-1 else 0

    return (Xc,Yc),(Xd,Yd)


def draw_map(obs_position,visited_map,current_postion,current_direction, Xmax,Ymax,
             position=None):
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
            elif (x,y) == position:
                line += " O" 
            elif (x,y) in obs_position:
                line += " #"
            elif (x,y) in visited_map:
                line += " x"
            else:
                line += " ."
        print(line+"\n")


def case(obs_position, current_postion, current_direction, Xmax,Ymax):
    visited_map={}
    visited_map[current_postion]=[current_direction]
    visited_distinct=1
    
    # draw_map(obs_position,visited_map,current_postion,current_direction, Xmax,Ymax) #print initial map
    # print("Begain in 3 seconds...")
    # time.sleep(3)

    while True:
        current_postion, current_direction = next_step(obs_position,current_postion,current_direction)
        Xc,Yc=current_postion[0],current_postion[1]
        if 1 <= Xc <= Xmax and 1 <= Yc <= Ymax:
            # print("-"*10,visited_distinct+1,"-"*10) #draw split line
            if (Xc,Yc) in visited_map:
                if current_direction in visited_map[(Xc,Yc)]:
                    return -1,visited_map
                else:
                    visited_map[(Xc,Yc)].append(current_direction)
            else:
                visited_map[(Xc,Yc)]=[current_direction]
                visited_distinct += 1
            # draw_map(obs_position,visited_map,current_postion,current_direction, Xmax,Ymax)
            # time.sleep(0.5)
        else:
            break
    
    return visited_distinct, visited_map


if __name__ == "__main__":
    
    obs_position,current_postion, Xmax,Ymax=define_map()

    # current_postion = (5,4) #initial position
    current_direction=(0,-1) #initial direction
    visited_distinct, visited_map=case(obs_position,current_postion,current_direction, Xmax,Ymax)
    print("Initial distinct is :",visited_distinct)

    loop_amount=0
    for position in visited_map:
    # for position in {(x,y) for x in range(1, Xmax+1) for y in range(1,Ymax+1)}:
        ori_map=obs_position.copy()
        if position == current_postion:
            continue
        ori_map[position]=True
        distinct, map=case(ori_map,current_postion,current_direction, Xmax,Ymax)
        if distinct==-1:
            loop_amount+=1
            # print("-"*20)
            # draw_map(ori_map,visited_map,current_postion,current_direction, Xmax,Ymax,position)
            # input("any key...")
    print("All possible trapped loop amount is :",loop_amount)

    

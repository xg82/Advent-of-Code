#Python
import time
import random,re

def define_initial_status():


    robot_positon_vel= []
    # with open("input1.txt",'r') as input:
    with open("input2.txt",'r') as input:
        for line in input:
            m = re.search(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)',line)
            robot_positon_vel.append(((int(m.group(1)),int(m.group(2))), (int(m.group(3)),int(m.group(4))) ))

    return robot_positon_vel


if __name__ == "__main__":
    
    pos_vel_list = define_initial_status() #list of all robots [((x,y),(vx,vy)), ((x,y),(vx,vy)), ...]
    
    Xmax=101
    Ymax=103
        
    target_steps = 0
    
    while (True):
        step = 1
        target_steps += step
        for index, robot in enumerate(pos_vel_list):
            pos, vel = robot
            x, y = pos
            vx, vy = vel

            x_new = (x+vx*step)%Xmax
            y_new = (y+vy*step)%Ymax
            pos_vel_list[index] = ((x_new,y_new),vel)
            
        position_set=set([pos[0] for pos in pos_vel_list])
        
        depth = 5
        found = 0
        
        for y in range(Ymax):
            for x in range(Xmax):
                if depth<x<Xmax-depth and y<Ymax-depth and (x,y) in position_set:
                    for i in range(1,depth):
                        if (x-i, y+i) not in position_set or (x+i,y+i) not in position_set: 
                            found = 0
                            break
                        found = y
                if found:
                    break
            if found:
                break

        if found:           
            file = open("out.txt",'w') 
            file.write(f"total steps: {target_steps}\n")
            file.write(f"Tree top in line: {found}\n")
            for y in range(Ymax):
                line=""
                for x in range(Xmax):
                    if (x,y) in position_set:
                        line+="*"
                    else:
                        line+=" "
                file.write(f"{y:>3d} {line}\n")
            file.close()
            
            print(target_steps, found)
            input("any key to continue...")
    





















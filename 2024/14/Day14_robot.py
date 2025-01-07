#Python
import time
import random,re

def define_initial_status():

# p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
    
    robot_positon_vel= []
    # with open("input1.txt",'r') as input:
    with open("input2.txt",'r') as input:
        for line in input:
            m = re.search(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)',line)
            robot_positon_vel.append(((int(m.group(1)),int(m.group(2))), (int(m.group(3)),int(m.group(4))) ))

    return robot_positon_vel



if __name__ == "__main__":
    
    pos_vel_set = define_initial_status()

    Xmax=11
    Ymax=7
    
    Xmax=101
    Ymax=103
    
    target_steps = 100
    
    final_pos_vel = {}
    for robot in pos_vel_set:
        pos, vel = robot
        x, y = pos
        vx, vy = vel
        
        x = (x+vx*target_steps)%Xmax
        y = (y+vy*target_steps)%Ymax
        final_pos_vel.setdefault((x,y),0)
        final_pos_vel[(x,y)]+=1
    
    q1,q2,q3,q4 =0,0,0,0
    file = open("out.txt",'w') 
    for y in range(Ymax):
        line=""
        for x in range(Xmax):
            xmid=(Xmax-1)/2
            ymid=(Ymax-1)/2
            if (x,y) in final_pos_vel:
                if x<xmid and y<ymid:
                    q1+=final_pos_vel[(x,y)]
                elif x>xmid and y<ymid:
                    q2+=final_pos_vel[(x,y)]            
                elif x<xmid and y>ymid:
                    q3+=final_pos_vel[(x,y)]  
                elif x>xmid and y>ymid:
                    q4+=final_pos_vel[(x,y)]   
                line+=str(final_pos_vel[(x,y)])
            else:
                line+=" "
        # print(line,"\n")
        file.write(f"{line}\n")
    
    factor = q1*q2*q3*q4
    print(q1,q2,q3,q4)
    print(factor)






















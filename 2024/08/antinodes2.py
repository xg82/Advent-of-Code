#Python
import re,itertools
from sympy import symbols

def main():
    
    antennas={}
    antinodes=set()
    lines,cols=0,0
    # with open("input1.txt",'r') as inp:
    with open("input2.txt",'r') as inp:
        for x, line in enumerate(inp):
            cols=len(line)
            for y,char in enumerate(line):
                if re.match(r'\w',char):
                    antennas.setdefault(char,set()).add((x,y))
                lines=y+1

    for key,value in antennas.items():
        if len(value)>1:
            combins=itertools.combinations(value,2)
            for pair in combins:
                x1,y1=pair[0]
                x2,y2=pair[1]
                t=symbols('t',real=True)
                x=x1+t*(x2-x1)
                y=y1+t*(y2-y1)
                a=min(lines, cols)
                for v in range(-a,a):
                    x_v=x.subs(t,v)
                    y_v=y.subs(t,v)
                    if x_v.is_integer and y_v.is_integer and 0<=x_v<lines and 0<=y_v<cols:
                        antinodes.add((int(x_v),int(y_v)))

    print(len(antinodes))


if __name__ == "__main__":
    main()


    

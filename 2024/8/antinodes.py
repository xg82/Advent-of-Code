#Python
import re,itertools
from sympy import symbols, Eq, solve, sqrt

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
                # t=symbols('t',real=True)
                # x=x1+t*(x2-x1)
                # y=y1+t*(y2-y1)
                # solutions=solve(Eq((x-x1)**2+(y-y1)**2,((x-x2)**2+(y-y2)**2)/4),t)
                # solutions=solve(Eq((x-x1)**2+(y-y1)**2,((x-x2)**2+(y-y2)**2)*4),t)
                # print(solutions)
                for t in [2/3,2,-1,1/3]:  #possible solution for parameter t
                    x=x1+(x2-x1)*t
                    y=y1+(y2-y1)*t
                    if x%1==0 and y%1==0 and 0<=x<lines and 0<=y<cols:
                        print(x,y)
                        antinodes.add((x,y))

    print(len(antinodes))


if __name__ == "__main__":
    main()


    

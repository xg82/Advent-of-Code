#python


def main():
    file_array=[]
    # with open("input1.txt",'r') as input:
    with open("input2.txt",'r') as input:
        for line in input:
            file_array.append(line.strip())

    total_xmas=0

    #horizontal check
    for line in file_array:
        for x in range(0,len(line)-3):
            if line[x:x+4] in ['XMAS','SAMX']:
                total_xmas+=1
    
    print(total_xmas)

    #vertical check
    for x in range(0,len(file_array[0])):
        for y in range(0, len(file_array)-3):
            word4=''.join(file_array[i][x] for i in range(y, y + 4))
            if word4 in ['XMAS','SAMX']:
              total_xmas+=1
            # print(word4)

    print(total_xmas)

    #diagonal check to right
    for x in range(0, len(file_array[0])-3):
        for y in range(0, len(file_array)-3):
            word4=file_array[x][y]+file_array[x+1][y+1]+file_array[x+2][y+2]+file_array[x+3][y+3]
            if word4 in ['XMAS','SAMX']:
              total_xmas+=1
            # print(word4)            

    print(total_xmas)

    #diagonal check to left
    for x in range(0, len(file_array[0])-3):
        for y in range(3, len(file_array)):
            word4=file_array[x][y]+file_array[x+1][y-1]+file_array[x+2][y-2]+file_array[x+3][y-3]
            if word4 in ['XMAS','SAMX']:
              total_xmas+=1
            # print(word4)            

    print(total_xmas)

    total_X_MAX=0
    for x in range(1, len(file_array)-1):
        for y in range(1, len(file_array[0])-1):
            if file_array[x][y]=="A":
                if {file_array[x-1][y-1],file_array[x+1][y+1]}=={"M","S"} and {file_array[x-1][y+1],file_array[x+1][y-1]}=={"M","S"}:
                    total_X_MAX+=1    

    print(total_X_MAX)

if __name__ == "__main__":
    main()
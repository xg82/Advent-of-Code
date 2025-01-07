#python


def main():
    total_safe=0
    with open("input1.txt",'r') as inp:
    # with open("input2.txt",'r') as inp:
        for line in inp:
            num=list(map(int,line.strip().split()))

            #incresing
            safe_flag=True
            if num[1]>num[0]:
                for i in range(len(num)-1):
                    if not num[i+1]-3<=num[i]<=num[i+1]-1:
                        safe_flag=False
                        continue

            #decreading
            elif num[1]<num[0]:
                for i in range(len(num)-1):
                    if not num[i]-3<=num[i+1]<=num[i]-1:
                        safe_flag=False
                        continue
            else:
                continue

            if safe_flag:
                total_safe+=1
                # print(line)
                # input("pause..")

    
    print(total_safe)





if __name__ == "__main__":
    main()
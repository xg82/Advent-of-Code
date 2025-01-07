#python


def main():
    total_safe=0
    # with open("input1.txt",'r') as inp:
    with open("input2.txt",'r') as inp:
        for line in inp:

            num=list(map(int,line.strip().split()))

            if check_true(num):
                total_safe+=1
                # print(line)
                # input("pause..")
            else:
                remove_char=0
                while remove_char<len(num):
                    l=num.copy()
                    l.pop(remove_char)
                    if check_true(l):
                        total_safe+=1
                        # print(num, ">", l)
                        # input("pause..")
                        break
                    remove_char+=1
    
    print(total_safe)


def check_true(num):

    safe_flag=True

    #incresing
    if num[1]>num[0]:
        for i in range(len(num)-1):
            if not num[i+1]-3<=num[i]<=num[i+1]-1:
                safe_flag=False
                break
    #decreading
    elif num[1]<num[0]:
        for i in range(len(num)-1):
            if not num[i]-3<=num[i+1]<=num[i]-1:
                safe_flag=False
                break

    else:
        safe_flag=False

    return safe_flag

if __name__ == "__main__":
    main()

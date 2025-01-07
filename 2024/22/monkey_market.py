def cal(sec):
    num = sec * 64
    sec ^= num
    sec %= 16777216

    num = sec // 32
    sec ^= num
    sec %= 16777216 

    num = sec * 2048
    sec ^= num
    sec %= 16777216 

    return sec


inp='inp1.txt'
inp='inp2.txt'
nums = [int(line.strip()) for line in open(inp)]

lastdigit_list = []

for num in nums:
    lastdigit_dict = {}
    secret = num
    l_list = [secret%10]
    for _ in range(2000):
        val =  cal(secret)
        l_list.append(val%10)
        secret = val
    for i in range(4,len(l_list)):
        seq = (l_list[i] - l_list[i-1], l_list[i-1] - l_list[i-2], l_list[i-2] - l_list[i-3], l_list[i-3] - l_list[i-4])[::-1]  
        lastdigit_dict.setdefault(seq, l_list[i])
    lastdigit_list.append(lastdigit_dict)

seq_times = {}
for buyer in lastdigit_list:
    for key, value in buyer.items():
        seq_times.setdefault(key, 0)
        seq_times[key] += value

max_key, max=None, 0
for key, val in seq_times.items():
    if val > max:
        max = val
        max_key = key
print(max_key, max)

    


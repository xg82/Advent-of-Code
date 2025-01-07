inp = "inp1.txt"
inp = "inp2.txt"

lines = [ line.strip() for line in open(inp) ]

base = {}
gate = {}
for line in lines:
    if ":" in line:
        base[line.split(":")[0]] = int(line.split(":")[1].strip())
    elif "->" in line:
        sp = line.split(" ")
        gate[sp[4]] = ((sp[0], sp[2]), sp[1])

def cal(a,b,c):
    if c == "AND":
        return a & b
    elif c == "OR":
        return a | b
    elif c == "XOR":
        return a ^ b

x_str = ''.join(str(value) for key, value in base.items() if key.startswith("x"))[::-1]
y_str = ''.join(str(value) for key, value in base.items() if key.startswith("y"))[::-1]
z_soll = bin((int(x_str, 2) + int(y_str, 2)))[2:]

while (gate):
    for key in list(gate.keys()):
        gate1, gate2 = gate[key][0]
        method = gate[key][1]
        if gate1 in base and gate2 in base:
            base[key] = cal(base[gate1], base[gate2], method)
            del gate[key]

z_dict = {key:value for key, value in base.items() if key.startswith("z")}
z_str = ''.join(str(z_dict[key]) for key in sorted(z_dict, reverse=True))
z_decimal = int(z_str, 2)
print(z_decimal)
print("\n")

print(z_soll)
print(z_str)

with open("all_value1.txt", 'w') as f:
    f.write("\n".join(f"{key} -> {value}" for key, value in sorted(base.items())))

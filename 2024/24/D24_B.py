#  M (intermediate sum)
#  N (intermediate carry)
#  R (carry for intermediate sum)
#  Z (final sum)
#  C (final carry)

def swap(a, b):
    pairs.append((a, b))
    key_a, key_b = (key for key, value in wires_gate.items() if value in (a, b))
    wires_gate[key_a], wires_gate[key_b] = wires_gate[key_b], wires_gate[key_a]

joints = open("inp2.txt").read().split("\n\n")[1]
gate_list = [(i.split(), j) for i, j in (k.split(" -> ") for k in joints.splitlines())]
wires_gate = {(frozenset(wires)): gate for wires, gate in gate_list}
pairs = []
end = False
z_amount = sum(value[1].startswith("z") for value in gate_list)
while not end:
    C = wires_gate[frozenset(("x00", "AND", "y00"))]
    for i in range(1, z_amount):
        xi, yi, zi = f"x{i:02}", f"y{i:02}", f"z{i:02}"
        M = wires_gate.get(frozenset((xi, "XOR", yi)))
        N = wires_gate.get(frozenset((xi, "AND", yi)))
        R = wires_gate.get(frozenset((M, "AND", C)))
        Z = wires_gate.get(frozenset((M, "XOR", C)))
        C = wires_gate.get(frozenset((N, "OR", R)))
        if C == "z45":
            end = True;  break
        if not Z:
            swap(M, N);  break
        if Z != zi:
            swap(Z, zi); break

print(pairs)
print(",".join(sorted(p for wire in pairs for p in wire)))


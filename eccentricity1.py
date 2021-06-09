from comb import comb
from itertools import permutations
# breadth = (2.3, 2.79, 2.90)
# load = (554, 700, 700)
combination = comb(width=15)
comb0 = combination[2]  # reminder - iterate through all combination
veh = []    # all vehicles <'a'><'b'><'c'> as indices for <classA><70RW><70RT>
index = bytes('a', 'utf-8')
for i in comb0:
    for j in range(i):
        veh.append(chr(index[0]))
    index = bytes(chr(index[0] + 1), 'utf-8')
perm = permutations(veh)
print(f'{comb0} >> {set(list(perm))}')

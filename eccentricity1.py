from comb import comb
from itertools import permutations
import DL_Section as dls
# breadth = (2.3, 2.79, 2.90)
# load = (554, 700, 700)


class load:
    def __init__(self,value):
        self.j=value

        if self.j=="a":
            self.name="Class A"
            self.ws = 1800
            self.lefclr = 150+self.ws/2
            self.g = 1200
            self.gs=self.g+self.ws
            self.q=114
        elif self.j=="b":
            self.name = "70R Wheeled"
            self.ws = 2600
            self.lefclr = 1200 + self.ws / 2
            self.gs=7000/2
            self.q = 700
        elif self.j=="c":
            self.name = "70R Tracked"
            self.ws = 2060
            self.lefclr = 1200 + self.ws / 2
            self.gs=7000/2
            self.q = 700


kerb_len=dls.length[10]
"""Length of Kerb"""

"""Position of edges of kerb"""
left_pos=dls.pos[10][0]
right_pos=dls.pos[13][0]

"""Distance of centroidal axis from leftmost edge"""
cl=dls.axes[0]-left_pos

"""Carriageway width"""
# cw=right_pos-(left_pos+kerb_len)
cw=15
dist=[]
e=[]


combination = comb(width=15)
perco=[]

for i in range(len(combination)):
    comb0=combination[i]
    veh = []  # all vehicles <'a'><'b'><'c'> as indices for <classA><70RW><70RT>
    index = bytes('a', 'utf-8')
    for i in comb0:
        for j in range(i):
            veh.append(chr(index[0]))
        index = bytes(chr(index[0] + 1), 'utf-8')
    perm = permutations(veh)
    p=list(set(perm))
    for i in range(len(p)):
        perco.append(p[i])
print(perco)

for i in range(len(perco)):
    e1=0
    laspos=0
    for j in range(len(perco[i])):
        lod=load(perco[i][j])
        if j==0:
            if lod.name=="Class A":
                laspos=(kerb_len+lod.lefclr)
            else:
                laspos=(7250-3500)

        elif j==(len(perco[i])-1) and (lod.name=="70R Wheeled" or lod.name=="70R Tracked"):
            laspos=(cw+kerb_len-lod.lefclr)
        else:
            if lod.name=="Class A":
                laspos+=lod.gs
            else:
                laspos+=7000
        e1 += (laspos) * lod.q
    a1=perco[i].count('a')
    a2=perco[i].count('b')
    a3=perco[i].count('c')
    e.append(e1/(1000*(a1*114+a2*700+a3*700)))

print(e)

import pandas as pd
from comb import comb
from itertools import permutations
import csv


# breadth = (2.3, 2.79, 2.90)
# load = (554, 700, 700)


class load:
    def __init__(self,value):
        self.j=value

        if self.j=="a":
            self.name="Class A"
            self.ws = 1.9
            self.lefclr = 0.150+self.ws/2
            self.g = 1.2
            self.gs=self.g+self.ws
            self.q=114
        elif self.j=="b":
            self.name = "70R Wheeled"
            self.ws = 7
            self.lefclr = 1.2 + 2.6/2
            self.gs=self.ws
            self.q = 700
        elif self.j=="c":
            self.name = "70R Tracked"
            self.ws = 7
            self.lefclr = 1.2 + 2.06/2
            self.gs=self.ws
            self.q = 700

df=pd.read_csv('data/DL.csv',delimiter=',').T
dfl=df.values.tolist()
kerb_len=dfl[10][2]

# """Length of Kerb"""
#
# """Position of edges of kerb"""
left_pos=dfl[10][4]
right_pos=dfl[13][4]

"""Carriageway width"""
# cw=right_pos-left_pos-kerb_len


"""Distance of centroidal axis from leftmost edge"""
# cl=(dls.axes[0]-left_pos+kerb_len)
cl=7.5

cw=15
dist=[]
e=[]
cla=[]
cl70rw=[]
cl70rt=[]
# print(e)
combination = comb(width=cw)
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
# print(perco)

for i in range(len(perco)):
    e1=0
    laspos=0
    for j in range(len(perco[i])):
        lod=load(perco[i][j])
        if j==0:
            e1 += (lod.lefclr) * lod.q
            if lod.name=="Class A":
                laspos = (lod.lefclr+lod.ws/2+lod.g)
            else:
                laspos=(7.25)
        else:
            e1 += (laspos+lod.ws/2) * lod.q
            laspos+=lod.gs
    if len(perco[i]) == 1 and lod.name == "Class A":
        e1 += (laspos + lod.ws / 2 + (cw - (laspos + lod.ws / 2)) / 2) * (cw - (laspos + lod.ws / 2)) * 0.5
    a1=perco[i].count('a')
    cla.append(a1)
    a2=perco[i].count('b')
    cl70rw.append(a2)
    a3=perco[i].count('c')
    cl70rt.append(a3)
    if len(perco)==1:
        e.append(cl-(e1 / (a1*114 + a2*700 + a3*700+500)))
    else:
        e.append(cl-(e1/(a1*114+a2*700+a3*700)))

df=pd.DataFrame({
    'Class A':cla,
    '70R Wheeled':cl70rw,
    '70R Tracked':cl70rt,
    'Eccentricity':e }).T
df.to_csv('data/eccentricity.csv',index_label="Load Combinations")


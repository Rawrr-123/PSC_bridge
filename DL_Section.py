import csv
import pandas as pd
from box_girder import sections as sc

# Positions are calculated from bottom left grid space of shape

A_sum = 0
A_x = 0
A_y = 0
obj = []
length = []
height = []
pos = []
orient = []
area = []
moi = []
center = []
centroid = []

with open('data/sect.csv', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print(row)
        obj.append((row[0]))
        length.append(float(row[1]))
        height.append(float(row[2]))
        pos.append([float(row[3]), float(row[4])])
        orient.append(float(row[5]))


class shape:
    def __init__(self, name, length, height, pos):
        self.name = name
        self.length = length
        self.height = height
        self.pos = pos

    @property
    def area(self):
        if self.name == "triangle":
            return (self.length * self.height) / 2
        elif self.name == "rectangle":
            return (self.length * self.height)

    @property
    def MOI(self):
        if self.name == "triangle":
            return [((self.length * self.height ** 3) / 36), ((self.length ** 3 * self.height) / 36)]
        elif self.name == "rectangle":
            return [((self.length * self.height ** 3) / 12), ((self.length ** 3 * self.height) / 12)]

    @property
    def Center(self):
        if self.name == "triangle":

            return [self.length / 3, self.height / 3]
        elif self.name == "rectangle":
            return [self.length / 2, self.height / 2]


for i in range(len(obj)):
    a = shape(obj[i], length[i], height[i], pos[i])
    area.append(a.area)
    moi.append(a.MOI)
    center.append(a.Center)
    A_sum = A_sum + a.area
    if obj[i] == "triangle":
        if orient[i] == 1:
            # top right
            A_x = a.area * (pos[i][0] + length[i] - a.Center[0]) + A_x
            A_y = a.area * (pos[i][1] + height[i] - a.Center[1]) + A_y
            centroid.append([(pos[i][0] + length[i] - a.Center[0]), (pos[i][1] + height[i] - a.Center[1])])
        elif orient[i] == 2:
            # bottom left
            A_x = a.area * (pos[i][0] + a.Center[0]) + A_x
            A_y = a.area * (pos[i][1] + a.Center[1]) + A_y
            centroid.append([(pos[i][0] + a.Center[0]), (pos[i][1] + a.Center[1])])
        elif orient[i] == 3:
            # top left
            A_x = a.area * (pos[i][0] + a.Center[0]) + A_x
            A_y = a.area * (pos[i][1] + height[i] - a.Center[1]) + A_y
            centroid.append([(pos[i][0] + a.Center[0]), (pos[i][1] + height[i] - a.Center[1])])
        elif orient[i] == 4:
            # bottom right
            A_x = a.area * (pos[i][0] + length[i] - a.Center[0]) + A_x
            A_y = a.area * (pos[i][1] + a.Center[1]) + A_y
            centroid.append([(pos[i][0] + length[i] - a.Center[0]), (pos[i][1] + a.Center[1])])
    elif obj[i] == "rectangle":
        A_x = a.area * (pos[i][0] + a.Center[0]) + A_x
        A_y = a.area * (pos[i][1] + a.Center[1]) + A_y
        centroid.append([(pos[i][0] + a.Center[0]), (pos[i][1] + a.Center[1])])
axes = [(A_x / A_sum), (A_y / A_sum)]
# print(A_sum)
# print (axes)
I_x = 0
I_y = 0
for i in range(len(obj)):
    h_x = int((centroid[i][0] - axes[0]))
    h_y = abs((centroid[i][1] - axes[1]))
    I_x = area[i] * h_x ** 2 + I_x
    I_y = area[i] * h_y ** 2 + I_y
# print ("The principal moment of inertia of section about centroidal (x,y) axes:",axes," is ",[I_x,I_y])

PDL_load = A_sum * 25
PDL_seperate = [a * 25 for a in area]
# print(dead)
# dl_moment=[]
ODL_load = (length[10] + length[13]) * 0.3 * 25 + 4
cw = (pos[13][0] - pos[10][0] + length[10])
Surfl_load = cw * 0.1 * 22

span = 50
supl = 0
if span <= 50:
    supl = 500 / 100
elif 7.5 < span <= 30:
    supl = ((500 - (40 * span - 300) / 9) / 100)
elif span > 30:
    supl = ((500 - 260) + (4800 / span)) * (16.5 - max(length[10], length[13])) / 1500

pdld = supl * (length[10] + length[13])

# larm=[]
# for i in range(len(obj)):
#     dl_moment.append((area[i])*25*(abs(centroid[i][0]-axes[0])))
#     larm.append(abs(centroid[i][0]-axes[0]))

CentroidalX, CentroidalY = map(list, zip(*centroid))
MOIX, MOIY = map(list, zip(*moi))
posx, posy = map(list, zip(*pos))
df = pd.DataFrame({
    'Shape': obj,
    'Length': length,
    'Height': height,
    'Grid X': posx,
    'Grid Y': posy,
    'Area': area,
    'Centroidal X': CentroidalX,
    'Centroidal Y': CentroidalY,
    'I-X': MOIX,
    'I-Y': MOIY,
    'Dead Loads': PDL_seperate,
    # 'Lever Arm':larm,
    # 'Dead Load Moments':dl_moment

}).T
PDL = []
ODL = []
SufDL = []
PedL = []

for i in range(len(sc)):
    alls = (sc[i] * span / 2) - (sc[i] ** 2 / 2)
    PDL.append(alls * PDL_load)
    ODL.append(alls * ODL_load)
    SufDL.append(alls * Surfl_load)
    PedL.append(alls * pdld)

df2 = pd.DataFrame({
    'Bridge Centroid': axes,
    'Centroidal MOI': list((I_x, I_y)),
    # 'Sum of Dead Load Moment':sum(dl_moment
}).T

df3 = pd.DataFrame({'Section at': sc, 'Dead Load': PDL, 'Other Loads': ODL, 'Surface Loads': SufDL,
                    'Pedestrian Load': PedL

                    }, index=sc)
pd.concat([df, df2], axis=0).to_csv('outputs/DL.csv')
df3.to_csv('outputs/Moments.csv', index_label="Section at")
# print("Dead load per m length is:",Dead_Loads)

df4=pd.DataFrame([PDL_load*span,ODL_load*span,Surfl_load*span,pdld*span],columns=['Loads'],index=['Dead Load','Other Load','Surface Load','Pedestrian load']
)
df4.to_csv('outputs/DL_for_Seismic.csv')
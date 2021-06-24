from bridge_specs import *

PDL_load = A_sum * 25
PDL_seperate = [a * 25 for a in area]
# print(dead)
# dl_moment=[]
ODL_load = (length[10] + length[13]) * 0.3 * 25 + 4

Surfl_load = cw * 0.1 * 22

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
a=[PDL_load*span/2,PDL_load*span/2,PDL_load*span]
b=[ODL_load*span/2,ODL_load*span/2,ODL_load*span]
c=[Surfl_load*span/2,Surfl_load*span/2,Surfl_load*span]
d=[pdld*span/2,pdld*span/2,pdld*span]
df4=pd.DataFrame([a,b,c,d],columns=['Left','Right','Sum'],index=['Dead Load','Other Load','Surface Load','Pedestrian load']
)
df4.to_csv('outputs/DL_for_Seismic.csv')
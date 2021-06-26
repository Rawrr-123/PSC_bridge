from bridge_specs import box,bearing
    # span,cw,l_kerblen,r_kerblen,area_sum,sc
import pandas as pd

span=box.span
cw=box.cw
l_kerblen=box.l_kerblen
r_kerblen=box.r_kerblen
area_sum=box.area_sum
sc=box.sc



PDL_load = area_sum * 25
# PDL_seperate = [a * 25 for a in area]
# print(dead)
# dl_moment=[]
ODL_load = (l_kerblen+r_kerblen) * 0.3 * 25 + 4

Surfl_load = cw * 0.1 * 22

supl = 0
if span <= 50:
    supl = 500 / 100
elif 7.5 < span <= 30:
    supl = ((500 - (40 * span - 300) / 9) / 100)
elif span > 30:
    supl = ((500 - 260) + (4800 / span)) * (16.5 - max(length[10], length[13])) / 1500

pdld = supl * (l_kerblen+r_kerblen)

# larm=[]
# for i in range(len(obj)):
#     dl_moment.append((area[i])*25*(abs(centroid[i][0]-axes[0])))
#     larm.append(abs(centroid[i][0]-axes[0]))


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


df3 = pd.DataFrame({'Section at': sc, 'Dead Load': PDL, 'Other Loads': ODL, 'Surface Loads': SufDL,
                    'Pedestrian Load': PedL

                    }, index=sc)

df3.to_csv('outputs/Moments.csv', index_label="Section at")
# print("Dead load per m length is:",Dead_Loads)
a=[PDL_load*span/2,PDL_load*span/2,PDL_load*span]
b=[ODL_load*span/2,ODL_load*span/2,ODL_load*span]
c=[Surfl_load*span/2,Surfl_load*span/2,Surfl_load*span]
d=[pdld*span/2,pdld*span/2,pdld*span]
df4=pd.DataFrame([a,b,c,d],columns=['RL','RR','Sum'],index=['Dead Load','Other Load','Surface Load','Pedestrian load']
)
df4.to_csv('outputs/DL_for_Seismic.csv')
# %%
import pandas as pd
import csv
from reaction import bm_udl
from irc6_2007 import ped_ll
import math
from Cross import Cross_section,cables,Dead_Load,expansion_calc,excel_loads
# from allinput import main_input

# %%

"""INPUTS SECTION"""

"""FOR CROSS SECTION"""
length=[]
height=[]


#####################################################################################################################

"""GUI INPUT OF BRIDGE SECTION LENGTHS AND HEIGHTS"""


df=pd.read_excel('data/box.xlsx',index_col=None,header=None)



height=df.values.tolist()[0]
length=df.values.tolist()[1]

df1=pd.read_excel('data/span.xlsx',index_col=None,header=None)
# print(df1)
span = int(df1.iloc[1,0])
no = 9

""""distance form left of 9 divisions of section"""
sc=[(j)/(no-1)*span for j in range(no)]

###############################################################################################
"""FOR DEAD LOAD MOMENTS INPUTS"""




cw=6
l_kerblen=0.6
r_kerblen=0.6





loads=["PDL","ODL","SIDL","PEDL"]


# %%
"""Creation of required cross section with length and height inputs"""
section=Cross_section(length,height)


"""Creation of cable properties """
# cable=cables(35,14,section)


"""Assigning section with cable """
section1=Cross_section(length,height)
section1.cableprop=cables(35,14,section).cablepos(0,50)

# print(section1.cableprop)


I=[]
ymax=[]
ymin=[]
area_sum=[]
cable_positions=[]

"""Cross Section values for given no of divisions """
for i in range(len(sc)):
    cable=cables(35,14,section)
    section.expansion_width=expansion_calc(span,sc[i],cable)    
    I.append(section.I)    
    ymax.append(section.ymax)
    ymin.append(section.ymin)
    area_sum.append(sum(section.section_area))
    cable_positions.append(cable.cablepos(sc[i],span))




PDL=[]
ODL=[]
PEDL=[]
SIDL=[]

"""Calculation of loads """
for i in range(len(sc)):
    PDL.append(Dead_Load('PDL',area_sum[i],sc[i],span,l_kerblen+r_kerblen,0.3,0.065,6,2,I[i],ymax[i],ymin[i]))
    ODL.append(Dead_Load('ODL',area_sum[i],sc[i],span,l_kerblen+r_kerblen,0.3,0.065,6,2,I[i],ymax[i],ymin[i]))
    PEDL.append(Dead_Load('PEDL',area_sum[i],sc[i],span,l_kerblen+r_kerblen,0.3,0.065,6,2,I[i],ymax[i],ymin[i]))
    SIDL.append(Dead_Load('SIDL',area_sum[i],sc[i],span,l_kerblen+r_kerblen,0.3,0.065,6,2,I[i],ymax[i],ymin[i]))


excel_loads(PDL,ODL,PEDL,SIDL,sc,span)





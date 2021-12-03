from tkinter.constants import FALSE
import pandas as pd
import csv
from calcs import calc_area,calc_moi,calc_centroid,composite_centroid,calc_Ah2,i_composite
from bridge_specs import box
# import tkinter as tk
# from PIL import Image,ImageTk
from allinput import allinput
################################################################################

length=[]
height=[]


##############################################################################



if False:
    allinput()

df=pd.read_excel('Saved Inputs/box.xlsx',index_col=None,header=None)
height=df.values.tolist()[0]
length=df.values.tolist()[1]

##################################################################################

"""For Box Cross Section"""


##################################################################################

"""Box Dim Inputs"""
# pillar_len=0.6
# pillar_hei=3.2
# botslab_len=2.4
# botslab_hei=0.5
# topslab_len=2.4
# topslab_hei=0.3
# rec_cant_length=1.8
# rec_cant_height=0.15
# lef_kerb_len=0.6
# lef_kerb_hei=0.3
# rig_kerb_len=0.6
# rig_kerb_hei=0.3
# tri_cant_len=1.8
# tri_cant_hei=0.3
# chamfer_len=0.45
# chamfer_hei=0.15


"""Fixed Data for bridge particulars"""
# ----------------------------------------------------------------------------------

name=['left Pillar','right pillar','bottom slab','top slab','left cantilever','right cantilever','left kerb','right kerb',
      'left triangle','right triangle','left top fillet','right top fillet','left bottom fillet','right bottom fillet']
                  #
                  # \--------|                  |\                  |--------/                /|
                  #  \       |                  | \                 |       /                / |
                  #   \      |                  |  \                |      /                /  |
                  #    \     |                  |   \               |     /                /   |
                  #     \    |                  |    \              |    /                /    |
                  #      \   |                  |     \             |   /                /     |
                  #       \  |                  |      \            |  /                /      |
                  #        \ |                  |       \           | /                /       |
                  #         \|                  |________\          |/                /________|
                  #   triangle-1                triangle_2          triangle_3        triangle_4

obj=['rectangle','rectangle','rectangle','rectangle','rectangle','rectangle','rectangle','rectangle','triangle_1',
     'triangle_3','triangle_3','triangle_1','triangle_2','triangle_4']





"""Position from left bounding box"""
pos=[[3.5,3.5]]#left pillar
pos.append([pos[0][0]+length[0]+length[2],pos[0][1]])#right pillar
pos.append([pos[0][0]+length[0],pos[0][1]])#bottom slab
pos.append([pos[0][0]+length[0],pos[0][1]+height[0]-height[3]])#top slab
pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0]-height[4],4)])#left cantilever
pos.append([round(pos[0][0]+length[0]+length[3]+length[1],4),round(pos[0][1]+height[0]-height[5],4)])#right cantilever
pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0],4)])#left kerb
pos.append([round(pos[0][0]+length[0]+length[3]+length[1]+length[5]-length[7],4),round(pos[0][1]+height[0],4)])#right kerb
pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0]-height[4]-height[8],4)])#left triangle
pos.append([round(pos[0][0]+length[0]+length[3]+length[1],4),round(pos[0][1]+height[0]-height[5]-height[9],4)])#right triangle
pos.append([round(pos[0][0]+length[0],4),round(pos[0][1]+height[0]-height[3]-height[10],4)])#left top fillet
pos.append([round(pos[0][0]+length[0]+length[3]-length[11],4),round(pos[0][1]+height[0]-height[3]-height[10],4)])#right top fillet
pos.append([round(pos[0][0]+length[0],4),round(pos[0][1]+height[2],4)])#left bottom fillet
pos.append([round(pos[0][0]+length[0]+length[2]-length[13],4),round(pos[0][1]+height[2],4)])#right bottom fillet



"""Calculations"""
# --------------------------------------------------------------------------------
dimen=[]
for i in range(len(pos)):
    dimen.append([length[i],height[i]])



area=calc_area(obj,dimen)
moi=calc_moi(obj,dimen)
centroid=calc_centroid(obj,dimen,pos)
axis=composite_centroid(area,centroid)
ah2=calc_Ah2(area,centroid,axis)
i_sum=i_composite(moi,ah2)


df=pd.DataFrame([name,length,height,pos,area,centroid,moi,ah2,i_sum,obj],
                index=['Name','Length','Height','Position','Area','Centroid','I','Ah2','I+Ah2','Object Type']).T
df.set_index('Name',inplace=True)
df2=pd.DataFrame([axis],index=['Centroidal Axis'])

# # print(axis)

#
df.to_excel('outputs/section.xlsx')
df2.to_excel('outputs/bridge_axis.xlsx')


################################################################################################


"""For Pier Section"""



import pandas as pd
from calcs import calc_area,calc_moi,calc_centroid,composite_centroid,calc_Ah2,i_composite
import openpyxl


length=[0.6,0.6,2.4,2.4,1.8,1.8,0.6,0.6,1.8,1.8,0.45,0.45,0.45,0.45]
height=[3.2,3.2,0.5,0.3,0.15,0.15,0.3,0.3,0.3,0.3,0.15,0.15,0.15,0.15]


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
pos=[[3.5,3.5]]
pos.append([pos[0][0]+length[0]+length[2],pos[0][1]])
pos.append([pos[0][0]+length[0],pos[0][1]])
pos.append([pos[0][0]+length[0],pos[0][1]+height[0]-height[3]])
pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0]-height[4],4)])
pos.append([round(pos[0][0]+length[0]+length[3]+length[1],4),round(pos[0][1]+height[0]-height[5],4)])
pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0],4)])
pos.append([round(pos[0][0]+length[0]+length[3]+length[1]+length[5]-length[7],4),round(pos[0][1]+height[0],4)])
pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0]-height[4]-height[8],4)])
pos.append([round(pos[0][0]+length[0]+length[3]+length[1],4),round(pos[0][1]+height[0]-height[5]-height[9],4)])
pos.append([round(pos[0][0]+length[0],4),round(pos[0][1]+height[0]-height[3]-height[10],4)])
pos.append([round(pos[0][0]+length[0]+length[3]-length[11],4),round(pos[0][1]+height[0]-height[3]-height[10],4)])
pos.append([round(pos[0][0]+length[0],4),round(pos[0][1]+height[2],4)])
pos.append([round(pos[0][0]+length[0]+length[2]-length[13],4),round(pos[0][1]+height[2],4)])


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


df=pd.DataFrame([name,length,height,pos,area,centroid,moi,ah2,i_sum,obj],index=['Name','Length','Height','Position','Area','Centroid','I','Ah2','I+Ah2','Object Type']).T
df.set_index('Name',inplace=True)
df2=pd.DataFrame([axis],index=['Centroidal Axis'])

# # print(axis)

#
df.to_excel('outputs/section.xlsx')
df2.to_excel('outputs/bridge_axis.xlsx')
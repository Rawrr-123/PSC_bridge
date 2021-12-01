import pandas as pd
from calcs import calc_area,calc_moi,calc_centroid,composite_centroid,calc_Ah2,i_composite
from bridge_specs import box
import tkinter as tk


################################################################################
root = tk.Tk()

canvas1 = tk.Canvas(root, width=1000, height=1000)
canvas1.pack()

img=tk.PhotoImage(file="Images/Bridge Section.png")
canvas1.create_image(300,300,image=img)

l1 = tk.Label(root, text='Bridge height')
canvas1.create_window(100, 100, window=l1)
e1 = tk.Entry(root)
canvas1.create_window(200, 100, window=e1)
e2 = tk.Entry(root)
canvas1.create_window(200, 140, window=e2)

def entry():
    print(e1.get())
    print(e2.get())

button1 = tk.Button(text='Input', command=entry)
canvas1.create_window(200, 180, window=button1)

root.mainloop()






##################################################################################

import openpyxl

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



pillar_len=box['pillar_len']
pillar_hei=box['pillar_hei']
botslab_len=box['botslab_len']
botslab_hei=box['botslab_hei']
topslab_len=box['topslab_len']
topslab_hei=box['topslab_hei']
rec_cant_length=box['rec_cant_length']
rec_cant_height=box['rec_cant_height']
lef_kerb_len=box['lef_kerb_len']
lef_kerb_hei=box['lef_kerb_hei']
rig_kerb_len=box['rig_kerb_len']
rig_kerb_hei=box['rig_kerb_hei']
tri_cant_len=box['tri_cant_len']
tri_cant_hei=box['tri_cant_hei']
chamfer_len=box['chamfer_len']
chamfer_hei=box['chamfer_hei']


length=[pillar_len,pillar_len,botslab_len,topslab_len,rec_cant_length,rec_cant_length,
        lef_kerb_len,rig_kerb_len,tri_cant_len,tri_cant_len,chamfer_len,chamfer_len,chamfer_len,chamfer_len]
height=[pillar_hei,pillar_hei,botslab_hei,topslab_hei,rec_cant_height,rec_cant_height,
        lef_kerb_hei,rig_kerb_hei,tri_cant_hei,tri_cant_hei,chamfer_hei,chamfer_hei,chamfer_hei,chamfer_hei]


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



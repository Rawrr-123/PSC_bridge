from tkinter.constants import FALSE
import pandas as pd
import csv
from calcs import calc_area,calc_moi,calc_centroid,composite_centroid,calc_Ah2,i_composite
from bridge_specs import box
import tkinter as tk
from PIL import Image,ImageTk

################################################################################

length=[]
height=[]

def tkinput():

    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=1000, height=500)
    canvas1.pack()
    root.title("Section Input")

    img=tk.PhotoImage(file="Images/Section.png")


    canvas1.create_image(700,250,image=img)

    l1 = tk.Label(root, text='Width(m)→')
    canvas1.create_window(160, 75, window=l1)
    l2 = tk.Label(root, text='Length(m)↑')
    canvas1.create_window(300, 75, window=l2)



    l3 = tk.Label(root, text='Section 1')
    canvas1.create_window(50, 100, window=l3)
    e1 = tk.Entry(root)
    canvas1.create_window(160, 100, window=e1)
    e2 = tk.Entry(root)
    canvas1.create_window(300, 100, window=e2)

    l4 = tk.Label(root, text='Section 2')
    canvas1.create_window(50, 125, window=l4)
    e3 = tk.Entry(root)
    canvas1.create_window(160, 125, window=e3)
    e4 = tk.Entry(root)
    canvas1.create_window(300, 125, window=e4)


    l5 = tk.Label(root, text='Section 3')
    canvas1.create_window(50, 150, window=l5)
    e5 = tk.Entry(root)
    canvas1.create_window(160, 150, window=e5)
    e6 = tk.Entry(root)
    canvas1.create_window(300, 150, window=e6)


    l6 = tk.Label(root, text='Section 4')
    canvas1.create_window(50, 175, window=l6)
    e7 = tk.Entry(root)
    canvas1.create_window(160, 175, window=e7)
    e8 = tk.Entry(root)
    canvas1.create_window(300, 175, window=e8)


    l7 = tk.Label(root, text='Section 5')
    canvas1.create_window(50, 200, window=l7)
    e9 = tk.Entry(root)
    canvas1.create_window(160, 200, window=e9)
    e10 = tk.Entry(root)
    canvas1.create_window(300, 200, window=e10)

    l8 = tk.Label(root, text='Section 6')
    canvas1.create_window(50, 225, window=l8)
    e11 = tk.Entry(root)
    canvas1.create_window(160, 225, window=e11)
    e12 = tk.Entry(root)
    canvas1.create_window(300, 225, window=e12)

    l9 = tk.Label(root, text='Section 7')
    canvas1.create_window(50, 250, window=l9)
    e13 = tk.Entry(root)
    canvas1.create_window(160, 250, window=e13)
    e14 = tk.Entry(root)
    canvas1.create_window(300, 250, window=e14)


    l10 = tk.Label(root, text='Section 8')
    canvas1.create_window(50, 275, window=l10)
    e15 = tk.Entry(root)
    canvas1.create_window(160, 275, window=e15)
    e16 = tk.Entry(root)
    canvas1.create_window(300, 275, window=e16)


    l11 = tk.Label(root, text='Section 9')
    canvas1.create_window(50, 300, window=l11)
    e17 = tk.Entry(root)
    canvas1.create_window(160, 300, window=e17)
    e18 = tk.Entry(root)
    canvas1.create_window(300, 300, window=e18)

    l12 = tk.Label(root, text='Section 10')
    canvas1.create_window(50, 325, window=l12)
    e19 = tk.Entry(root)
    canvas1.create_window(160, 325, window=e19)
    e20 = tk.Entry(root)
    canvas1.create_window(300, 325, window=e20)


    l13 = tk.Label(root, text='Section 11')
    canvas1.create_window(50, 350, window=l13)
    e21 = tk.Entry(root)
    canvas1.create_window(160, 350, window=e21)
    e22 = tk.Entry(root)
    canvas1.create_window(300, 350, window=e22)


    l14 = tk.Label(root, text='Section 12')
    canvas1.create_window(50, 375, window=l14)
    e23 = tk.Entry(root)
    canvas1.create_window(160, 375, window=e23)
    e24 = tk.Entry(root)
    canvas1.create_window(300, 375, window=e24)


    l15 = tk.Label(root, text='Section 13')
    canvas1.create_window(50, 400, window=l15)
    e25 = tk.Entry(root)
    canvas1.create_window(160, 400, window=e25)
    e26 = tk.Entry(root)
    canvas1.create_window(300, 400, window=e26)


    l16 = tk.Label(root, text='Section 14')
    canvas1.create_window(50, 425, window=l16)
    e27 = tk.Entry(root)
    canvas1.create_window(160, 425, window=e27)
    e28 = tk.Entry(root)
    canvas1.create_window(300, 425, window=e28)


    def entry():
        w1=float(e1.get())
        l1=float(e2.get())
        w2=float(e3.get())
        l2=float(e4.get())
        w3=float(e5.get())
        l3=float(e6.get())
        w4=float(e7.get())
        l4=float(e8.get())
        w5=float(e9.get())
        l5=float(e10.get())
        w6=float(e11.get())
        l6=float(e12.get())
        w7=float(e13.get())
        l7=float(e14.get())
        w8=float(e15.get())
        l8=float(e16.get())
        w9=float(e17.get())
        l9=float(e18.get())
        w10=float(e19.get())
        l10=float(e20.get())
        w11=float(e21.get())
        l11=float(e22.get())
        w12=float(e23.get())
        l12=float(e24.get())
        w13=float(e25.get())
        l13=float(e26.get())
        w14=float(e27.get())
        l14=float(e28.get())
        length.extend([w1,w2,w3,w4,w10,w13,w11,w14,w9,w12,w5,w6,w7,w8])
        height.extend([l1,l2,l3,l4,l10,l13,l11,l14,l9,l12,l5,l6,l7,l8])
        root.quit()
    button1 = tk.Button(text='Input', command=entry)
    canvas1.create_window(225, 475, window=button1)

    root.mainloop()
    df=pd.DataFrame(length,height).T
    df.to_excel('Saved Inputs/box.xlsx',encoding='utf-8',index_label='Columns',index=False)
    
##############################################################################



if False:
    tkinput()
else:
    df=pd.read_excel('Saved Inputs/box.xlsx',index_col=None,header=None)
    height=df.values.tolist()[0]
    length=df.values.tolist()[1]




print(length,height)
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



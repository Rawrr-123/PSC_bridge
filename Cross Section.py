import pandas as pd
import csv
from reaction import bm_udl
from irc6_2007 import ped_ll

# import tkinter as tk
# from PIL import Image,ImageTk
# from allinput import allinput

######################################################################################3

"""INPUTS SECTION"""

"""FOR CROSS SECTION"""
length=[]
height=[]


if False:
    allinput()

df=pd.read_excel('Saved Inputs/box.xlsx',index_col=None,header=None)


height=df.values.tolist()[0]
length=df.values.tolist()[1]


"""FOR DEAD LOAD MOMENTS"""


df_bridge=pd.read_excel('outputs/section.xlsx').set_index('Name')


span=50
cw=6
l_kerblen=0.6
r_kerblen=0.6
area_sum=round(sum(pd.to_numeric(df_bridge.loc[:,'Area'])),5)
sc=[(j)/8*50 for j in range(9)]
loads=["PDL","ODL","SIDL","PEDL"]

####################################################################################3###############
"""Dimensions=[length,height] for rectangle/triangle and radius for circle"""
"""Objects= Rectangle,circle,triangle"""
"""Pos=[x,y]"""


def calc_area(object,dimensions):
    if object=='rectangle':
        return round(dimensions[0]*dimensions[1],6)
    elif object =='circle':
        return round(dimensions**2*3.14159266,6)
    else:
        return round(dimensions[0],4)*round(dimensions[1]/2,6)


def calc_moi(object,dimensions):
    if object=='rectangle':
        return [round(dimensions[0]*dimensions[1]**3/12,4),round(dimensions[0]**3*dimensions[1]/12,4)]
    elif object=='circle':
        return round(dimensions**4*3.14159266/4,4)
    else:
        return [round(dimensions[0]*dimensions[1]**3/36,4),round(dimensions[0]**3*dimensions[1]/36,4)]



def calc_centroid(object, dimensions,pos):
    if object == 'rectangle':
        return [round(round(pos[0]+dimensions[0]/2,4),5),round(round(pos[1]+dimensions[1]/2,4),5)]



    elif object == 'circle':
        return [round(pos[0]+0,5),round(pos[1]+0,5)]


    elif object=='triangle_1':
        return [round(pos[0]+(dimensions[0]*2/3),5),round(pos[1]+(dimensions[1]*2/3),5)]




    elif object == 'triangle_2' :
        return [round(pos[0] + (dimensions[0] * 1 / 3),5),round( pos[1] + (dimensions[1] * 1 / 3),5)]


    elif object == 'triangle_3':
        return [round(pos[0] + (dimensions[0] * 1 / 3),5), round(pos[1] + (dimensions[1] * 2 / 3),5)]


    elif object == 'triangle_4':
        return [round(pos[0] + (dimensions[0] * 2 / 3),5),round( pos[1] + (dimensions[1] * 1 / 3),5)]

    
def composite_centroid(area,centroid):
    ax=0
    ay=0
    asum=0
    for i in range(len(area)):
        ax+=round(area[i]*centroid[i][0],8)
        ay += round(area[i] * centroid[i][1],8)
        asum+=round(area[i],5)
    return [round(ax/asum,6),round(ay/asum,6)]


def calc_Ah2(area,centroid,composite_axis):
    return [round(area*(centroid[1]-composite_axis[1])**2,6),round(area*(centroid[0]-composite_axis[0])**2,6)]
    

# def i_composite(moi,ah2):
#     i_sum=[]
#     for i in range(len(moi)):
#         i_sum.append([moi[i][0]+ah2[i][0],moi[i][1]+ah2[i][1]])
#     return i_sum

def i_composite(moi,ah2):
    i_sum=[0,0]
    for i in range(len(moi)):
        i_sum[0]+=moi[i][0]+ah2[i][0]
        i_sum[1]+=moi[i][1]+ah2[i][1]
    return i_sum


def stiffness(fck,I,l):
    fcm = fck + 10
    E = 22 * (fcm / 12.5) ** 0.3
    return 3*E*I/l**3



class Cross_section:
    def __init__(self,length,height):
        self.length=length
        self.height=height

    @property
    def name(self):
        return['left Pillar','right pillar','bottom slab','top slab','left cantilever','right cantilever',
      'left triangle','right triangle','left top fillet','right top fillet','left bottom fillet','right bottom fillet']
        
    
    @property
    def obj(self):    
        return['rectangle','rectangle','rectangle','rectangle','rectangle','rectangle','triangle_1',
     'triangle_3','triangle_3','triangle_1','triangle_2','triangle_4']

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
        
    
    @property
    def position(self):
        pos=[[3.5,3.5]]#left pillar
        pos.append([pos[0][0]+self.length[0]+self.length[2],pos[0][1]])#right pillar
        pos.append([pos[0][0]+self.length[0],pos[0][1]])#bottom slab
        pos.append([pos[0][0]+self.length[0],pos[0][1]+self.height[0]-self.height[3]])#top slab
        pos.append([round(pos[0][0]-self.length[4],4),round(pos[0][1]+self.height[0]-self.height[4],4)])#left cantilever
        pos.append([round(pos[0][0]+self.length[0]+self.length[3]+self.length[1],4),round(pos[0][1]+self.height[0]-self.height[5],4)])#right cantilever
        # pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0],4)])#left kerb
        # pos.append([round(pos[0][0]+length[0]+length[3]+length[1]+length[5]-length[7],4),round(pos[0][1]+height[0],4)])#right kerb
        pos.append([round(pos[0][0]-self.length[4],4),round(pos[0][1]+self.height[0]-self.height[4]-self.height[8],4)])#left triangle
        pos.append([round(pos[0][0]+self.length[0]+self.length[3]+self.length[1],4),round(pos[0][1]+self.height[0]-self.height[5]-self.height[9],4)])#right triangle
        pos.append([round(pos[0][0]+self.length[0],4),round(pos[0][1]+self.height[0]-self.height[3]-self.height[9],4)])#left top fillet
        pos.append([round(pos[0][0]+self.length[0]+self.length[3]-self.length[10],4),round(pos[0][1]+self.height[0]-self.height[3]-self.height[9],4)])#right top fillet
        pos.append([round(pos[0][0]+self.length[0],4),round(pos[0][1]+self.height[2],4)])#left bottom fillet
        pos.append([round(pos[0][0]+self.length[0]+self.length[2]-self.length[11],4),round(pos[0][1]+self.height[2],4)])#right bottom fillet
        return pos
    
    @property
    def dimensions(self):
        dimen=[]
        for i in range(len(self.position)):
            dimen.append([self.length[i],self.height[i]])
        return dimen

        
    @property
    def section_area(self):
        area=[]
        for i in range(len(self.name)):
            area.append(calc_area(self.obj[i],self.dimensions[i]))
        return area

    @property
    def section_centroid(self):
        centroid=[]
        for i in range(len(self.obj)):
            centroid.append(calc_centroid(self.obj[i],self.dimensions[i],self.position[i]))
        return centroid


    @property
    def section_moi(self):
        moi=[]
        for i in range(len(self.obj)):
            moi.append(calc_moi(self.obj[i],self.dimensions[i]))
        return moi
        

    @property
    def Centroid(self):
        return composite_centroid(self.section_area,self.section_centroid)
    
    @property
    def AH2(self):
        ah2=[]
        for i in range(len(self.obj)):
            ah2.append(calc_Ah2(self.section_area[i],self.section_centroid[i],self.Centroid))
        return ah2
    
    @property
    def I(self):
        return i_composite(self.section_moi,self.AH2)\
    
    @property
    def ymax(self):
        ymax=0
        hold=0
        for i in range(len(self.name)):
            hold=abs(self.position[i][1]-self.Centroid[1])
            if ymax<hold:
                ymax=hold
        return round(ymax,5)

    @property
    def ymin(self):
        hold=0
        ymin=abs(self.position[0][1]-self.Centroid[1])
        for i in range(len(self.name)):
            hold=abs(self.position[i][1]-self.Centroid[1])
            if ymin>hold:
                ymin=hold 
        return round(ymin,5)
    



def excel_export(section):

    df=pd.DataFrame([section.name,section.length,section.height,section.position,section.section_area,section.section_centroid,section.section_moi,section.AH2,section.obj],
                    index=['Name','Length','Height','Position','Area','Centroid','I','Ah2','Object Type']).T
    df.set_index('Name',inplace=True)
    df2=pd.DataFrame([section.Centroid],index=['Centroidal Axis'])
    df.to_excel('outputs/section.xlsx')
    df2.to_excel('outputs/bridge_axis.xlsx')



class Dead_Load:
    def __init__(self,name,asum,sc,span,walkway_width,walkway_thickness,wearing_course,cw,railing_udl,I,ymax,ymin):
        self.areasum=asum
        self.name=name
        self.sections=sc
        self.span=span
        self.www=walkway_width
        self.wwt=walkway_thickness
        self.wc=wearing_course
        self.cw=cw
        self.rudl=railing_udl
        self.I=I
        self.ymax=ymax
        self.ymin=ymin

    
    @property
    def load(self):
        if self.name=="PDL":
            return self.areasum*25
        elif self.name=="ODL":
            return self.www*self.wwt*25+2*self.rudl
        elif self.name=="SIDL":
            return self.wc*self.cw*22
        elif self.name=="PEDL":
            return ped_ll(self.span,self.www)
        



    @property
    def BM(self):
        bm=[]
        for i in range(len(self.sections)):
            bm.append(bm_udl(span,self.sections[i],self.load))
        return bm
    
    @property
    def stress(self):
        smax=[]
        smin=[]
        for i in range(len(self.BM)):
            smax.append(self.BM[i]*self.ymax/self.I)
            smin.append(self.BM[i]*self.ymin/self.I)
        return [smax,smin]


def excel_loads(PDL,ODL,PEDL,SIDL,sc):
        
    df3 = pd.DataFrame({'Section at': sc, 'Dead Load': PDL.BM, 'Other Loads': ODL.BM, 'Surface Loads': SIDL.BM,
                        'Pedestrian Load': PEDL.BM

                        })

    df3.to_csv('outputs/Moments.csv')
    
    df5=pd.DataFrame({'Section at': sc, 'S+ PDL': PDL.stress[0], 'S- PDL': PDL.stress[1], 'S+ ODL': ODL.stress[0],'S- ODL': ODL.stress[1],
                     'S+ PEDL': PEDL.stress[0], 'S- PEDL': PEDL.stress[1],'S+ SIDL': SIDL.stress[0], 'S- SIDL': SIDL.stress[1]

                        })

    df5.to_csv('outputs/Stresses.csv')


    a=[PDL.load*span/2,PDL.load*span/2,PDL.load*span]
    b=[ODL.load*span/2,ODL.load*span/2,ODL.load*span]
    c=[SIDL.load*span/2,SIDL.load*span/2,SIDL.load*span]
    d=[PEDL.load*span/2,PEDL.load*span/2,PEDL.load*span]
    df4=pd.DataFrame([a,b,c,d],columns=['RL','RR','Sum'],index=['Dead Load','Other Load','Surface Load','Pedestrian load']
    )
    df4.to_csv('outputs/DL_for_Seismic.csv')




#############################################################################################33



section=Cross_section(length,height)
PDL=Dead_Load('PDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
ODL=Dead_Load('ODL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
PEDL=Dead_Load('PEDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
SIDL=Dead_Load('SIDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)

excel_loads(PDL,ODL,PEDL,SIDL,sc)
# print(dls.stress)


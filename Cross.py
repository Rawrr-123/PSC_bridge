import pandas as pd
import csv
from reaction import bm_udl
from irc6_2007 import ped_ll
import math

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
        ax+=round(area[i]*centroid[i][0],6)
        ay+=round(area[i]*centroid[i][1],6)
        asum+=area[i]
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
    def __init__(self,length,height,span,section_at):
        self.length=length
        self.height=height
        self.span=span
        self.section_at=section_at
        if self.expansion_width>0:
            if self.expansion_width>=self.height[10] and self.expansion_width>=self.height[11]:
                h1=self.height[10]
                h2=self.height[11]
            else:
                h1=h2=0
            self.length=self.length+[self.length[10],round(self.length[2]*0.45-self.length[10]*2,5),round(self.length[2]*0.45-self.length[10],5),self.length[10],self.length[11],round(self.length[2]*0.45-self.length[11],5),round(self.length[2]*0.45-self.length[11]*2,5),self.length[11]]
            self.height=self.height+[h1,h1,self.expansion_width-h1,self.expansion_width-h1,self.expansion_width-h2,self.expansion_width-h2,h2,h2]
    
    @property
    def expansion_width(self):
        return 0.5

    @property
    def name(self):
        nyam=['left Pillar','right pillar','bottom slab','top slab','left cantilever','right cantilever',
      'left triangle','right triangle','left top fillet','right top fillet','left bottom fillet','right bottom fillet']
        if self.expansion_width>0:
            nyam=nyam+['Expanded_triangle_left','Top_Expanded_rectangle_left','Side_Expanded_rectangle_left','Fillet_triangle_left','Fillet_triangle_right','Side_Expanded_rectangle_right',
            'Top_Expanded_rectangle_right','Expanded_triangle_right']
        return nyam
    
    @property
    def obj(self):    
        obui=['rectangle','rectangle','rectangle','rectangle','rectangle','rectangle','triangle_1',
     'triangle_3','triangle_3','triangle_1','triangle_2','triangle_4']
        if self.expansion_width>0:
            obui=obui+['triangle_1','rectangle','rectangle','triangle_2','triangle_4','rectangle','rectangle','triangle_3']
        return obui

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
        pos=[[3.5,3.5]]#left pillar  0
        pos.append([pos[0][0]+self.length[0]+self.length[2],pos[0][1]])#right pillar  1
        pos.append([pos[0][0]+self.length[0],pos[0][1]])#bottom slab  2
        pos.append([pos[0][0]+self.length[0],pos[0][1]+self.height[0]-self.height[3]])#top slab  3
        pos.append([round(pos[0][0]-self.length[4],4),round(pos[0][1]+self.height[0]-self.height[4],4)])#left cantilever  4
        pos.append([round(pos[0][0]+self.length[0]+self.length[3]+self.length[1],4),round(pos[0][1]+self.height[0]-self.height[5],4)])#right cantilever  5
        # pos.append([round(pos[0][0]-length[4],4),round(pos[0][1]+height[0],4)])#left kerb  
        # pos.append([round(pos[0][0]+length[0]+length[3]+length[1]+length[5]-length[7],4),round(pos[0][1]+height[0],4)])#right kerb
        pos.append([round(pos[0][0]-self.length[4],4),round(pos[0][1]+self.height[0]-self.height[4]-self.height[6],4)])#left triangle  6
        pos.append([round(pos[0][0]+self.length[0]+self.length[3]+self.length[1],4),round(pos[0][1]+self.height[0]-self.height[5]-self.height[7],4)])#right triangle  7
        pos.append([round(pos[0][0]+self.length[0],4),round(pos[0][1]+self.height[0]-self.height[3]-self.height[9],4)])#left top fillet  8
        pos.append([round(pos[0][0]+self.length[0]+self.length[3]-self.length[10],4),round(pos[0][1]+self.height[0]-self.height[3]-self.height[9],4)])#right top fillet  9
        pos.append([round(pos[0][0]+self.length[0],4),round(pos[0][1]+self.height[2],4)])#left bottom fillet  10
        pos.append([round(pos[0][0]+self.length[0]+self.length[2]-self.length[11],4),round(pos[0][1]+self.height[2],4)])#right bottom fillet  11
        if self.expansion_width>0:
            pos=pos+[[pos[10][0],pos[10][1]]]
            pos = pos+ [[pos[10][0]+self.length[10],pos[10][1]]]
            pos= pos + [[pos[10][0],pos[10][1]+self.height[10]]]
            pos = pos +[[round(pos[10][0]+self.length[2]*0.45-self.length[10],4),pos[10][1]]]

            
            pos = pos+ [[pos[11][0]-self.length[2]*0.45-self.length[11],pos[11][1]]]
            pos = pos+[[pos[11][0]+self.length[11]-self.length[2]*0.45,pos[11][1]+self.height[11]]]
            pos = pos+ [[pos[11][0]-self.length[2]*0.45+self.length[11],pos[11][1]]]
            pos=pos+[[pos[11][0],pos[11][1]]]

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

    def cable_pos(self,f,nos):

        fck=35
        if fck<45:
            mina=0.280+(45-fck)*4/1000
            minb=0.200+(45-fck)*4/1000

        else:
            mina=0.280
            minb=0.220

        expanlen=min(section.length[13],section.length[16])
        b=section.height[2]/2
        if b<minb:
            raise ValueError ("Very bad input section")
        a=0.450
        if a<mina:
            raise ValueError ("Very bad input section")
        e=section.length[0]/2
        if e<=b:
            raise ValueError ("Very bad input section")

        cc=round(section.position[1][0]+section.length[1]-section.position[0][0]-section.length[0],3)

        n=14

        ntop=round(n/4)/2
        nbot=n-ntop*2


    
        nbotup=0

        adash=cc/(nbot+1)
        while adash<a:

            if (nbotup/2)<=math.floor((expanlen-2*e)/a):
                nbot=nbot-2
                nbotup=nbotup+2
                adash=cc/(nbot+1)
            else:
                ntop=ntop+1
                nbot=nbot-2
                adash=cc/(nbot+1)

        nbotup=nbotup/2
        amid=0.15
        expanlen

        ####################################################

        toppos=[]
        midtop=[]
        bottompos=[]
        midbot=[]
        bottomposupleft=[]
        bottomposupright=[]
        midbotupleft=[]
        midbotupright=[]
        ntop=int(ntop)
        nbot=int(nbot)
        nbotup=int(nbotup)
        for i in range(ntop):
            if i==0:
                toppos.append([round(x+y,4) for x,y in zip(section.position[0],[e,b+3*a])])
                midtop.append([round(x+y,4) for x,y in zip(section.position[0],[e,b+3*amid])])
                
            if i>0:
                toppos.append([round(x+y,4) for x,y in zip(toppos[i-1],[0,a])])
                midtop.append([round(x+y,4) for x,y in zip(midtop[i-1],[0,amid])])

        for i in range(len(toppos)):
            toppos.append([x+y for x,y in zip(toppos[i],[cc,0])])
            midtop.append([x+y for x,y in zip(midtop[i],[cc,0])])

            
        for i in range(nbot):
            if i==0:
                bottompos.append([round(x+y,4) for x,y in zip(section.position[0],[e+adash,b])])
                midbot.append([round(x+y,4) for x,y in zip(section.position[0],[e+adash,b])])
            if i>0:
                bottompos.append([round(x+y,4) for x,y in zip(bottompos[i-1],[adash,0])])
                midbot.append([round(x+y,4) for x,y in zip(midbot[i-1],[adash,0])])
        for i in range(nbotup):
            if i==0:
                bottomposupleft.append([round(x+y,4) for x,y in zip(section.position[0],[e+adash,b+a])])
                bottomposupright.append([round(x+y,4) for x,y in zip(section.position[1],[-e-adash,b+a])])
                midbotupleft.append([round(x+y,4) for x,y in zip(section.position[0],[e+adash,b+a])])
                midbotupright.append([round(x+y,4) for x,y in zip(section.position[0],[-e-adash,b+a])])
            if i>0:
                bottomposupleft.append([round(x+y,4) for x,y in zip(bottomposupleft[i-1],[a,0])])
                bottomposupright.append([round(x+y,4) for x,y in zip(bottomposupright[i-1],[-a,0])])
                midbotupleft.append([round(x+y,4) for x,y in zip(midbotupleft[i-1],[a,0])])
                midbotupright.append([round(x+y,4) for x,y in zip(midbotupright[i-1],[-a,0])])
        endcablepos=[*toppos,*bottompos,*bottomposupleft,*bottomposupright]

        midcablepos=[*midtop,*midbot,*midbotupleft,*midbotupright]

        x=self.section_at
        l=self.span
        cablepos=[]


        for i in range(len(endcablepos)):
            
            h=midcablepos[i][1]-endcablepos[i][1]
            pos= -((4*h*x**2)/(l**2))+4*h*x/l+endcablepos[i][1]
            cablepos.append([endcablepos[i][0],pos])
        
        return cablepos

 


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



def excel_export(section):

    df=pd.DataFrame([section.name,section.length,section.height,section.position,section.section_area,section.section_centroid,section.section_moi,section.AH2,section.obj],
                    index=['Name','Length','Height','Position','Area','Centroid','I','Ah2','Object Type']).T
    df.set_index('Name',inplace=True)
    df2=pd.DataFrame([section.Centroid],index=['Centroidal Axis'])
    df.to_excel('outputs/section.xlsx')
    df2.to_excel('outputs/bridge_axis.xlsx')



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



section=Cross_section(length,height,50,25)

PDL=Dead_Load('PDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
ODL=Dead_Load('ODL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
PEDL=Dead_Load('PEDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
SIDL=Dead_Load('SIDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,section.I[0],section.ymax,section.ymin)
# excel_export(section)
# excel_loads(PDL,ODL,PEDL,SIDL,sc)
# print(section.Centroid)

print(section.cable_pos(35,14))
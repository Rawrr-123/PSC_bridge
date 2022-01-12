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


#####################################################################################################################

"""GUI INPUT OF BRIDGE SECTION LENGTHS AND HEIGHTS"""

if False:
    allinput()

df=pd.read_excel('Saved Inputs/box.xlsx',index_col=None,header=None)


height=df.values.tolist()[0]
length=df.values.tolist()[1]



###############################################################################################
"""FOR DEAD LOAD MOMENTS INPUTS"""


df_bridge=pd.read_excel('outputs/section.xlsx').set_index('Name')

span=50
cw=6
l_kerblen=0.6
r_kerblen=0.6
area_sum=round(sum(pd.to_numeric(df_bridge.loc[:,'Area'])),5)

""""distance form left of 9 divisions of section"""
sc=[(j)/8*50 for j in range(9)] 

loads=["PDL","ODL","SIDL","PEDL"]

####################################################################################3###############
"""Dimensions=[length,height] for rectangle/triangle and radius for circle"""
"""Objects= Rectangle,circle,triangle"""
"""Pos=[x,y]"""

######################################################################################################
"""SHAPE DEFINITIONS FOR TRIANGLES"""
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
        
    

####################################################################################################
"""CALCULATE SECTION AREA FOR SIMPLE SHAPES
OBJECT=OBJECT NAME i.e. "rectangle" "triangle-1" "triangle-2" "circle" etc
DIMENSIONS=[LENGTH,HEIGHT] FOR RECTANGLES AND TRIANGLES AND 
            RADIUS FOR CIRCLES           """

def calc_area(object,dimensions):
    if object=='rectangle':
        return round(dimensions[0]*dimensions[1],6)
    elif object =='circle':
        return round(dimensions**2*3.14159266,6)
    else:
        return round(dimensions[0],4)*round(dimensions[1]/2,6)

###############################################################################################
""" CALCULATE SECTION MOMENT OF INERTIA ABOUT CENTROID FOR SIMPLE SHAPES
      OBJECT=OBJECT NAME i.e. "rectangle" "triangle-1" "triangle-2" "circle" etc
DIMENSIONS=[LENGTH,HEIGHT] FOR RECTANGLES AND TRIANGLES AND 
            RADIUS FOR CIRCLES   """

def calc_moi(object,dimensions):
    if object=='rectangle':
        return [round(dimensions[0]*dimensions[1]**3/12,4),round(dimensions[0]**3*dimensions[1]/12,4)]
    elif object=='circle':
        return round(dimensions**4*3.14159266/4,4)
    else:
        return [round(dimensions[0]*dimensions[1]**3/36,4),round(dimensions[0]**3*dimensions[1]/36,4)]

###############################################################################################

""" CALCULATE POSITION OF CENTROID OF SIMPLE SHAPES ABOUT ORIGIN
      OBJECT=OBJECT NAME i.e. "rectangle" "triangle-1" "triangle-2" "circle" etc
DIMENSIONS=[LENGTH,HEIGHT] FOR RECTANGLES AND TRIANGLES AND 
            RADIUS FOR CIRCLES   
POS=[X-POSITION.Y-POSITION] """

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


##########################################################################################
""" CALCULATE POSITION OF COMPOSITE CENTROID OF MANY SIMPLE SHAPES ABOUT ORIGIN
      AREA= AREA OF INDIVIDUAL SIMPLE SHAPES
CENTROID=CENTROID OF INDIVIDUAL SHAPES ABOUT ORIGIN
"""

    
def composite_centroid(area,centroid):
    ax=0
    ay=0
    asum=0
    for i in range(len(area)):
        ax+=round(area[i]*centroid[i][0],6)
        ay+=round(area[i]*centroid[i][1],6)
        asum+=area[i]
    return [round(ax/asum,6),round(ay/asum,6)]

#############################################################################
""" CALCULATE AH2 FOR INDIVIDUAL SIMPLE SHAPES
      AREA= AREA OF INDIVIDUAL SIMPLE SHAPES
CENTROID=CENTROID OF INDIVIDUAL SHAPES ABOUT ORIGIN
COMPOSITE AXIS=CENTROID OF COMPOSITE SECTION
"""

def calc_Ah2(area,centroid,composite_axis):
    return [round(area*(centroid[1]-composite_axis[1])**2,6),round(area*(centroid[0]-composite_axis[0])**2,6)]
    
################################################################################################

# def i_composite(moi,ah2):
#     i_sum=[]
#     for i in range(len(moi)):
#         i_sum.append([moi[i][0]+ah2[i][0],moi[i][1]+ah2[i][1]])
#     return i_sum

###########################################################################################

""" CALCULATE MOMENT OF INERTIA OF COMPOSITE SECTION
      MOI=MOMENT OF INERTIA OF INDIVIDUAL SIMPLE SHAPES
AH2=AH2 FOR INDIVIDUAL SIMPLE SHAPES
"""

def i_composite(moi,ah2):
    i_sum=[0,0]
    for i in range(len(moi)):
        i_sum[0]+=moi[i][0]+ah2[i][0]
        i_sum[1]+=moi[i][1]+ah2[i][1]
    return i_sum

###################################################################################
"""CALCULATE STIFFNESS
FCK= CONCRETE STRENGTH
I=SECTION MOI
L=SPAN LENGTH
"""

def stiffness(fck,I,l):
    fcm = fck + 10
    E = 22 * (fcm / 12.5) ** 0.3
    return 3*E*I/l**3


"""CALCULATE WIDTH OF EXPANDED SECTION OF BOX"""

def expansion_calc(span,section_at,cable):
    return 0

#################################################################################################

"""BOX GIRDER CROSS SECTION OBJECT 
LENGTH = ARRAY OF LENGTH OF DIFFERENT SECTIONS 
HEIGHT = ARRAY OF LENGTH OF DIFFERENT SECTIONS  
"""

class Cross_section:
    def __init__(self,length,height,expanwidth=0):
        self.len=length
        self.hei=height
        self.exp_width=expanwidth
       
    @property 
    def length(self):
        if self.expansion_width>0:
            return self.len+[self.len[10],round(self.len[2]*0.45-self.len[10]*2,5),round(self.len[2]*0.45-self.len[10],5),self.len[10],self.len[11],round(self.len[2]*0.45-self.len[11],5),round(self.len[2]*0.45-self.len[11]*2,5),self.len[11]]
        else:
            return self.len

    @property 
    def height(self):
        if self.expansion_width>0:
            if self.expansion_width>=self.hei[10] and self.expansion_width>=self.hei[11]:
                h1=self.hei[10]
                h2=self.hei[11]
            else:
                h1=h2=0 
            return self.hei+[h1,h1,self.expansion_width-h1,self.expansion_width-h1,self.expansion_width-h2,self.expansion_width-h2,h2,h2]
        else:
            return self.hei

    """WIDTH OF EXPANSION IN END SIDES """
    @property
    def expansion_width(self):
        return self.exp_width

    @expansion_width.setter
    def expansion_width(self,width):
        self.exp_width=width


    """NAME OF PARTS OF SECTIONS"""
    @property
    def name(self):
        nyam=['left Pillar','right pillar','bottom slab','top slab','left cantilever','right cantilever',
      'left triangle','right triangle','left top fillet','right top fillet','left bottom fillet','right bottom fillet']
        if self.expansion_width>0:
            nyam=nyam+['Expanded_triangle_left','Top_Expanded_rectangle_left','Side_Expanded_rectangle_left','Fillet_triangle_left','Fillet_triangle_right','Side_Expanded_rectangle_right',
            'Top_Expanded_rectangle_right','Expanded_triangle_right']
        return nyam
    

    """OBJECT TYPE CORRESPONDING TO DIFFERENT PARTS OF THE SECTION"""   
    @property
    def obj(self):    
        obui=['rectangle','rectangle','rectangle','rectangle','rectangle','rectangle','triangle_1',
     'triangle_3','triangle_3','triangle_1','triangle_2','triangle_4']
        if self.expansion_width>0:
            obui=obui+['triangle_1','rectangle','rectangle','triangle_2','triangle_4','rectangle','rectangle','triangle_3']
        return obui


    """POSITION OF DIFFERENT PARTS OF THE SECTION WRT ORIGIN WITH LEFT BOTTOM CORNER OF LEFT PILLAR SECTION AT [0,0]"""   
    @property
    def position(self):
        pos=[[0,0]]#left pillar  0
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
    

    """ARRAY OF DIMENSIONS OF EACH SECTION IE [LENGTH,HEIGHT]"""
    @property
    def dimensions(self):
        dimen=[]
        for i in range(len(self.position)):
            dimen.append([self.length[i],self.height[i]])
        return dimen


    """AREA OF EACH INDIVIDUAL SECTIONS """    
    @property
    def section_area(self):
        area=[]
        for i in range(len(self.name)):
            area.append(calc_area(self.obj[i],self.dimensions[i]))
        return area


    """CENTROID OF EACH INDIVIDUAL SECTIONS"""
    @property
    def section_centroid(self):
        centroid=[]
        for i in range(len(self.obj)):
            centroid.append(calc_centroid(self.obj[i],self.dimensions[i],self.position[i]))
        return centroid

    
    """"MOI OF EACH INDIVIDUAL SECTIONS """
    @property
    def section_moi(self):
        moi=[]
        for i in range(len(self.obj)):
            moi.append(calc_moi(self.obj[i],self.dimensions[i]))
        return moi

    """COMPOSITE CENTROID OF WHOLE BOX GIRDER """
    @property
    def Centroid(self):
        return composite_centroid(self.section_area,self.section_centroid)
    

    """AH2 OF EACH INDIVIDUAL SECTIONS FROM THEIR OWN CENTROID TO CENTROID OF COMPOSITE BRIDGE SECTION"""
    @property
    def AH2(self):
        ah2=[]
        for i in range(len(self.obj)):
            ah2.append(calc_Ah2(self.section_area[i],self.section_centroid[i],self.Centroid))
        return ah2
    

    """COMPOSITE MOI OF BOX CROSS SECTION"""
    @property
    def I(self):
        return i_composite(self.section_moi,self.AH2)\
    

    """MAX AND MIN Y VALUES FROM CENTROID OF BOX GIRDER"""
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


################################################################################################
"""CABLE PROPERTIES CLASS 
F= Fck OF CONCRETE
NOS=NO OF CABLES 
SECTION = CROSS SECTION OBJECT """
class cables:
    def __init__(self,f,nos,section):
        self.fck=f
        self.n=nos
        self.section=section
        self.cc=round(section.position[1][0]+section.length[1]-section.position[0][0]-section.length[0],3)
    
    @property 
    def expanlen(self):
        try:
            expanlen=min(section.length[14],section.length[17])+section.length[0]
        except:
            expanlen=section.length[0]
        return expanlen

    @property 
    def a(self):
        if self.fck<45:
            mina=0.280+(45-self.fck)*4/1000
        else:
            mina=0.280
        a=0.450
        if a<mina:
            raise ValueError ("Very bad input section")
        return a
    
    @property 
    def b(self):
        if self.fck<45:
            minb=0.200+(45-self.fck)*4/1000
        else:
            minb=0.220
        b=self.section.height[2]/2
        if b<minb:
            raise ValueError ("Very bad input section")
        return b

    @property
    def e(self):
        e=section.length[0]/2
        if e<=self.b:
            raise ValueError ("Very bad input section")
        return e

    @property 
    def cable_arrangement(self):
        self.ntop=round(self.n/4)/2
        self.nbot=self.n-self.ntop*2
        self.nbotup=0
        self.adash=self.cc/(self.nbot-1)
        while self.adash<self.a:

            if (self.nbotup/2)<=math.floor((self.expanlen-2*self.e)/self.a):
                print((self.expanlen-2*self.e)/self.a)
                self.nbot=self.nbot-2
                self.nbotup=self.nbotup+2
                self.adash=self.cc/(self.nbot+1)
            else:
                self.ntop=self.ntop+1
                self.nbot=self.nbot-2
                self.adash=self.cc/(self.nbot+1)

        self.nbotup=self.nbotup/2
        self.amid=0.15
        return self.ntop,self.nbot,self.nbotup
        
    @property
    def endcablepos(self):
        toppos=[]
        bottompos=[]
        bottomposupleft=[]
        bottomposupright=[]
        ntop=int(self.ntop)
        nbot=int(self.nbot)
        nbotup=int(self.nbotup)

        for i in range(ntop):
            if i==0:
                toppos.append([round(x+y,4) for x,y in zip(self.section.position[0],[self.e,self.b+3*self.a])])
                                
            if i>0:
                toppos.append([round(x+y,4) for x,y in zip(toppos[i-1],[0,self.a])])
                
        for i in range(len(toppos)):
            toppos.append([x+y for x,y in zip(toppos[i],[self.cc,0])])
            
            
        for i in range(nbot):
            if i==0:
                bottompos.append([round(x+y,4) for x,y in zip(self.section.position[0],[self.e,self.b])])
            if i>0:
                bottompos.append([round(x+y,4) for x,y in zip(bottompos[i-1],[self.adash,0])])
        for i in range(nbotup):
            if i==0:
                bottomposupleft.append([round(x+y,4) for x,y in zip(self.section.position[0],[self.e,self.b+self.a])])
                bottomposupright.append([round(x+y,4) for x,y in zip(self.section.position[1],[-self.e,self.b+self.a])])
                
            if i>0:
                bottomposupleft.append([round(x+y,4) for x,y in zip(bottomposupleft[i-1],[self.a,0])])
                bottomposupright.append([round(x+y,4) for x,y in zip(bottomposupright[i-1],[-self.a,0])])
                
        endcablepos=[*toppos,*bottompos,*bottomposupleft,*bottomposupright]
        self.bottomposup_end=bottomposupleft+bottomposupright
        return endcablepos
    
    @property
    def midcablepos(self):
        midtop=[]
        midbot=[]
        midbotupleft=[]
        midbotupright=[]
        ntop=int(self.ntop)
        nbot=int(self.nbot)
        nbotup=int(self.nbotup)
        for i in range(ntop):
            if i==0:                
                midtop.append([round(x+y,4) for x,y in zip(section.position[0],[self.e,self.b+3*self.amid])])
                
            if i>0:                
                midtop.append([round(x+y,4) for x,y in zip(midtop[i-1],[0,self.amid])])

        for i in range(len(midtop)):           
            midtop.append([x+y for x,y in zip(midtop[i],[self.cc,0])])

            
        for i in range(nbot):
            if i==0:                
                midbot.append([round(x+y,4) for x,y in zip(section.position[0],[self.e,self.b])])
            if i>0:                
                midbot.append([round(x+y,4) for x,y in zip(midbot[i-1],[self.adash,0])])
        for i in range(nbotup):
            if i==0:                
                midbotupleft.append([round(x+y,4) for x,y in zip(section.position[0],[self.e,self.b+self.a])])
                midbotupright.append([round(x+y,4) for x,y in zip(section.position[0],[-self.e,self.b+self.a])])
            if i>0:                
                midbotupleft.append([round(x+y,4) for x,y in zip(midbotupleft[i-1],[self.a,0])])
                midbotupright.append([round(x+y,4) for x,y in zip(midbotupright[i-1],[-self.a,0])])
        
        self.bottomposup_mid=midbotupleft+midbotupright
        midcablepos=[*midtop,*midbot,*midbotupleft,*midbotupright]
        return midcablepos

    
    def cablepos(self,section_at,span):
        x=section_at
        l=span
        cablepos=[]

        for i in range(len(self.endcablepos)):
            
            h=self.midcablepos[i][1]-self.endcablepos[i][1]
            pos= -((4*h*x**2)/(l**2))+4*h*x/l+self.endcablepos[i][1]
            cablepos.append([self.endcablepos[i][0],pos])
        return cablepos


#############################################################################################################
"""DEAD LOAD CLASS 
        NAME=NAME OF LOAD i.e. PDL,ODL,SIDL OR PEDL
        ASUM=AREA SUM OF CROSS SECTION OF BOX GIRDER
        SC= SECTION DIVISIONS ARRAY EG. [0M,25M,50M]
        CW= CLEARWAY OF ROAD 
        YMAX,YMIN = MAXIMUM,MINIMUM Y FROM CENTROID OF BOX GIRDER """

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
            return 25
        elif self.name=="ODL":
            return self.www*self.wwt*25+2*self.rudl
        elif self.name=="SIDL":
            return self.wc*self.cw*22
        elif self.name=="PEDL":
            return ped_ll(self.span,self.www)
        


    """FIND BENDING MOMENT DUE TO UDLS OF DIFFERENT LOADS"""

    @property
    def BM(self):
        bm=[]
        for i in range(len(self.sections)):
            if self.name=="PDL":
                bm.append(bm_udl(span,self.sections[i],self.load*self.areasum[i]))
            else:
                bm.append(bm_udl(span,self.sections[i],self.load))
        return bm
    



    """FIND STRESSES DUE TO UDLS OF DIFFERENT LOADS"""

    @property
    def stress(self):
        smax=[]
        smin=[]
        for i in range(len(self.BM)):
            smax.append(self.BM[i]*self.ymax[i]/self.I[i][0])
            smin.append(self.BM[i]*self.ymin[i]/self.I[i][0])
        return [smax,smin]

###########################################################################################
"""EXPORT POSITION OF CENTROIDAL AXIS AND SECTION PROPERTIES OF CROSS SECTION TO EXCEL"""

def excel_export(section):

    df=pd.DataFrame([section.name,section.length,section.height,section.position,section.section_area,section.section_centroid,section.section_moi,section.AH2,section.obj],
                    index=['Name','Length','Height','Position','Area','Centroid','I','Ah2','Object Type']).T
    df.set_index('Name',inplace=True)
    df2=pd.DataFrame([section.Centroid],index=['Centroidal Axis'])
    df.to_excel('outputs/section.xlsx')
    df2.to_excel('outputs/bridge_axis.xlsx')

###########################################################################################
"""EXPORT MOMENTS AND STRESSES DUE TO PERMANENT DEAD LOAD(PDL), SUPER IMPOSED DEAD LOAD(SIDL),PEDESTRIAN LOAD
(PEDL) AND  OTHER DEAD LOAD(ODL)"""

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


"""Creation of required cross section with length and height inputs"""
section=Cross_section(length,height)


"""Creation of cable properties """
cable=cables(35,14,section)


I=[]
ymax=[]
ymin=[]
area_sum=[]


"""Cross Section values for given no of divisions """
for i in range(len(sc)):
    
    section.expansion_width+=expansion_calc(span,sc,cable)
    I.append(section.I)    
    ymax.append(section.ymax)
    ymin.append(section.ymin)
    area_sum.append(sum(section.section_area))






"""Calculation of loads """

PDL=Dead_Load('PDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,I,ymax,ymin)
ODL=Dead_Load('ODL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,I,ymax,ymin)
PEDL=Dead_Load('PEDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,I,ymax,ymin)
SIDL=Dead_Load('SIDL',area_sum,sc,span,l_kerblen+r_kerblen,0.3,0.065,6,2,I,ymax,ymin)

# excel_export(section)
# excel_loads(PDL,ODL,PEDL,SIDL,sc)
# print(section.Centroid)
# section.expansion_width=0.5
# print(section.cable_pos(35,14,50,12))

# print(len(section.length))
# print(cable.cable_arrangement)


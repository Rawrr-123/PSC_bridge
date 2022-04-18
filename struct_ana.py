from anastruct import SystemElements
import pandas as pd
from inspect import currentframe
# import openpyxl

# def get_linenn():
#     cf = currentframe()
#     return cf.f_back.f_lineno

df=pd.read_excel('data/box.xlsx',index_col=None,header=None)
s=0
l_kerblen=0.3
r_kerblen=0.3

d=0.5
sp=0.065

def dist_len(veh):
    if veh=="70R_T":
        l=2*(d+sp)+4.750
    if veh=="70R_W":
        l=2*(d+sp)+0.25
    if veh=="Class_A":
        l=2*(d+sp)+0.25
    return l
    

ss = SystemElements()

ss.add_element(location=[[0, 3], [df.iloc[1,4]+0, 3]])
ss.add_element(location=[[df.iloc[1,4]+0, 3], [0+df.iloc[1,4]+df.iloc[1,3], 3]])
ss.add_element(location=[[0+df.iloc[1,4]+df.iloc[1,3], 3], [0+df.iloc[1,4]+df.iloc[1,3]+df.iloc[1,5], 3]])
ss.add_element(location=[[df.iloc[1,4]+0, 3], [df.iloc[1,4]+0, 3-df.iloc[0,0]]])
ss.add_element(location=[[0+df.iloc[1,4]+df.iloc[1,3], 3], [0+df.iloc[1,4]+df.iloc[1,3], 3-df.iloc[0,1]]])
ss.add_element(location=[[df.iloc[1,4]+0, 3-df.iloc[0,0]],[0+df.iloc[1,4]+df.iloc[1,3], 3-df.iloc[0,1]]])





no=2
g=no-1
gauge=1
def class_A(g):
    global s
    s=0
    if (df.iloc[1,4]+0)<l_kerblen+0.4:
        ss.insert_node(element_id=2, location=[0+l_kerblen+0.4, 3])
        ss.insert_node(element_id=4, location=[0+l_kerblen+2.2, 3])
        for i in range(g):
            ss.insert_node(element_id=3+2*(i+1), location=[0+l_kerblen+0.4+(1.8+gauge)*(i+1), 3])
            ss.insert_node(element_id=5+2*(i+1), location=[0+l_kerblen+2.2+(1.8+gauge)*(i+1), 3])
            s=s+1

    if (df.iloc[1,4]+0)>l_kerblen+0.4:
        ss.insert_node(element_id=1, location=[0+0.4+l_kerblen, 3])
        ss.insert_node(element_id=3, location=[0+2.2+l_kerblen, 3])
        for i in range(g):
            ss.insert_node(element_id=2+2*(i+1), location=[0.4+l_kerblen+(1.8+gauge)*(i+1), 3])
            ss.insert_node(element_id=4+2*(i+1), location=[2.2+l_kerblen+(1.8+gauge)*(i+1), 3])
            s=s+1
    if s>0:
        ss.point_load(node_id=[2, 4,5,7], Fy=-54/dist_len("Class_A"))
    else:
        ss.point_load(node_id=[2, 4], Fy=-54/dist_len("Class_A"))


  

def SeventyR_T():
    if (df.iloc[1,4]+0)<l_kerblen+1.2:
        ss.insert_node(element_id=2, location=[0+l_kerblen+1.2+0.42, 3])
        ss.insert_node(element_id=4, location=[0+l_kerblen+1.2+2.06+0.42, 3])
    if (df.iloc[1,4]+0)>l_kerblen+1.2:
        ss.insert_node(element_id=1, location=[0+l_kerblen+1.2+0.42, 3])
        ss.insert_node(element_id=3, location=[0+l_kerblen+1.2+2.06+0.42, 3])
        ss.point_load(node_id=[2, 4], Fy=-(350/dist_len("70R_T")))

def SeventyR_W():
    if (df.iloc[1,4]+0)<l_kerblen+1.2:
        ss.insert_node(element_id=2, location=[0+l_kerblen+1.2+0.42, 3])
        ss.insert_node(element_id=4, location=[0+l_kerblen+1.2+1.93+0.42, 3])
    if (df.iloc[1,4]+0)>l_kerblen+1.2:
        ss.insert_node(element_id=1, location=[0+l_kerblen+1.2+0.42, 3])
        ss.insert_node(element_id=3, location=[0+l_kerblen+1.2+1.93+0.42, 3])
        ss.point_load(node_id=[2, 4], Fy=-85/dist_len("70R_W"))


class_A(g)
# SeventyR_W()
ss.add_support_fixed(node_id=5+2+2*s)
ss.add_support_fixed(node_id=6+2+2*s)





ss.solve()
ss.show_structure()
ss.show_bending_moment()


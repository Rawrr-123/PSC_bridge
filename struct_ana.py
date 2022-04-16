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
def class_A():
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
        ss.point_load(node_id=[2, 4,5,7], Fy=-10)
    else:
        ss.point_load(node_id=[2, 4], Fy=-10)


  

def SeventyR(w):
    if (df.iloc[1,4]+0)<l_kerblen+1.2:
        ss.insert_node(element_id=2, location=[0+l_kerblen+1.2, 3])
        ss.insert_node(element_id=4, location=[0+l_kerblen+2.2, 3])
    if (df.iloc[1,4]+0)>l_kerblen+1.2:
        ss.insert_node(element_id=1, location=[0+l_kerblen+1.2, 3])
        ss.insert_node(element_id=3, location=[0+l_kerblen+2.2, 3])
    if w == 'T':
        ss.point_load(node_id=[2, 4], Fy=-10)
    elif w == 'W':
        ss.point_load(node_id=[2, 4], Fy=-10)



SeventyR('T')
ss.add_support_fixed(node_id=5+2+2*s)
ss.add_support_fixed(node_id=6+2+2*s)





ss.solve()
ss.show_structure()


import pandas as pd 
import numpy as np 
import math
from irc6_2007 import impact
df1=pd.read_excel('data/box.xlsx', index_col=None,header=None)
df2=pd.read_excel('data/span.xlsx', index_col=None,header=None)
df3=pd.read_excel('data/material.xlsx', index_col=None,header=None)
# df4=pd.read_excel('data/bm_ss.xlsx', index_col=None,header=None)
dfe = pd.read_excel('outputs/max_e.xlsx', index_col=0)
span=df2.iloc[1,0]
# print(df3)
fy =df3.iloc[2,0]
fck=df3.iloc[1,0]
ll_bm=40.71
dl_bm=20.29
d= 500
# print(dfe)
ecc = dfe['MaxEccentricity'] #eccentricity

def df(ecc, webcc):
    df = (webcc/2+ecc)/webcc
    return round(df, 3)

webcc = df1.iloc[1,1]+df1.iloc[1,2] #input web center/center distance
distf = [df(i, webcc) for i in ecc]
# print(distf)
impactf=[1+impact('Class A',span),1+impact('Class A',span),1+impact('Class 70RW',span),1+impact('Class 70RW',span)]
# print(impactf)
factor=np.multiply(distf,impactf)
# print(factor)

designbm=ll_bm*1.5*max(factor)+dl_bm*1.35*max(distf)
# print(designbm)
if fy == 500:
    k=0.133
elif fy == 415:
    k =0.138

# print(designbm)
ast=(d*1000*fck+1.07*math.sqrt((0.87*1000*d**2-4*designbm)*fck*1000*1000))/(2*fy*1000)
astmin= 0.0012*1000*d
print(max(astmin,ast))
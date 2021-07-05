import pandas as pd
import math
import openpyxl



"""Bridge Sepcifications Data"""
df_bridge=pd.read_excel('outputs/section.xlsx').set_index('Name')
# print(df_bridge)
"""HFL and LWW Data"""

arr1=pd.read_csv('outputs/Linear_WW.csv').values.tolist()[0]


"""Cross Section Data"""
df_cross=pd.read_csv('data/new_Cross.csv')


box={'span':50

}

# ---------------------------------------------------------------------------
box={
    # """Bridge Specifics"""

    # """Locations of 9 parts of span"""

    'sc':[(j)/8*50 for j in range(9)],


    'span':50,

    # """Cross Sectional Area"""
    'area_sum':round(sum(pd.to_numeric(df_bridge.loc[:,'Area'])),5),

    # """Kerb Lengths"""
    'l_kerblen':float(df_bridge.loc['left kerb','Length']),
    'r_kerblen':float(df_bridge.loc['right kerb','Length']),

    # """Carriageway Width"""
    # 'cw': round(float(df_bridge.iloc[3,14][0])-float(df_bridge.iloc[3,11][0])-l_kerblen,5),
    'cw':6,

    # """Bridge Length"""
    'bridge_len' : arr1[4]
}

# -----------------------------------------------------------------



water={
    # """Lowest RL of Cross Section"""
    'lowest_bed' : min(df_cross.iloc[:, 1]),

    # """Waterway"""
    'lww' : arr1[2],

    # """HFL"""

    'HFL_initial': arr1[1],

    # """HFL after construction"""

    'HFL':  arr1[3]
}
# ----------------------------------------------------------------



bearing={

    # """Bearing Specifics"""

    'c_c':1.5
}
# ----------------------------------------------------------------------


pier={
    """Pier Speicifcs"""



    """Pier Cap """
    'pcap_len':9,
    'pcap_wide':3,
    'pcap_height':1.5,
    # pcap_area=
    # """Pier Stem"""
#     'pout_dia':3,
#     'pin_dia':1.5,
#     'clear_height': math.ceil(water['HFL']) + 3 - math.floor(water['lowest_bed'])-pier['pcap_height'],
#
#     # """Lever Arms"""
#     'l_larm':(pcap_len-bearing.c_c)/2,
#     'r_larm':(pcap_len+bearing.c_c)/2,
#     't_larm':pcap_wide/2
}
#

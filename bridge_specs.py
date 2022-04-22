import pandas as pd
import math
import openpyxl


"""Bridge Sepcifications Data"""
df_bridge=pd.read_excel('outputs/section.xlsx').set_index('Name')

"""HFL and LWW Data"""

arr1=pd.read_csv('outputs/Linear_WW.csv').values.tolist()[0]


"""Cross Section Data"""
df_cross=pd.read_csv('data/new_Cross.csv')


# ---------------------------------------------------------------------------
box={
    # """Bridge Specifics"""

    # """Locations of 9 parts of span"""

    'sc':[(j)/8*50 for j in range(9)],


    'span':50,

    # """Cross Sectional Area"""
    'area_sum':round(sum(pd.to_numeric(df_bridge.loc[:,'Area'])),5),



    # """Carriageway Width"""

    # """Bridge Length"""
    'bridge_len' : arr1[4],

    'pillar_len':0.6,
    'pillar_hei':3.2,
    'botslab_len':2.4,
    'botslab_hei':0.5,
    'topslab_len':2.4,
    'topslab_hei':0.3,
    'rec_cant_length':1.8,
    'rec_cant_height':0.15,
    'lef_kerb_len':0.6,
    'lef_kerb_hei':0.3,
    'rig_kerb_len': 0.6,
    'rig_kerb_hei': 0.3,
    'tri_cant_len':1.8,
    'tri_cant_hei':0.3,
    'chamfer_len':0.45,
    'chamfer_hei':0.15
}

box.update({
    'cw':2*box['rec_cant_length']+box['topslab_len']-box['lef_kerb_len']-box['rig_kerb_len']

})

# -----------------------------------------------------------------



water={
    # """Lowest RL of Cross Section"""
    'lowest_bed' : min(df_cross.iloc[:, 1]),

    # """Waterway"""
    'lww' : arr1[2],

    # """HFL"""

    'HFL_initial': arr1[1],

    # """HFL after construction"""

    'HFL':  arr1[3],

    'Q':516.89,

    'cross_area':arr1[5],

    'lww_final':arr1[4]
}
# ----------------------------------------------------------------



bearing={

    # """Bearing Specifics"""

    'c_c':1.5
    'bearing_ht':0.6
}
# ----------------------------------------------------------------------


pier={
    # """Pier Speicifcs"""



    # """Pier Cap """
    'pcap_len':9,
    'pcap_wide':3,
    'pcap_height':1.5,


    # """Pier Stem"""
    'pout_dia':3,
    'pin_dia':1.5,



}



pier.update({

    'clear_height': math.ceil(water['HFL']) + 3 - math.floor(water['lowest_bed'])-pier['pcap_height'],
    'stem_area':((pier['pout_dia']**2)*math.pi/4)-((pier['pin_dia']**2)*math.pi/4),
    
#
    # """Lever Arms"""
    'l_larm':(pier['pcap_len']-bearing['c_c'])/2,
    'r_larm':(pier['pcap_len']+bearing['c_c'])/2,
    't_larm':pier['pcap_wide']/2,
    


         })

pier.update({
    'stem_vol':pier['stem_area']*pier['clear_height']

      })
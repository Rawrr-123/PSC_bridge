import pandas as pd
import math



"""Bridge Sepcifications Data"""
df_bridge=pd.read_csv('outputs/DL.csv')
# print(df_bridge.iloc[1,11])

"""HFL and LWW Data"""

arr1=pd.read_csv('outputs/Linear_WW.csv').values.tolist()[0]


"""Cross Section Data"""
df_cross=pd.read_csv('data/new_Cross.csv')


# ---------------------------------------------------------------------------
class box:
    """Bridge Specifics"""

    """Locations of 9 parts of span"""
    sc=[(j)/8*50 for j in range(9)]


    span=50

    """Cross Sectional Area"""
    area_sum=round(sum(pd.to_numeric(df_bridge.iloc[5,1:])),5)

    """Kerb Lengths"""
    l_kerblen=float(df_bridge.iloc[1,11])
    r_kerblen=float(df_bridge.iloc[1,14])

    """Carriageway Width"""
    cw = round(float(df_bridge.iloc[3,14])-float(df_bridge.iloc[3,11])-l_kerblen,5)

    """Bridge Length"""
    bridge_len = arr1[4]
# -----------------------------------------------------------------



class water:
    """Lowest RL of Cross Section"""
    lowest_bed = min(df_cross.iloc[:, 1])

    """Waterway"""
    lww = arr1[2]

    """HFL"""

    HFL_initial = arr1[1]

    """HFL after construction"""

    HFL = arr1[3]

# ----------------------------------------------------------------



class bearing:
    """Bearing Specifics"""

    c_c=1.5

# ----------------------------------------------------------------------


class pier:
    """Pier Speicifcs"""



    """Pier Cap """
    pcap_len=9
    pcap_wide=3
    pcap_height=1.5

    """Pier Stem"""
    pout_dia=3
    pin_dia=1.5
    clear_height = math.ceil(water.HFL) + 3 - math.floor(water.lowest_bed)-pcap_height

    """Lever Arms"""
    l_larm=(pcap_len-bearing.c_c)/2
    r_larm=(pcap_len+bearing.c_c)/2
    t_larm=pcap_wide/2



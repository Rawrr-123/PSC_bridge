##### importing packages ####
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from allinput import main_input
from irc6_2007 import *

from reaction import find_bm, find_sf, find_ra, find_rb
# from bridge_specs import box, bearing

#### bridge specs ####
if False:
    main_input()

df=pd.read_excel('data/span.xlsx',index_col=None,header=None)
span = int(df.iloc[2])

c_c = 3 #input

#### Live load calculation ####
vehicles = [ll_A, ll_70R, ll_70RT]
classA_pair, class70R, class70RT = [list(i.loadpair) for i in vehicles]
loads = [classA_pair, class70R, class70RT]



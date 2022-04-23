# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from allinput import main_input
from irc6_2007 import *

from reaction import find_bm, find_sf, find_ra, find_rb
# from bridge_specs import box, bearing

# %% [markdown]
# #### inputs

# %%
span = 60

# %% [markdown]
# #### defining loads

# %%
vehicles = [ll_A, ll_70R, ll_70RT]
classA_pair, class70R, class70RT = [list(i.loadpair) for i in vehicles]
loads = [classA_pair, class70R, class70RT]

# %% [markdown]
# #### maxBM, maxSF at equal intervals
# when each vehicle from the list of vehicles travels along the span, max reactions (BM and SF+/-) at equally divided intervals are calculated and stored in maxBMs, maxSFs_plus, maxSFs_minus.

# %%
#input
def max_rxn(loads, span):
    """

    Args:
        loads: loads pair [(x, axle_load)]
        span: span in metres

    Returns:
        dataframe containing max reactions at intermediate spans for each live load type
    """
    maxBMs = []
    maxSFs_plus = []
    maxSFs_minus = []
    for i in range(len(loads)):
        maxBM = []
        maxSF_plus = []
        maxSF_minus = []
        for j in range(9):
            at = span / 8 * j
            first_wheel_at = 0
            step = 0.1

            BM = find_bm(span, 0, at)
            SF_plus = find_sf(span, 0, at)
            SF_minus = find_sf(span, 0, at)
            for k in range(int((span + loads[i][-1][0]) / step) + 2):  # '+2' to make sure the load moves all the way to
                # end until it has no effect
                bm = 0
                sf = 0
                for this in loads[i]:
                    a, load = this
                    pos = -a + first_wheel_at
                    bm = bm + find_bm(span, pos, at) * load
                    sf = sf + find_sf(span, pos, at) * load
                first_wheel_at += step
                BM = bm if bm > BM else BM
                SF_plus = sf if sf > SF_plus else SF_plus
                SF_minus = sf if sf < SF_minus else SF_minus
            maxBM.append(round(BM, 3))
            maxSF_plus.append(round(SF_plus, 3))
            maxSF_minus.append(round(SF_minus, 3))
        maxBMs.append(maxBM)
        maxSFs_plus.append(maxSF_plus)
        maxSFs_minus.append(maxSF_minus)
    
    A = ['MaxBM', 'MaxSF+', 'MaxSF-']
    B = ['ClassA', 'Class70RW', 'Class70RT']

    iterables = [A, B]
    index = pd.MultiIndex.from_product(iterables)

    C = []

    for i in [maxBMs, maxSFs_plus, maxSFs_minus]:
        C.extend(i)

    df = pd.DataFrame(C, index=index, columns=[span / 8 * i for i in range(9)])
#     print(df.loc[('ClassA', 'MaxSF-')])   ## you can navigate using loc, iloc

    new_row = df.loc['MaxSF+'].where(df.loc['MaxSF+'] > abs(df.loc['MaxSF-']), abs(df.loc['MaxSF-']))

    new_row.index = pd.MultiIndex.from_product([['MaxSF'], B])
    df = pd.concat([df, new_row])
    
    return df

# %% [markdown]
# #### impact factor

# %%
IF = [impact(i.name, span) for i in vehicles]

# %% [markdown]
# #### output #1

# %%
df_maxR = max_rxn(loads, span) # without impact factor
df_maxR.to_excel('outputs/loads.xlsx') # uncomment to save as excel file


# %%
# df_maxRxn*2

# %%




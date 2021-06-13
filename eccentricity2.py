from matplotlib import pyplot as plt

from carriageway import Carriageway, Combination, Arrangement
import pandas as pd

carriageway = Carriageway(width=10)
combinations = carriageway.combinations()
list_combinations = []
list_max_e = []
list_plot = []
for i in combinations:
    list_combinations.append([i.classA, i.class70Rw, i.class70Rt])
    arrangements = i.arrangements()
    list_arrangements = []
    eccentricity = []
    max_e = 0
    for k in arrangements:
        list_arrangements.append(k.veh)
        e = k.eccentricity()
        eccentricity.append(e)
        max_e = e if abs(e) > abs(max_e) else max_e
    list_max_e.append(max_e)
    # print(list_arrangements, eccentricity)
    # list_plot.append(arrangements[eccentricity.index(max_e)].plot_signal())   # uncomment to display plot

df = pd.DataFrame(list_combinations, columns=['ClassA', 'Class70Rw', 'Class70Rt'], index=[f'comb{i+1}' for i in range(len(list_combinations))])
df['MaxEccentricity'] = list_max_e
print(df)

# for i in list_plot:
#     i.plot()
#     plt.show()

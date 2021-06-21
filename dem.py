import pandas as pd

from carriageway import Arrangement

# carr = Carriageway(width=15)
# comb = carr.combinations()
# for j in comb:
#     print(j)
#     arr = j.arrangements()
#     plots = []
#     for i in arr:
#         print(i)
#         ax = i.plot_signal()
#         if ax is not None:
#             plots.append(ax)
#             print(i.eccentricity())
#     for i in plots:
#         i.plot()
#         plt.show()

# arr = Arrangement('a', 4.3)
# arr.get_position()
# print(arr.position, arr.veh_weight, arr.veh_width)
# ax = arr.plot_signal()
# print(ax)

df = pd.read_excel('outputs/loads.xlsx', index_col=[0, 1])
print(df.loc['MaxBM'][25], (df.loc['MaxBM'][25]*0.5).dot([2, 0, 0]))

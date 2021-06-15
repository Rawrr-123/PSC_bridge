from matplotlib import pyplot as plt

from carriageway import Arrangement, Combination, Carriageway
carr = Carriageway(9.7)
comb = carr.combinations()
for j in comb:
    print(j)
    arr = j.arrangements()
    plots = []
    for i in arr:
        print(i)
        ax = i.plot_signal()
        plots.append(ax)
        print(i.eccentricity())
    for i in plots:
        i.plot()
        plt.show()

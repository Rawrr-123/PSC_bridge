from matplotlib import pyplot as plt

from carriageway import Carriageway
carr = Carriageway(width=15)
comb = carr.combinations()
for j in comb:
    print(j)
    arr = j.arrangements()
    plots = []
    for i in arr:
        print(i)
        ax = i.plot_signal()
        if ax is not None:
            plots.append(ax)
            print(i.eccentricity())
    for i in plots:
        i.plot()
        plt.show()

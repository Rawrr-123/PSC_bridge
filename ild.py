from matplotlib import pyplot as plt

from reaction import find_bm
from load import ll_70R
from bridge_specs import box

span=box.span


at = 25
first_wheel_at = 0
step = 1
il0 = {'first_wheel_at': [], 'BM': []}

for i in range(int((span + ll_70R.wheel_length) / step) + 1):
    bm = 0
    for j in ll_70R.loadpair:
        a, load = j
        pos = -a + first_wheel_at
        bm = bm + find_bm(span, pos, at) * load
    il0['first_wheel_at'].append(first_wheel_at)
    il0['BM'].append(bm)
    first_wheel_at += step

print(il0)
plt.plot(il0["first_wheel_at"], il0["BM"])
plt.title(f'ILD of BM at {at}m when load 70R is traversing along the span of {span}m')
plt.xlabel('First wheel at')
plt.ylabel('BM')
plt.plot()
plt.show()

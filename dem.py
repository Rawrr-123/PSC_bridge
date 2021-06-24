import pandas as pd
from bridge_specs import span,c_c
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
from load import ll_A, ll_70R, ll_70RT

vehicles = [ll_A, ll_70R, ll_70RT]
from reaction import find_rb, find_ra



reactions = []

max_sums = []
lefts = []
rights = []
max_sums_at = []
for veh in vehicles:
    dummy_load = list(veh.loadpair)
    no = 2
    nose_dist = 20
    if veh.name == 'Class 70RT':
        nose_dist = 90
        no = 1
    elif veh.name == 'Class 70RW':
        nose_dist = 31.52

    final_load = list(dummy_load)
    max_sum_at = 0
    for i in range(no - 1):
        delta = dummy_load[-1][0] + nose_dist
        final_load.extend([(i[0] + delta, i[1]) for i in dummy_load])

    sumlr = 0
    nleft = 0
    nright = 0

    head_at = 0
    step = 0.05
    for i in range(int(90 / step)):
        left = 0
        right = 0
        for j in final_load:
            rb = find_rb(span, head_at - j[0], c_c / 2, c_c / 2) * j[1]
            ra = find_ra(span, head_at - j[0] - (span + c_c), c_c / 2, c_c / 2) * j[1]
            temp = 0
            if head_at - j[0] == span + c_c / 2:
                print('hjgjh')
                temp = (ra + rb) / 2
                ra = temp
                rb = temp
            left += rb
            right += ra

        if left + right > sumlr:
            sumlr = left + right
            nleft, nright = left, right
            max_sum_at = head_at

        head_at = round(head_at + step, 5)
    max_sums.append(sumlr)
    lefts.append(nleft)
    rights.append(nright)
    max_sums_at.append(max_sum_at)

df = pd.DataFrame([lefts, rights, max_sums, max_sums_at], columns=['class A', '70RW', '70RT'],
                  index=['RL', "RR", 'sum', 'max_load_at'])
print(df)

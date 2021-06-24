import csv
import math
import matplotlib.pyplot as plt
import pandas as pd


plt.style.use('seaborn')
# plt.ioff()

original_coordinates = []
with open('data/cross.csv') as csv_file:
    #
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        original_coordinates.append((float(row[0]), float(row[1])))


def transform(ref, coordinates, lim=200):
    transformed = []
    for _index, i in enumerate(coordinates):
        if i[0] < ref - lim / 2:
            transformed.append((i[0], i[1] + 50))
            if coordinates[_index + 1][0] > ref - lim / 2:
                _y = interpolate_y(i, coordinates[_index + 1], ref - lim / 2)
                transformed.append((ref - lim / 2 - 0.00000001, _y + 50))
                transformed.append((ref - lim / 2, _y))
        elif ref - lim / 2 < i[0] < ref + lim / 2:
            transformed.append(i)
        elif i[0] > ref + lim / 2:
            if coordinates[_index - 1][0] < ref + lim / 2:
                _y = interpolate_y(i, coordinates[_index - 1], ref + lim / 2)
                transformed.append((ref + lim / 2, _y))
                transformed.append((ref + lim / 2 + 0.00000001, _y + 50))
            transformed.append((i[0], i[1] + 50))
    return transformed


def interpolate_x(p1, p2, h):
    return p1[0] + (h - p1[1]) * ((p2[0] - p1[0]) / (p2[1] - p1[1]))


def interpolate_y(p1, p2, _x):
    return p1[1] + (_x - p1[0]) * ((p2[1] - p1[1]) / (p2[0] - p1[0]))


ref_point = -15
span_limit = 100
new_coordinates = transform(ref_point, original_coordinates, lim=200)


for g in range(2):
    if g==0:
        pairs=original_coordinates
    else:
        pairs=new_coordinates
    x = [i[0] for i in pairs]
    y = [i[1] for i in pairs]
    datum = 1065
    min_rl = min(y)
    stage = []
    discharge = []
    linearWW = []

    while datum >= min_rl:
        area = 0
        perimeter = 0
        breadth = 0
        for index, pair in enumerate(pairs):
            if pair[1] <= datum:
                previous = index - 1 if index - 1 > 0 else 0
                if pairs[previous][1] > datum:
                    _x = interpolate_x(pairs[previous], pair, datum)
                    del_x = pair[0] - _x
                    del_y0 = datum - pair[1]
                    del_y1 = 0
                else:
                    del_x = pair[0] - pairs[previous][0]
                    del_y0 = datum - pair[1]
                    del_y1 = datum - pairs[previous][1]

                del_y = del_y0 - del_y1
                perimeter += math.sqrt(del_y ** 2 + del_x ** 2)
                area += (del_y0 + del_y1) / 2 * del_x
                breadth += del_x
                # try:
                if pairs[index + 1][1] > datum:
                    _x = interpolate_x(pair, pairs[index + 1], datum)
                    del_x = _x - pair[0]
                    del_y0 = 0
                    del_y1 = datum - pair[1]
                    del_y = del_y0 - del_y1
                    perimeter += math.sqrt(del_y ** 2 + del_x ** 2)
                    area += (del_y0 + del_y1) / 2 * del_x
                    breadth += del_x
                # except:
                #     continue
        r = area / perimeter
        s = 0.03957
        q = 1 / 0.035 * area * pow(r, 2 / 3) * pow(s, 1 / 2)
        stage.append(datum)
        discharge.append(q)
        linearWW.append(breadth)
        datum -= 0.1

    designQ = 516  # input design discharge
    p1 = 0
    q1 = 0
    pb = 0
    qb = 0
    for index, q in enumerate(discharge):
        if designQ > q:
            p1 = (stage[index - 1], discharge[index - 1])
            q1 = (stage[index], q)
            pb = (linearWW[index - 1], discharge[index - 1])
            qb = (linearWW[index], q)
            break
    if pairs == new_coordinates:
        st_new = interpolate_x(p1, q1, designQ)
        lww_new = interpolate_x(pb, qb, designQ)
    else:
        st=interpolate_x(p1, q1, designQ)
        lww=interpolate_x(pb, qb, designQ)

plt.rcParams['figure.figsize'] = (9, 6)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(discharge, stage)
ax1.set_xlabel('Discharge (Cumec)')
ax1.set_ylabel('Stage (m)')
ax1.set_title('Rating Curve\n')
ax1.axhline(y=st, linewidth=0.5)
ax1.axvline(x=designQ, linewidth=0.5)
ax1.text(designQ, st - 0.15, f' design Q = {designQ}\n stage = {st}')

ax2.plot(x, y)
ax2.set_ylim([1062, 1070])
ax2.set_xlim([ref_point - span_limit / 2 - 10, ref_point + span_limit / 2 + 10])
ax2.set_xlabel('x (Cumec)')
ax2.set_ylabel('RL (m)')
ax2.set_title('Cross Section\n')
ax2.axhline(y=st, linewidth=0.5, label=f'Design Flood Level @ {round(st, 4)}m', color='grey')
# ax2.axvline(x=designQ, linewidth=0.5)
ax2.text(-40, st, f' Linear Waterway Width {round(lww, 4)}m\n', horizontalalignment='center')
plt.legend()
plt.tight_layout()

# fig1.savefig('outputs/rating_curve.png')
# fig2.savefig('outputs/cross_section.png')

#
# x = [i[0] for i in pairs]
# y = [i[1] for i in pairs]
# plt.plot(x, y)
# plt.show()

(pd.DataFrame([st,lww,st_new,lww_new],columns=['Values'],index=['HFL','Linear Waterway','HFL after construction','LWW after construction']).T).to_csv('outputs/Linear_WW.csv',encoding='utf-8')
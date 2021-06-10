import csv
import math
import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.ioff()

dist = []
rl = []
with open('data/cross.csv') as csv_file:
    #
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # print(row)
        dist.append(float(row[0]))
        rl.append(float(row[1]))


def interpolate_x(p1, p2, h):
    return p1[0] + (h - p1[1]) * ((p2[0] - p1[0]) / (p2[1] - p1[1]))


min_rl = min(rl)
pairs = list(zip(dist, rl))  # [(x, rl)]
datum = 1065

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
                x = interpolate_x(pairs[previous], pair, datum)
                del_x = pair[0] - x
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
                x = interpolate_x(pair, pairs[index + 1], datum)
                # print(pair, pairs[index+1], x, datum)
                del_x = x - pair[0]
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
p = 0
q = 0
for index, q in enumerate(discharge):
    if designQ > q:
        p1 = (stage[index - 1], discharge[index - 1])
        q1 = (stage[index], q)
        pb = (linearWW[index - 1], discharge[index - 1])
        qb = (linearWW[index], q)
        break

st = interpolate_x(p1, q1, designQ)
lww = interpolate_x(pb, qb, designQ)

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

ax2.plot(dist, rl)
ax2.set_xlabel('x (Cumec)')
ax2.set_ylabel('RL (m)')
ax2.set_title('Cross Section\n')
ax2.axhline(y=st, linewidth=0.5, label=f'Design Flood Level @ {round(st, 4)}m', color='grey')
# ax2.axvline(x=designQ, linewidth=0.5)
ax2.text(-40, st, f' Linear Waterway Width {round(lww, 4)}m\n', horizontalalignment='center')
plt.legend()
plt.tight_layout()

fig1.savefig('outputs/rating_curve.png')
fig2.savefig('outputs/cross_section.png')

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


def interpolate_x(p1, p2, h):
    return p1[0] + (h - p1[1]) * ((p2[0] - p1[0]) / (p2[1] - p1[1]))


def interpolate_y(p1, p2, x):
    return p1[1] + (x - p1[0]) * ((p2[1] - p1[1]) / (p2[0] - p1[0]))


def transform(ref, coordinates, lim=200.00):
    transformed = []
    for index in range(len(coordinates)):
        if coordinates[index][0] < ref - lim / 2:
            transformed.append((coordinates[index][0], coordinates[index][1] + 50))
            if coordinates[index + 1][0] > ref - lim / 2:
                y = interpolate_y(coordinates[index], coordinates[index + 1], ref - lim / 2)
                transformed.append((ref - lim / 2 - 0.00000001, y + 50))
                transformed.append((ref - lim / 2, y))
        elif ref - lim / 2 < coordinates[index][0] < ref + lim / 2:
            transformed.append(coordinates[index])
        elif coordinates[index][0] > ref + lim / 2:
            if coordinates[index - 1][0] < ref + lim / 2:
                y = interpolate_y(coordinates[index], coordinates[index - 1], ref + lim / 2)
                transformed.append((ref + lim / 2, y))
                transformed.append((ref + lim / 2 + 0.00000001, y + 50))
            transformed.append((coordinates[index][0], coordinates[index][1] + 50))
    return transformed


ref_point = -15
bridge_length = 247.5  # tweak
new_coordinates = transform(ref_point, original_coordinates, lim=bridge_length)

s = 0.019573923  # input


def rating_curve(upper_limit, coord, slope, step=0.01):
    """Gets rating curve for given cross section.

    Parameters
    ----------
    upper_limit : float
        upper limit of stage
    coord : list
        List of (x,y) pairs of cross section in ascending order of x
    slope : float
        longitudinal slope of river channel
    step : float (default 0.01)
        step
    Returns
    -------
    dict
        dictionary containing list of discharge, list of linearWW, list of area for respective list of stage
        for given cross section
    """

    stage = []
    discharge = []
    linearWW = []
    totalarea = []

    min_rl = min([i[1] for i in coord])
    while upper_limit >= min_rl:
        area = 0
        perimeter = 0
        breadth = 0
        for index, pair in enumerate(coord):
            if pair[1] <= upper_limit:
                previous = index - 1 if index - 1 > 0 else 0
                if coord[previous][1] > upper_limit:
                    _x = interpolate_x(coord[previous], pair, upper_limit)
                    del_x = pair[0] - _x
                    del_y0 = upper_limit - pair[1]
                    del_y1 = 0
                else:
                    del_x = pair[0] - coord[previous][0]
                    del_y0 = upper_limit - pair[1]
                    del_y1 = upper_limit - coord[previous][1]

                del_y = del_y0 - del_y1
                perimeter += math.sqrt(del_y ** 2 + del_x ** 2)
                area += (del_y0 + del_y1) / 2 * del_x
                breadth += del_x
                # try:
                if coord[index + 1][1] > upper_limit:
                    _x = interpolate_x(pair, coord[index + 1], upper_limit)
                    del_x = _x - pair[0]
                    del_y0 = 0
                    del_y1 = upper_limit - pair[1]
                    del_y = del_y0 - del_y1
                    perimeter += math.sqrt(del_y ** 2 + del_x ** 2)
                    area += (del_y0 + del_y1) / 2 * del_x
                    breadth += del_x
                # except:
                #     continue
        totalarea.append(area)
        r = area / perimeter
        q = 1 / 0.035 * area * pow(r, 2 / 3) * pow(slope, 1 / 2)
        stage.append(upper_limit)
        discharge.append(q)
        linearWW.append(breadth)
        upper_limit -= step
    return {
        'Stage': stage,
        'Discharge': discharge,
        'linearWW': linearWW,
        'Area': totalarea
    }


prop_before = rating_curve(1065, original_coordinates, s)
prop_after = rating_curve(1065, new_coordinates, s)

designQ = 516.89  # input design discharge


def findProp(target_discharge, list_Q, list_stage, list_linearww, list_area):
    """
    finds stage, linearww, area for given list of disharges and list of stages:

    Args:
    designQ: design Q (float)
    list_Q: (list)
    list_stage (list)
    list_linearww (list)
    list_area (list)
    """
    st1 = None
    st2 = None
    lww1 = None
    lww2 = None
    ar1 = None
    ar2 = None
    for index in range(len(list_Q)):
        if target_discharge > list_Q[index]:
            st1 = (list_stage[index - 1], list_Q[index - 1])
            st2 = (list_stage[index], list_Q[index])
            lww1 = (list_linearww[index - 1], list_Q[index - 1])
            lww2 = (list_linearww[index], list_Q[index])
            ar1 = (list_area[index - 1], list_Q[index - 1])
            ar2 = (list_area[index], list_Q[index])

            st = interpolate_x(st1, st2, target_discharge)
            lww = interpolate_x(lww1, lww2, target_discharge)
            ar = interpolate_x(ar1, ar2, target_discharge)
            break
    return st, lww, ar


hfl_before, linearww_before, area_before = findProp(
    designQ,
    prop_before['Discharge'],
    prop_before['Stage'],
    prop_before['linearWW'],
    prop_before['Area']
)

hfl_after, linearww_after, area_after = findProp(
    designQ,
    prop_after['Discharge'],
    prop_after['Stage'],
    prop_after['linearWW'],
    prop_after['Area']
)

plt.rcParams['figure.figsize'] = (9, 6)

fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()

ax1.plot(prop_after['Discharge'], prop_after['Stage'])
ax1.set_xlabel('Discharge (Cumec)')
ax1.set_ylabel('Stage (m)')
ax1.set_title('Rating Curve after construction\n')
ax1.axhline(y=hfl_after, linewidth=0.5)
ax1.axvline(x=designQ, linewidth=0.5)
ax1.text(designQ, hfl_after - 0.15, f' design Q = {designQ}\n stage = {hfl_after}')

# ax2.plot(x, y)
# ax2.set_ylim([1062, 1070])
# ax2.set_xlim([ref_point - span_limit / 2 - 10, ref_point + span_limit / 2 + 10])
# ax2.set_xlabel('x (Cumec)')
# ax2.set_ylabel('RL (m)')
# ax2.set_title('Cross Section\n')
# ax2.axhline(y=hfl, linewidth=0.5, label=f'Design Flood Level @ {round(hfl, 4)}m', color='grey')
# # ax2.axvline(x=designQ, linewidth=0.5)
# ax2.text(-40, hfl, f' Linear Waterway Width {round(lww, 4)}m\n', horizontalalignment='center')
# plt.legend()
# plt.tight_layout()

fig1.savefig('outputs/rating_curve.png')
# fig2.savefig('outputs/cross_section.png')

#
# x = [i[0] for i in pairs]
# y = [i[1] for i in pairs]
# plt.plot(x, y)
# # plt.show()

df = pd.DataFrame([[hfl_before, linearww_before, area_before, hfl_after, linearww_after, area_after]],
                  columns=('HFL_before',
                           'LWW_before',
                           'Area_before',
                           'HFL_after',
                           'LWW_after',
                           'Area_after'))

df.to_csv('outputs/Linear_WW.csv')

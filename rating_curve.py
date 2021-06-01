import csv
import matplotlib.pyplot as plt
import math

dist = []
rl = []
with open('cross.csv') as csv_file:
    #
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        dist.append(float(row[0]))
        rl.append(float(row[1]))


def interpolate_x(p1, p2, h):
    return p1[0] + (h - p1[1]) * ((p2[0] - p1[0]) / (p2[1] - p1[1]))


min_rl = min(rl)
pairs = list(zip(dist, rl)) #[(x, rl)]
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
            try:
                if pairs[index + 1][1] > datum:
                    x = interpolate_x(pair, pairs[index + 1], datum)
                    del_x = x - pair[0]
                    del_y0 = 0
                    del_y1 = datum - pair[1]
                    del_y = del_y0 - del_y1
                    perimeter += math.sqrt(del_y ** 2 + del_x ** 2)
                    area += (del_y0 + del_y1) / 2 * del_x
                    breadth += del_x
            except:
                continue
    r = area / perimeter
    q = 1/0.035*area*pow(r, 2/3)*pow(0.22258, 1/2)
    stage.append(datum)
    discharge.append(q)
    linearWW.append(breadth)
    datum -= 0.1


plt.plot(discharge, stage)

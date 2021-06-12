from comb import comb
from load import ll_A, ll_70R, ll_70RT

from itertools import permutations
from matplotlib import pyplot as plt
import numpy as np


def vehicle(character):
    if character == 'a':
        return ll_A
    elif character == 'b':
        return ll_70R
    elif character == 'c':
        return ll_70RT


class Arrangement:
    center = []
    load = []

    def __init__(self, veh, width=None):
        self.veh = veh
        self.width = width
        cursor = 0
        if self.veh[0] == 'a':
            cursor += 150 + ll_A.width
            Arrangement.center.append(cursor - ll_A.width / 2)
        else:
            cursor += max(1200 + vehicle(self.veh[0]).width, 7250)
            Arrangement.center.append(1200 + (vehicle(self.veh[0]).width / 2))
        right_wheel = Arrangement.center[0] + (vehicle(self.veh[0]).width / 2)
        Arrangement.load.append(vehicle(self.veh[0]).weight)
        index = 1
        for _i in self.veh[1:]:
            gap = max(cursor - right_wheel, 1200)
            if _i == 'a':
                Arrangement.center.append(right_wheel + gap + ll_A.width / 2)
                cursor = Arrangement.center[index - 1] - ll_A.width / 2
            else:
                gap = max(cursor - right_wheel, 3500 - vehicle(_i).width / 2, 1200)
                Arrangement.center.append(right_wheel + gap + vehicle(_i).width / 2)
                cursor = Arrangement.center[index] + max(vehicle(_i).width, 3500)
            right_wheel = Arrangement.center[index] + vehicle(_i).width / 2
            Arrangement.load.append(vehicle(self.veh[index]).weight)
            index += 1

    def __str__(self):
        _string = '('
        for _i in self.veh:
            _string += f'{_i}'
        _string += ')'
        return _string

    def eccentricity(self):

        arr_dist_from_center = np.array(Arrangement.center) - self.width / 2
        arr_load = np.array(Arrangement.load)
        eccentricity = (arr_dist_from_center * arr_load).sum() / arr_load.sum()
        return eccentricity

    def plot_signal(self):
        f, ax = plt.subplots(figsize=(7, 3))
        plt.subplots_adjust(bottom=0.25)
        ax.plot()
        ax.set_ylim(-0.02, 0.1)

        ticks = []
        index = 0
        for _i in Arrangement.center:
            left_wheel = _i - vehicle(self.veh[index]).width / 2
            right_wheel = _i + vehicle(self.veh[index]).width / 2
            ticks.extend([left_wheel, _i, right_wheel])
            ax.arrow(_i, 0.03, 0, -0.030, length_includes_head=True, head_width=100, head_length=0.005)
            ax.hlines(y=0, xmax=right_wheel, xmin=left_wheel)
            ax.text(_i, -0.01, f'{vehicle(self.veh[index]).name}', ha='center')
            index += 1
        ax.set_xticks(ticks)
        ax.set_xticklabels(ticks, rotation=45, fontsize=7)
        ax.set_xlabel('Distance from left abutment in metres')
        ax.set_yticks([])

        return ax


class Combination:
    def __init__(self, nclass_a, nclass70_rw, nclass70_rt):
        self.classA = nclass_a
        self.class70Rw = nclass70_rw
        self.class70Rt = nclass70_rt

    def arrangements(self):
        obj = []
        veh = []  # all vehicles <'a'><'b'><'c'> as indices for <classA><70RW><70RT>
        index = bytes('a', 'utf-8')
        for i in [self.classA, self.class70Rw, self.class70Rt]:
            for j in range(i):
                veh.append(chr(index[0]))
            index = bytes(chr(index[0] + 1), 'utf-8')
        perm = permutations(veh)
        p = list(set(perm))
        for _i in p:
            obj.append(Arrangement(_i))
        return obj

    def __str__(self):
        return f'{self.classA}, {self.class70Rw}, {self.class70Rt}'


class Carriageway:
    def __init__(self, width):
        self.width = width

    def combinations(self):
        raw = comb(width=self.width)
        obj = []
        for _i in raw:
            obj.append(Combination(_i[0], _i[1], _i[2]))
        return obj


arrangement1 = Arrangement(['a', 'b', 'b'], 16600)
plot = arrangement1.plot_signal()
print(arrangement1.eccentricity())

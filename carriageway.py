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


class Carriageway:
    def __init__(self, width):
        self.width = width

    def combinations(self):
        raw = comb(width=self.width)
        obj = []
        for _i in raw:
            obj.append(Combination(_i[0], _i[1], _i[2], self.width))
        return obj


class Combination(Carriageway):
    def __init__(self, nclass_a, nclass70_rw, nclass70_rt, width):
        super().__init__(width)
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
            obj.append(Arrangement(_i, self.width))
        return obj

    def __str__(self):
        return f'{self.classA}, {self.class70Rw}, {self.class70Rt}'


class Arrangement(Carriageway):
    position = []
    weight = []
    get_position_index = 0
    last_wheel = 0

    def __init__(self, veh, width):
        super().__init__(width)
        self.veh = veh
        self.width = width
        self.position = []
        self.weight = []
        self.get_position_index = 0
        self.last_wheel = 0

    def __str__(self):
        _string = '('
        for _i in self.veh:
            _string += f'{_i}'
        _string += ')'
        return _string

    def get_position(self):
        cursor = 0
        center = []
        load = []

        g = 0.4 + (self.width - 5.3) if 5.3 <= self.width <= 6.1 else 1.2  # for ClassA and general

        if self.veh[0] == 'a':
            cursor += 0.150 + ll_A.width
            center.append(cursor - ll_A.width / 2)
        else:
            cursor += max(1.200 + vehicle(self.veh[0]).width, 7.250)
            center.append(1.200 + (vehicle(self.veh[0]).width / 2))
        right_wheel = center[0] + (vehicle(self.veh[0]).width / 2)
        load.append(vehicle(self.veh[0]).weight)
        index = 1
        for _i in self.veh[1:]:
            gap = max(cursor - right_wheel, g)
            if _i == 'a':
                center.append(right_wheel + gap + ll_A.width / 2)
                cursor = center[index - 1] - ll_A.width / 2
            else:
                gap = max(cursor - right_wheel, 3.500 - vehicle(_i).width / 2, 1.200)
                center.append(right_wheel + gap + vehicle(_i).width / 2)
                cursor = center[index] + max(vehicle(_i).width, 3.500)
            right_wheel = center[index] + vehicle(_i).width / 2
            load.append(vehicle(self.veh[index]).weight)
            index += 1
        self.position = center
        self.weight = load
        self.get_position_index = 1
        self.last_wheel = right_wheel

    def check_exceedance(self):
        gap_last = 0.15 if self.veh[-1] == 'a' else 1.2
        if self.last_wheel + gap_last > self.width:
            return 0
        else:
            return 1

    def check_from_right(self):
        if self.veh[-1] == 'b' or self.veh[-1] == 'c':
            no_permission_zone = 7.25
        else:
            no_permission_zone = 0

        if self.position[-2] + vehicle(self.veh[-2]).width / 2 > self.width - no_permission_zone:
            return 0
        else:
            return 1

    def eccentricity(self):

        if Arrangement.get_position_index == 0:
            Arrangement.get_position(self)
        if Arrangement.check_exceedance(self) * Arrangement.check_from_right(self) == 1:
            arr_dist_from_center = np.array(self.position) - self.width / 2
            arr_load = np.array(self.weight)
            eccentricity = (arr_dist_from_center * arr_load).sum() / arr_load.sum()
            return eccentricity

    def plot_signal(self):
        if Arrangement.get_position_index == 0:
            Arrangement.get_position(self)
        if Arrangement.check_exceedance(self) * Arrangement.check_from_right(self) == 1:
            f, ax = plt.subplots(figsize=(7, 3))
            plt.subplots_adjust(bottom=0.25)
            ax.plot()
            ax.set_xlim(-0.1, self.width)
            ax.set_ylim(-0.02, 0.1)
            ax.hlines(y=0, xmax=self.width, xmin=0, lw=0.5)
            ticks = []
            for _index, _i in enumerate(self.veh):
                left_wheel = self.position[_index] - vehicle(self.veh[_index]).width / 2
                right_wheel = self.position[_index] + vehicle(self.veh[_index]).width / 2
                ticks.extend([round(left_wheel, 2), round(self.position[_index], 2), round(right_wheel, 2)])
                ax.arrow(self.position[_index], 0.01, 0, -0.010, length_includes_head=True, head_width=0.1,
                         head_length=0.005)
                ax.hlines(y=0, xmax=right_wheel, xmin=left_wheel)
                ax.text(self.position[_index], -0.01, f'{vehicle(self.veh[_index]).name}', ha='center')
                ax.text(self.position[_index], 0.015, f'{self.weight[_index]}', ha='center')
            ticks.append(self.width)
            ax.set_xticks(ticks)
            ax.set_xticklabels(ticks, rotation=45, fontsize=7)
            ax.set_xlabel('Distance from left abutment in metres')
            ax.set_yticks([])
            return ax

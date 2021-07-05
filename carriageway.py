from comb import comb
from load import ll_A, ll_70R, ll_70RT, Load

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

    def get_value(self):
        return [self.classA, self.class70Rw, self.class70Rt]

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

    def max_e(self):
        arrangements = self.arrangements()
        max_e = 0
        for k in arrangements:
            if k.check_exceedance() * k.check_from_right() == 1:
                e = k.eccentricity()
                max_e = e if abs(e) > abs(max_e) else max_e
        return max_e

    def __str__(self):
        return f'{self.classA}, {self.class70Rw}, {self.class70Rt}'


class Arrangement(Carriageway):
    position = []
    veh_weight = []
    get_position_index = 0
    last_wheel = 0
    veh_name = []

    def __init__(self, veh, width):
        super().__init__(width)
        self.veh = list(veh)
        self.width = width
        self.position = []
        self.veh_name = [vehicle(i).name for i in self.veh]
        self.veh_width = [vehicle(i).width for i in self.veh]
        self.veh_weight = [vehicle(i).weight for i in self.veh]

        self.get_position_index = 0
        self.last_wheel = 0

    def __str__(self):
        _string = '('
        for _i in self.veh:
            _string += f'{_i}'
        _string += ')'
        return _string

    def get_value(self):
        return [self.veh]

    def get_position(self):
        cursor = 0
        center = []

        g = 0.4 + (self.width - 5.3) if 5.3 <= self.width <= 6.1 else 1.2  # for ClassA and general

        if self.veh[0] == 'a':
            cursor += 0.150 + self.veh_width[0]
            center.append(cursor - self.veh_width[0] / 2)
        else:
            cursor += max(1.200 + self.veh_width[0], 7.250)
            center.append(1.200 + self.veh_width[0] / 2)
        right_wheel = center[0] + self.veh_width[0] / 2

        for index, _i in enumerate(self.veh[1:]):
            gap = max(cursor - right_wheel, g)
            if _i == 'a':
                center.append(right_wheel + gap + self.veh_width[index + 1] / 2)
                cursor = center[index + 1 - 1] - self.veh_width[index + 1] / 2
            else:
                gap = max(cursor - right_wheel, 3.500 - self.veh_width[index + 1] / 2, 1.200)
                center.append(right_wheel + gap + self.veh_width[index + 1] / 2)
                cursor = center[index + 1] + max(self.veh_width[index + 1], 3.500)
            right_wheel = center[index + 1] + self.veh_width[index + 1] / 2

        if 4.25 < self.width < 5.3 and self.veh == ['a']:
            q = Load('q=5KN/m2', [], [], self.width - right_wheel)
            center.append(right_wheel + q.width / 2)
            self.veh.append('q')
            self.veh_name.append('q=500kg/m2')
            self.veh_width.append(q.width)
            self.veh_weight.append(5 * q.width)
        self.position = center
        self.get_position_index = 1
        self.last_wheel = right_wheel

    def check_exceedance(self):
        if self.get_position_index == 0:
            Arrangement.get_position(self)
        gap_last = 0.15 if self.veh[-1] == 'a' else 1.2
        if self.last_wheel + gap_last > self.width:
            return 0
        else:
            return 1

    def check_from_right(self):
        if self.get_position_index == 0:
            Arrangement.get_position(self)
        if len(self.veh) >= 2:
            if self.veh[-1] == 'b' or self.veh[-1] == 'c':
                no_permission_zone = 7.25
            else:
                no_permission_zone = 0

            if self.position[-2] + vehicle(self.veh[-2]).width / 2 > self.width - no_permission_zone:
                return 0
            else:
                return 1
        else:
            return 1

    def eccentricity(self):

        if self.get_position_index == 0:
            Arrangement.get_position(self)
        arr_dist_from_center = np.array(self.position) - self.width / 2
        arr_load = np.array(self.veh_weight)
        eccentricity = (arr_dist_from_center * arr_load).sum() / arr_load.sum()
        return eccentricity

    def plot_signal(self):
        if self.get_position_index == 0:
            Arrangement.get_position(self)
        f, ax = plt.subplots(figsize=(7, 3))
        plt.subplots_adjust(bottom=0.25)
        ax.plot()
        ax.set_xlim(-0.1, self.width)
        ax.set_ylim(-0.02, 0.1)
        ax.hlines(y=0, xmax=self.width, xmin=0, lw=0.5)
        ticks = []
        for _index, _i in enumerate(self.veh):
            ticks.append(self.width)
            left_wheel = self.position[_index] - self.veh_width[_index] / 2
            right_wheel = self.position[_index] + self.veh_width[_index] / 2
            ticks.extend([round(left_wheel, 2), round(self.position[_index], 2), round(right_wheel, 2)])
            ax.arrow(self.position[_index], 0.01, 0, -0.010, length_includes_head=True, head_width=0.1,
                     head_length=0.005)
            ax.hlines(y=0, xmax=right_wheel, xmin=left_wheel)
            ax.text(self.position[_index], -0.01, f'{self.veh_name[_index]}', ha='center')
            ax.text(self.position[_index], 0.015, f'{self.veh_weight[_index]}', ha='center')
        ticks.append(self.width)
        ax.set_xticks(ticks)
        ax.set_xticklabels(ticks, rotation=45, fontsize=7)
        ax.set_xlabel('Distance from left kerb in metres')
        ax.set_yticks([])
        return ax

from itertools import permutations
from load import ll_A, ll_70R, ll_70RT
import matplotlib.pyplot as plt

from comb import comb


def vehicle(character):
    if character == 'a':
        return ll_A
    elif character == 'b':
        return ll_70R
    elif character == 'c':
        return ll_70RT


class Arrangement:

    def __init__(self, veh, width=None):
        self.veh = veh
        self.width = width

    def __str__(self):
        _string = '('
        for _i in self.veh:
            _string += f'{_i}'
        _string += ')'
        return _string

    def eccentricity(self):
        center = []
        cursor = 0
        if self.veh[0] == 'a':
            cursor += 150 + ll_A.width
            center.append(cursor - ll_A.width / 2)
        else:
            cursor += max(1200 + vehicle(self.veh[0]).width, 7250)
            center.append(1200 + (vehicle(self.veh[0]).width / 2))
        right_wheel = center[0] + (vehicle(self.veh[0]).width / 2)
        index = 1
        for _i in self.veh[1:]:
            gap = max(cursor - right_wheel, 1200)
            if _i == 'a':
                center.append(right_wheel + gap + ll_A.width / 2)
                cursor = center[index - 1] - ll_A.width / 2
            else:
                gap = max(cursor - right_wheel, 3500 - vehicle(_i).width / 2, 1200)
                center.append(right_wheel + gap + vehicle(_i).width / 2)
                cursor = center[index] + max(vehicle(_i).width, 3500)
            right_wheel = center[index] + vehicle(_i).width / 2
            index += 1
        return center

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


# carr = Carriageway(width=14)
# for i in carr.combinations():
#     print(i)
#     for j in i.arrangements():
#         print(j)

plot = Arrangement(['b', 'c', 'c']).eccentricity()
print(plot)

from itertools import permutations
from matplotlib import pyplot as plt
import math
import numpy as np


class Load:
    """
    refer to cl 204.1
    """

    def __init__(self, name, pos, wheel_load, width, nose_dist):
        """

        Args:
            pos (list): successive position of wheels (and finally tail) starting from nose
            wheel_load (list): load at successive wheels
        """
        self.name = name
        self.pos = pos
        self.wheel_load = wheel_load
        self.width = width
        self.nose_dist = nose_dist

    @property
    def wheel_length(self):
        """

        Returns:

        """
        return round(sum(self.pos[1:-1]), 2)

    @property
    def length(self):
        """

        Returns: length of the vehicle

        """
        return round(sum(self.pos), 2)

    @property
    def max_weight(self):
        if self.name == 'Class A':
            return 114
        elif self.name == 'Class 70RW' or self.name == 'Class 70RT':
            return 700
        else:
            return 5

    @max_weight.setter
    def max_weight(self, weight):
        self._weight = weight

    @property
    def loadpair(self):
        """

        Returns:zip with load and position w.r.to front wheel at 0

        """
        wheel_pos = [0]
        for index, pos in enumerate(self.pos[1:-1]):
            wheel_pos.append(wheel_pos[index] + pos)
        return zip(wheel_pos, self.wheel_load)

    @property
    def weight(self):
        return sum(self.wheel_load)

    def reduced(self, to):
        reduced_load = [x*to for x in self.wheel_load]
        return Load(f'reduced {self.name}', self.pos, reduced_load, self.width, self.nose_dist)

    def __add__(self, other):
        name = self.name + ' + ' + other.name

        pos1 = self.pos
        pos2 = other.pos
        nose = max(self.nose_dist, other.nose_dist)
        total_pos = []
        total_pos.extend(pos1[:-1])
        total_pos.append(pos1[-1] + nose + pos2[0])
        total_pos.extend(pos2[1:])

        load1 = self.wheel_load
        load2 = other.wheel_load
        total_load = []
        total_load.extend(load1)
        total_load.extend(load2)

        width = max(self.width, other.width)
        return Load(name, total_pos, total_load, width, nose)


#   some standard loads

ll_70R = Load(name='Class 70RW', pos=[0.61, 3.960, 1.520, 2.130, 1.370, 3.050, 1.370, 0.91],
              wheel_load=[80, 120, 120, 170, 170, 170, 170],
              width=2.790, nose_dist=30)
ll_70RT = Load(name='Class 70RT', pos=[0.0, 0.653, 0.653, 0.653, 0.652, 0.653, 0.653, 0.653, 0.0],
               wheel_load=[50, 100, 100, 100, 100, 100, 100, 50], width=2.900, nose_dist=90)
ll_A = Load(name='Class A', pos=[0.6, 1.1, 3.2, 1.2, 4.3, 3, 3, 3, 0.9], wheel_load=[27, 27, 114, 114, 68, 68, 68, 68],
            width=2.300, nose_dist=18.5)


##################################################################################

def lane_number(CW_width):
    """
    returns number of lanes for given width.
    refer to irc6_2000 table 6.

    Args:
        CW_width: carriageway width in meters

    """
    if 20.1 <= CW_width < 23.6:
        return 6
    elif 16.6 <= CW_width < 20.1:
        return 5
    elif 13.1 <= CW_width < 16.6:
        return 4
    elif 9.6 <= CW_width < 13.1:
        return 3
    elif 5.3 <= CW_width < 9.6:
        return 2
    elif 4.25 <= CW_width < 5.3:
        return 1
    else:
        return 0


def comb(lane=None, width=None):
    """
    takes lane number as default input. you can specify CW width instead of lane by passing 'width = <width>'.
    For example: comb(width=15) is equivalent to comb(lane_number(15)).
    refer to table 6 and table 6A.

    Args:
        lane (int): no. of lanes
        width (float): carriageway width in metres

    Returns:
        list of possible combinations, each in format [no. of ClassA, no. of Class70RW, no. of Class 70RT]

    """

    if width is not None:
        lane = lane_number(width)
    nclassA = lane  # no. of classA veh (remaining)
    n70 = 0  # no. of class70 veh
    combination = []
    while nclassA >= 0:
        if n70 <= 0:
            combination.append([nclassA, 0, 0])
        else:
            for i in range(n70 + 1):
                combination.append([nclassA, n70 - i, i])
        n70 += 1
        nclassA -= 2
    return combination


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
        self.veh_weight = [vehicle(i).max_weight for i in self.veh]

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
            q = Load('q=5KN/m2', [], [], self.width - right_wheel, 0)
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
        f, ax = plt.subplots(figsize=(12, 5))
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
            ax.arrow(self.position[_index], 0.01, 0, -0.010, length_includes_head=True, head_width=0.1,
                     head_length=0.005)
            ax.hlines(y=0, xmax=right_wheel, xmin=left_wheel)
            ax.text(self.position[_index], -0.01, f'{self.veh_name[_index]}', ha='center')
            ax.text(self.position[_index], 0.015, f'{self.veh_weight[_index]}', ha='center')
        ticks.append(self.width)
        ax.set_xticks(ticks)
        ax.set_xticklabels(ticks, rotation=45, fontsize=10)
        ax.set_xlabel('Distance from left kerb in metres', fontsize = 10)
        ax.set_yticks([])
        return ax


####################################################################################

def congestion(span):
    """
    refer to 204.4
    Args:
        span: span length in metres

    Returns:
        cf: congestion factor

    """
    if 10 <= span < 30:
        cf = 1.15
    elif 30 <= span < 60:
        cf = 1.15 + (span - 30) / 30 * 0.45
    elif 60 <= span < 70:
        cf = 1.60 + (span - 60) / 10 * 0.10
    else:
        cf = 1.7
    return cf


##############################################################################

def reductionL(nlane):
    """
    Reduction in the longitudinal effect on bridges having more than two traffic lanes due to
    the low probability that all lanes will be subjected to the characteristic loads simultaneously
    shall be in accordance with the Table 8 of IRC 6 2007.

    Args:
        nlane: number of lanes

    Returns:
        rl: reduction in longitudinal effects
    """
    if nlane == 2:
        rl = 0
    elif nlane == 3:
        rl = 0.1
    else:
        rl = 0.2
    return rl


###############################################################################

def ped_ll(span, width_footway):
    """
    refer to 206.1

    Args:
        span: effective span length in m
        width_footway: width of footway in m

    Returns:
        pedll: footway loading in kg/m.sq
    """
    pedll = 0
    if span <= 50:
        pedll = (500 / 100)*width_footway
    elif 7.5 < span <= 30:
        pedll = ((500 - (40 * span - 300) / 9) / 100)*width_footway
    elif span > 30:
        pedll = (((500 - 260) + (4800 / span)) * (16.5 - width_footway) / 1500)**width_footway
        
    return pedll



#################################################################################

def impact(loading, span, material='RCC'):
    """
    Provision for impact or dynamic action shall be made by an increment of the live load
    by an impact allowance expressed as a fraction or a percentage of the applied live load.
    from irc6 cl.208

    Args:
        loading (str): options => 'classA', 'classAA', '70R', '70RT'
        span (float): span length in metres
        material (str): options => 'RCC' (default), 'steel'

    Returns:
        impact factor value (float)

    """
    if loading == 'Class A' or loading == 'Class B':
        if material == 'RCC':
            if span <= 3:
                return 0.5
            elif 3 < span < 45:
                return 4.5 / (6 + span)
            else:
                return 0.088
        if material == 'steel':
            if span <= 3:
                return 0.545
            elif 3 < span < 45:
                return 9 / (13.5 + span)
            else:
                return 0.154
    if loading == 'Class AA' or loading == 'Class 70RW' or loading == 'Class 70RT':
        if span < 9:
            if loading == 'Class 70RT':
                if span <= 5:
                    return 0.25
                else:
                    return .25 + ((.1 - .25) / (9 - 5)) * (span - 5)
            else:
                return .25
        else:
            if material == 'RCC':
                if loading == 'Class 70RT':
                    if span <= 40:
                        return 0.1
                    else:
                        return impact('Class A', span, 'RCC')
                else:
                    if span < 12:
                        return 0.25
                    else:
                        return impact('Class A', span, 'RCC')
            if material == 'steel':
                if loading == 'Class 70RT':
                    return 0.1
                else:
                    if span < 23:
                        return 0.25
                    else:
                        return impact('Class A', span, 'steel')


#################################################################################

def f_watercurrent(vel, theta=0):
    """

    Args:
        vel: velocity m/s
        theta: angle from normal direction of current in degrees

    Returns:
        p_par, p_T: pressure intensity in direction parallel and normal to pier/current direction. in kN/m.sq
    """
    v_par = vel * math.cos(math.radians(theta))
    v_T = vel * math.sin(math.radians(theta))

    # for piers with semi-circular ends
    k_par = 0.66
    k_T = 1.5

    p_par = 52 * k_par * v_par ** 2 / 100
    p_T = 52 * k_T * v_T ** 2 / 100

    return round(p_par, 3), round(p_T, 3)


################################################################################################

# computation of seismic response
def zone_factor(zone_no):
    """
    zone factor. refer to table 16
    Args:
        zone_no: classification of zone

    Returns:
        zf: zone factor
    """
    zf = {1: 0, 2: 0.1, 3: 0.16, 4: 0.24, 5: 0.36}
    return zf[zone_no]


def vib_period(d, f):
    """
    The fundamental natural period T (in seconds) of pier/abutment of the bridge along a
    horizontal direction
    refer to annex D (cl 219.5)

    Args:
        d: Appropriate dead load of the superstructure and live load in kN

        f: Horizontal force in kN required to be applied at the centre of mass of superstructure for one mm horizontal
            deflection at the top of the pier/ abutment for the earthquake in the transverse direction; and the force
            to be applied at the top of· the bearings for the earthquake in the longitudinal direction.ie: stiffness

    Returns:
        fundamental period of vibration T
    """
    return 2 * math.sqrt(d / (1000 * f))


def sag(t, soil_type):
    """
    Average responses acceleration coefficient for 5 percent damping of load resisting
    elements depending upon the fundamental period of vibration T as given in Fig. 20 IRC6
    refer to 219.5.1
    Args:
        t: fundamental period of vibration T
        soil_type: may contain soil type ('hard', 'rock', 'medium', 'mid', 'soft') or
            nominal variable for soil type ('I', 'II', 'III')

    Returns:
        Sa/g value
    """
    if soil_type.upper() == 'I' or soil_type.upper() == 'ROCK' or soil_type.upper() == 'HARD':
        if 0.00 <= t <= 0.10:
            return 1 + 15 * t
        elif 0.10 <= t <= 0.40:
            return 2.50
        elif 0.40 <= t <= 4.00:
            return 1.00 / t
    elif soil_type.upper() == 'II' or soil_type.upper() == 'MEDIUM' or soil_type.upper() == 'MID':
        if 0.00 <= t <= 0.10:
            return 1 + 15 * t
        elif 0.10 <= t <= 0.55:
            return 2.50
        elif 0.55 <= t <= 4.00:
            return 1.36 / t
    elif soil_type.upper() == 'III' or soil_type.upper() == 'SOFT':
        if 0.00 <= t <= 0.10:
            return 1 + 15 * t
        elif 0.10 <= t <= 0.67:
            return 2.50
        elif 0.67 <= t <= 4.00:
            return 1.67 / t

def ah(z, sag, r, i):
    """

    Args:
        z: Zone factor as given in table 4.2 sp114
        sag: Design acceleration coefficient
        r: Response reduction factor given in table 4.1 sp114
        i: Importance Factor given in table 4.3

    Returns:
        Design horizontal seismic coefficient
    """

    ahh = (z / 2) * sag / (r / i)
    return ahh

def mult_factor(load,direction):
    """
       Multiplication factor for different loads along different directions
       Refer to IRC-6 219.5.2"""
    if direction.upper()=="LONG":
        if load.upper()=="DL":
            return 1.00
        elif load.upper() =="LL" :
            return 0.00
        elif load.upper() =="PEDL":
            return 0.00
    elif direction=="trans":
        if load.upper()=="DL":
            return 1.00
        elif load.upper() == "LL":
            return 0.20
        elif load.upper() == "PEDL":
            return 0.20


def RR_factor(direction):
    if direction.upper()=="LONG" or "VERT":
        return 3.00
    elif direction.upper()=="TRANS":
        return 1.00

####################################################################################################

def ka(a,b,d,p):
    """ Returns the coefficient of active earth pressure Ka estimated based on Coulomb earth pressure theory."""
    k = (pow(math.cos(math.radians(p-a)),2)/((pow(math.cos(math.radians(a)),2))*math.cos(math.radians(d+a))))*pow((1/(1+pow((math.sin(math.radians(p+d))*math.sin(math.radians(p-b)))/(math.cos(math.radians(a-b))*math.cos(math.radians(d+a))),0.5))),2)
    return round(k,5)

def ca(a,b,d,p,l,av):
    """ Returns the coefficient of active earth pressure Ka estimated based on Coulomb earth pressure theory."""
    ca1 = (1+av)*(pow(math.cos(math.radians(p-a-l)),2)/((math.cos(math.radians(l))*(pow(math.cos(math.radians(a)),2))*math.cos(math.radians(d+a+l)))))*pow((1/(1+pow((math.sin(math.radians(p+d))*math.sin(math.radians(p-b-l)))/(math.cos(math.radians(a-b))*math.cos(math.radians(d+a+l))),0.5))),2)
    ca2 = (1-av)*(pow(math.cos(math.radians(p-a-l)),2)/((math.cos(math.radians(l))*(pow(math.cos(math.radians(a)),2))*math.cos(math.radians(d+a+l)))))*pow((1/(1+pow((math.sin(math.radians(p+d))*math.sin(math.radians(p-b-l)))/(math.cos(math.radians(a-b))*math.cos(math.radians(d+a+l))),0.5))),2)
    return round(max(ca1,ca2),5)
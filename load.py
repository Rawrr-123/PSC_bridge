class Load:

    def __init__(self, name, pos, wheel_load, width):
        """

        Args:
            pos (list): successive position of wheels (and finally tail) starting from nose
            wheel_load (list): load at successive wheels
        """
        self.name = name
        self.pos = pos
        self.wheel_load = wheel_load
        self.width = width

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
    def weight(self):
        return sum(self.wheel_load)

    @property
    def loadpair(self):
        """

        Returns:zip with load and position w.r.to front wheel at 0

        """
        wheel_pos = [0]
        for index, pos in enumerate(self.pos[1:-1]):
            wheel_pos.append(wheel_pos[index]+pos)
        return zip(wheel_pos, self.wheel_load)


ll_70R = Load('Class 70RW', [0.61, 3.960, 1.520, 2.130, 1.370, 3.050, 1.370, 0.91], [80, 120, 120, 170, 170, 170, 170], 2790)
ll_70RT = Load('Class 70RT', [0.0, 0.653, 0.653, 0.653, 0.652, 0.653, 0.653, 0.653, 0.0], [50, 100, 100, 100, 100, 100, 100, 50], 2900)
ll_A = Load('Class A', [0.6, 1.1, 3.2, 1.2, 4.3, 3, 3, 3, 0.6], [27, 27, 114, 114, 68, 68, 68, 68, 27, 27], 2300)

print(ll_A.weight, ll_70R.weight, ll_70RT.weight)
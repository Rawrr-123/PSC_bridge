class Load:

    def __init__(self, pos, wheel_load):
        """

        Args:
            pos (list): successive position of wheels (and finally tail) starting from nose
            wheel_load (list): load at successive wheels
        """
        self.pos = pos
        self.wheel_load = wheel_load

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
    def loadpair(self):
        """

        Returns:zip with load and position w.r.to front wheel at 0

        """
        wheel_pos = [0]
        for index, pos in enumerate(self.pos[1:-1]):
            wheel_pos.append(wheel_pos[index]+pos)
        return zip(wheel_pos, self.wheel_load)


ll_70R = Load([0.61, 3.960, 1.520, 2.130, 1.370, 3.050, 1.370, 0.91], [80, 120, 120, 170, 170, 170, 170])
ll_70RT = Load([0.0, 0.653, 0.653, 0.653, 0.652, 0.653, 0.653, 0.653, 0.0], [50, 100, 100, 100, 100, 100, 100, 50])
ll_A = Load([0.6, 1.1, 3.2, 1.2, 4.3, 3, 3, 3, 0.6], [27, 27, 114, 114, 68, 68, 68, 68, 27, 27])

list(ll_70R.loadpair)

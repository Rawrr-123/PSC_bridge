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


ll_70R = Load([0.91, 1.370, 3.05, 1.37, 2.130, 1.520, 3.960, 0.61], [17, 17, 17, 17, 12, 12, 8])

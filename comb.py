def lane_number(CW_width):
    """
    returns number of lanes for given width.

    Args:
        CW_width: carriageway width in meters

    """
    if 13.1 < CW_width < 16.6:
        return 4
    elif 9.6 < CW_width < 13.1:
        return 3
    elif 5.3 < CW_width < 9.6:
        return 2
    elif 4.25 < CW_width < 5.3:
        return 1
    else:
        return 0


def comb(lane=None, width=None):
    """
    takes lane number as default input. you can specify CW width instead of lane by passing 'width = <width>'.
    For example: comb(width=15) is equivalent to comb(lane_number(15)).

    Args:
        lane (int): no. of lanes
        width (float): carriageway width in metres

    Returns:
        list of possible combinations, each in format [<no. of ClassA>, <no. of Class70RW>, <no. of Class 70RT>

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


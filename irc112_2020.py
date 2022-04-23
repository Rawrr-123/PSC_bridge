
def stress(ec2, fck):
    """
    stress strain relationship. refer to IRC: 112-2020 Cl. 6.4.2.8
    :param ec2: strain
    :param fck: fck of concrete
    :return: stress for giver strain ec2 for concrete of grade fck
    """
    if ec2 < 0:
        stress = 0
    elif 0 <= ec2 <= 0.002:
        stress = 0.67*fck/1.5 * (1 - np.power((1 - ec2 / 0.002), 2))
    else:
        stress = 0.67*fck/1.5
    return stress


def stress(ec2, fck):
    """
    stress strain relationship. refer to IRC: 112-2020 Cl. 6.4.2.8
    :param ec2: strain
    :param fck: fck of concrete
    :return: stress for giver strain ec2 for concrete of grade fck
    """
    if ec2 < 0:
        stress = 0
    elif 0 <= ec2 <= 0.002:
        stress = 0.67 * fck / 1.5 * (1 - np.power((1 - ec2 / 0.002), 2))
    else:
        stress = 0.67 * fck / 1.5
    return stress


def ebot(etop):
    """
    strain on bottom such that strain at 3/7h from top is ec2 0.002
    :param etop: strain on top
    :return: strain at bottom
    """
    ebot = 4 / 3 * (0.0035 - etop)
    return ebot


def interpolate_e(etop, ebot, depth, y):
    """
    interpolate strain at certain depth from bottom
    :param etop: strain at top
    :param ebot: strain at bottom
    :param y: distance at which e is required (from bottom)
    :param d: depth of section
    :return: strain
    """

    e = etop + (ebot - etop) / depth * (depth - y)
    return e


def na(etop, ebot, depth):
    """
    interpolate neutral axis
    :param etop: strain at top
    :param ebot: strain at bottom
    :param depth: depth of section
    :return: depth of neutral axis from bottom
    """
    na = depth / (ecu2 - ebot) * -ebot
    return na


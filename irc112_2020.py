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


def eff_span(type, span, bea, d, sup):
    """

    Args:
        type: Type of the member (Simply supported, framing into supporting, continuous )
        span: Total length of span
        bea: Width of bearing
        d: Effective depth of beam
        sup: Width of supporting members
    Returns: Effective span of the beam
    """
    if type == 'simply_supported':
        return min(span + bea, span + d)
    elif type == 'framing_into_supporting':
        return (span + sup)
    elif type == 'continuous':
        return (span + sup)


def K(d):
    """
    A parameter used during shear check and design.
    Args:
        d: Effective depth in mm.

    Returns: K

    """
    return (1 + pow((200 / d), 0.5)) if (1 + pow((200 / d), 0.5)) <= 2 else 2


def row_1(as1, bw, d):
    """
    Percentage of tensile reinforcement.
    Args:
        as1: Area of tensile reinforcement in mm^2.
        bw: Width of web in mm.
        d: Effective depth in mm.

    Returns: Percentage of tensile reinforcement.
    """
    return as1 / (bw * d) if as1 / (bw * d) <= 0.02 else 0.02


def check_1(V, K, row_1, fck, bw, d):
    """
    Checks whether the applied shear force is within limits of the shear strength of the structure.
    Args:
        V: Applied shear force in N.
        K: Parameter calculated from above.
        row_1: Percentage of tensile reinforcement.
        fck: Characteristics strength of concrete.
        bw: Effective width in mm.
        d: Effective width in mm.

    Returns: True if check is passed and false if not.

    """
    Vrdc = pow((0.12 * K * (80row_1 * fck)), 0.33) * bw * d
    if Vrdc >= V:
        return True
    else:
        return False


def stress_check(type, fck, fy, comp, tens):
    """
    Checks for permissible stress under serviceability limit state criteria.
    Args:
        type: type of load combination. (rare for Rare and quasi for Quasi-permanent)
        fck: Characteristics strength of concrete in N/mm^2.
        fy: Yield strength of steel in N/mm^2.
        comp: Compressive stress in N/mm^2
        tens: Tensile stress in N/mm^2.

    Returns: True if stress within limit else False.

    """
    if type == 'rare':
        if comp <= 0.8fck and tens <= 0.8fy:
            return True
        else:
            return False
    if type == 'quasi':
        if comp <= 0.36 * (fck + 10)
            return True
        else:
            return False


def row_eff(x, d, h, bw, As)
    """

    Args:
        x: Neutral axis depth in mm. 
        d: Effective depth in mm.
        h: Total height/depth of the section in mm.
        As: Area of tensile reinforcement in mm^2.

    Returns:
    Effective percentage of reinforcement.
    """
    heff = min(2.5 * (h - d), (h - x) / 3, h / 2)
    return As / (heff * bw)


def k1k2(type, loading):
    """
    Parameters depending on type of reinforcements and loading.
    Args:
        type: deformed or plain for deformed bars and effectively plain bars
        loading: bending for pure bending and torsion for pure torsion

    Returns:
        a list of constants k1 and k2.

    """
    k = []
    if type == 'deformed' and loading = 'bending':
        k.append(0.8)
        k.append(0.5)
    elif type == 'deformed' and loading = 'torsion':
        k.append(0.8)
        k.append(1)
    elif type == 'plain' and loading = 'bending':
        k.append(1.6)
        k.append(0.5)
    elif type == 'plain' and loading = 'torsion':
        k.append(1.6)
        k.append(1)


def sr_max(dia, c, s, type, loading, x, d, h, bw, s)
    """
    Maximum crack spacing.
    Args:
        dia: Diameter of the reinforcement bar used in mm.
        c: Effective cover in mm.
        s: Spacing of reinforcements in mm.
        type: Type of bar either deformed or plain.
        loading: Type of loading either bending or torsion.

    Returns: Maximum crack spacing in mm.

    """
    if s <= 5 * (c + dia / 2):
        return 3.4 * c + (0.425 * k1k2(type, loading)[0] * k1k2(type, loading)[1] * dia) / row_eff(x, d, h, bw, s)
    elif s >= 5 * (c + dia / 2):
        return 1.3 * (d - x)


def crack_width(dia, c, s, type, loading, sigma, fcte, Es, Ecm, kt=0.5, x, d, h, bw, As):
    """
    Calculation of crack width.
    Args:
        sigma: Stress in tension reinforcement assuming cracked section in Mpa.
        fcte: Mean effective compressive stress of concrete in MPa.
        Es: Elasticity of steel in MPa.
        Ecm: Elasticity of concrete in Mpa.

    Returns: Crack width in mm.

    """
    alp = Es / Ecm
    if (sigma - kt * fcte / row_eff(x, d, h, bw, As) * (1 + alp * row_eff(x, d, h, bw, As))) / Es >= 0.6*sigma/Es
        diff_e = (sigma - kt * fcte / row_eff(x, d, h, bw, As) * (1 + alp * row_eff(x, d, h, bw, As))) / Es
    else::
        diff_e = 0.6*sigma/Es
    return sr_max(dia, c, s, type, loading) * diff_e




    """
    Member stiffness matrix
    Args:
        a: Area
        e: Modulus of elasticity kN/m**2
        i: Moment of Inertia about Z axis m**4
        l: length of member m

    Returns:
        numpy array of member stiffness matrix

    """
    a = a*e/l
    b = 6*e*i/l**2
    c = 12*e*i/l**3
    d = 4*e*i/l
    k = np.array([
        [a, 0, 0, -a, 0, 0],
        [0, c, b, 0, -c, b],
        [0, b, d, 0, -b, d/2],
        [-a, 0, 0, a, 0, 0],
        [0, -c, -b, 0, c, -b],
        [0, b, d/2, 0, -b, d]
    ])
    return k
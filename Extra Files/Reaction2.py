def find_rb(s, u, b=0):
    if 0 < u < s:
        rb = u / (s - b / 2)
    elif round(u, 2) == s:
        rb = (u / (s - b / 2)) / 2
    else:
        rb = 0

    return rb


def find_ra(s, u, b=0):
    if u < s:
        ra = 0
    elif round(u, 2) == s:
        ra = (2 * s - u) / (s - b / 2) / 2

    elif s < u <= 2 * s:
        ra = (2 * s - u) / (s - b / 2)
    else:
        ra = 0

    return ra

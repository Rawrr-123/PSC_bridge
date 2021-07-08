def find_rb(s, u, b=0):
    if 0 < u < s + b / 2:
        rb = u / s
    elif u == s + b / 2:
        rb = 0.5 * u / s
    else:
        rb = 0

    return rb


def find_ra(s, u, b=0):
    if u < s + b / 2:
        ra = 0
    elif u == s + b / 2:
        ra = 0.5 * (2 * s + b - u) / s

    elif s < u <= 2 * s:
        ra = (2 * s + b - u) / s
    else:
        ra = 0

    return ra

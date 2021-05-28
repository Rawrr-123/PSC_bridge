import matplotlib.pyplot as plt
plt.style.use('seaborn')


def FindBM(s, u, b):
    """
    returns bending moment at x=b due to unit load at x=u on a span of length s
            Parameters:
                        s = span length
                        u = position of unit load (from left end)
                        b = location at which bending moment is required (from left end)
            Returns:
                        bm = beding moment
    """
    if u < 0 or u > s:
        bm = 0
    elif 0 <= u < s:
        bm = u/s*(s-b)
    else:
        bm = (s-u)/s*b
 
    return(bm)


def FindSF(s, u, b):
    """
    returns shear force at x=b due to unit load at x=u on a span of length s
            Parameters:
                        s = span length
                        u = position of unit load (from left end)
                        b = location at which shear force is required (from left end)
            Returns:
                        sf = shear force
    """
    if u < 0 or u > s:
        sf = 0
    elif 0 <= u < b:
        sf = -u/s
    else:
        sf = (s-u)/s
    return(sf)


def il(span, at, of='bm', detail=25):
    """
    function for ild on a specific point
            Parameters:
                        span = Span length
                        at = point at which influence line is to be calculated
                        of = 'bm' bending moment(default) or 'sf' shear force
                        detail = number of il points
            Returns:
                        il(dict) = ild coordinates in the form of a dictionary {'x': [], 'y': []}
    """

    il = {'x': [], 'y': []}
    if(of == 'bm'):
        for i in range(detail+1):
            bm = FindBM(span, span/detail*i, at)
            il['x'].append(span/detail*i)
            il['y'].append(bm)
    if(of == 'sf'):
        for i in range(detail+1):
            sf = FindSF(span, span/detail*i, at)
            il['x'].append(span/detail*i)
            il['y'].append(sf)
    return(il)


#plotting ild of sf

ild = il(of='sf', at=20, span=50, detail=500)
plt.plot(ild['x'], ild['y'])
plt.axhline(y=max(ild["y"]), color='grey', lw=0.5, label=f'max = {max(ild["y"])}')
plt.axhline(y=min(ild["y"]), color='grey', lw=0.5, label=f'min = {round(min(ild["y"]), 2)}')
plt.legend()
plt.tight_layout()
plt.show()

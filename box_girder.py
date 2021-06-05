import pandas as pd


def find_bm(s, u, b):
    if u < 0 or u > s:
        b = 0
    elif 0 <= u < b:
        b = u / s * (s - b)
    else:
        b = (s - u) / s * b

    return b


def find_sf(s, u, b):
    if u < 0 or u > s:
        sh = 0
    elif 0 <= u < b:
        sh = -u / s
    else:
        sh = (s - u) / s
    return sh


# defining load

ll_70R = [(0, 80), (3.96, 120), (5.48, 120), (7.61, 170), (8.98, 170), (12.03, 170), (13.40, 170)]
ll_70RT = [(0, 50), (0.653, 100), (1.306, 100), (1.959, 100), (2.611, 100), (3.264, 100), (3.917, 100), (4.57, 50)]
ll_A = [(0, 27), (1.1, 27), (4.3, 114), (5.5, 114), (9.8, 68), (12.8, 68), (15.8, 68), (18.8, 68)]

loads = [ll_A, ll_70R, ll_70RT]

span = 50
maxBMs = []
maxSFs_plus = []
maxSFs_minus = []
for i in range(len(loads)):
    maxBM = []
    maxSF_plus = []
    maxSF_minus = []
    for j in range(9):
        at = span / 8 * j
        first_wheel_at = 0
        step = 0.1

        BM = find_bm(span, 0, at)
        SF_plus = find_sf(span, 0, at)
        SF_minus = find_sf(span, 0, at)

        for k in range(int((span + loads[i][-1][0]) / step) + 2):  # '+2' to make sure the load moves all the way to
            # end until it has no effect
            bm = 0
            sf = 0
            for this in loads[i]:
                a, load = this
                pos = -a + first_wheel_at
                bm = bm + find_bm(span, pos, at) * load
                sf = sf + find_sf(span, pos, at) * load
            first_wheel_at += step
            BM = bm if bm > BM else BM
            SF_plus = sf if sf > SF_plus else SF_plus
            SF_minus = sf if sf < SF_minus else SF_minus
        maxBM.append(round(BM, 3))
        maxSF_plus.append(round(SF_plus, 3))
        maxSF_minus.append(round(SF_minus, 3))
    maxBMs.append(maxBM)
    maxSFs_plus.append(maxSF_plus)
    maxSFs_minus.append(maxSF_minus)

# print(f'Max Bending moments \n {maxBMs}')
# print(f'Max positive Shear Forces \n {maxSFs_plus}')
# print(f'Max negative Shear Forces \n {maxSFs_minus}')

A = ['ClassA', 'Class70RW', 'Class70RT']
B = ['MaxBM', 'MaxSF+', 'MaxSF-']
C = []
for i in range(len(loads)):
    for j in [maxBMs, maxSFs_plus, maxSFs_minus]:
        C.append(j[i])

iterables = [A, B]
index = pd.MultiIndex.from_product(iterables)
df = pd.DataFrame(C, index=index, columns=[span / 8 * i for i in range(9)])
# print(df.loc['ClassA', 'MaxSF-'])   ## you can navigate using loc, iloc
df.to_excel('outputs/loads.xlsx')

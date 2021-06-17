import matplotlib.pyplot as plt
plt.style.use('seaborn')
plt.interactive(0)

def impact(loading, span, material='RCC'):
    """

    Args:
        loading (str): options => 'classA', 'classAA', '70R', '70RT'
        span (float): span length in metres
        material (str): options => 'RCC' (default), 'steel'

    Returns:
        impact factor value (float)

    """
    if loading == 'Class A' or loading == 'Class B':
        if material == 'RCC':
            if span <= 3:
                return 0.5
            elif 3 < span < 45:
                return 4.5 / (6 + span)
            else:
                return 0.088
        if material == 'steel':
            if span <= 3:
                return 0.545
            elif 3 < span < 45:
                return 9 / (13.5 + span)
            else:
                return 0.154
    if loading == 'Class AA' or loading == 'Class 70RW' or loading == 'Class 70RT':
        if span < 9:
            if loading == 'Class 70RT':
                if span <= 5:
                    return 0.25
                else:
                    return .25 + ((.1 - .25) / (9 - 5)) * (span - 5)
            else:
                return .25
        else:
            if material == 'RCC':
                if loading == 'Class 70RT':
                    if span <= 40:
                        return 0.1
                    else:
                        return impact('Class A', span, 'RCC')
                else:
                    if span < 12:
                        return 0.25
                    else:
                        return impact('Class A', span, 'RCC')
            if material == 'steel':
                if loading == 'Class 70RT':
                    return 0.1
                else:
                    if span < 23:
                        return 0.25
                    else:
                        return impact('Class A', span, 'steel')


x = [i*0.5 for i in range(int(50 / 0.5))]
ll_A_RCC = [impact('ClassA', i * 0.5) for i in range(int(50 / 0.5))]
ll_70R_RCC = [impact('Class 70RW', i * 0.5) for i in range(int(50 / 0.5))]
ll_70RT_RCC = [impact('Class 70RT', i * 0.5) for i in range(int(50 / 0.5))]

# ll_A_steel = [impact('classA', i * 0.5, 'steel') for i in range(int(50 / 0.5))]
# ll_70R_steel = [impact('70R', i * 0.5, 'steel') for i in range(int(50 / 0.5))]
# ll_70RT_steel = [impact('70RT', i * 0.5, 'steel') for i in range(int(50 / 0.5))]

plt.figure(figsize=(9, 6))

plt.plot(x, ll_A_RCC, label="Class A RCC")
plt.plot(x, ll_70R_RCC, label="Class 70R RCC")
plt.plot(x, ll_70RT_RCC, label="Class 70RT RCC")

# plt.plot(x, ll_A_steel, label="class A steel")
# plt.plot(x, ll_70R_steel, label="70R steel")
# plt.plot(x, ll_70RT_steel, label="70RT steel")

plt.xlabel('Span m')
plt.ylabel('IF')
plt.title('Impact factor')
plt.legend()

plt.tight_layout()
# plt.show()  # uncomment to display the plot or navigate to outputs folder for impact_factor.png
plt.savefig('outputs/impact_factor.png')

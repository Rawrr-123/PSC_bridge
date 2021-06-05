import matplotlib.pyplot as plt


def impact(loading, span, material='RCC', vehicle='wheeled'):
    if loading == 'class A' or loading == 'class B':
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
    if loading == 'class AA' or loading == '70R':
        if span < 9:
            if vehicle == 'tracked':
                return .25 + ((.1 - .25) / (9 - 5)) * (span - 5)
            elif vehicle == 'wheeled':
                return .25
        else:
            if material == 'RCC':
                if vehicle == 'tracked':
                    if span <= 40:
                        return 0.1
                    else:
                        return impact('class A', span, 'RCC')
                if vehicle == 'wheeled':
                    if span < 12:
                        return 0.25
                    else:
                        return impact('class A', span, 'RCC')
            if material == 'steel':
                if vehicle == 'tracked':
                    return 0.1
                if vehicle == 'wheeled':
                    if span < 23:
                        return 0.25
                    else:
                        return impact('class A', span, 'steel')


x = [i for i in range(int(50 / 0.5))]
ll_A = [impact('class A', i * 0.5) for i in range(int(50 / 0.5))]
ll_70R = [impact('70R', i * 0.5) for i in range(int(50 / 0.5))]
ll_70RT = [impact('70R', i * 0.5, vehicle='tracked') for i in range(int(50 / 0.5))]
plt.plot(x, ll_A, label="class A")
plt.plot(x, ll_70R, label="70R")
plt.plot(x, ll_70RT, label="70RT")
plt.legend()
plt.show()  # uncomment to display the plot or navigate to outputs folder for impact_factor.png
plt.savefig('outputs/impact_factor.png')

from carriageway import Carriageway, Combination, Arrangement
import pandas as pd

carriageway = Carriageway(width=15)
combinations = carriageway.combinations()
list_combinations = []
list_max_e = []
for i in combinations:
    list_combinations.append([i.classA, i.class70Rw, i.class70Rt])
    arrangements = i.arrangements()
    list_arrangements = []
    eccentricity = []
    max_e = 0
    for k in arrangements:
        list_arrangements.append(k.veh)
        eccentricity.append(k.eccentricity())
        print(i, k, eccentricity)
        max_e = k.eccentricity() if k.eccentricity() > max_e else max_e
    list_max_e.append(max_e)

df = pd.DataFrame(list_combinations, columns=['ClassA', 'Class70Rw', 'Class70Rt'], index=[f'comb{i+1}' for i in range(len(list_combinations))])
df['MaxEccentricity'] = list_max_e
print(df)


# arr = Arrangement(('a', 'a', 'a', 'a'), 1500).plot_signal()
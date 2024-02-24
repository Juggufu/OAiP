# 2
def future(*mass, **const):
    CountConst = 1
    for key, value in const.items():
        CountConst *= float(value)
    sum_of_masses = sum(mass) * CountConst
    if sum_of_masses > VIN:
        return 'ACCELERATION'
    elif sum_of_masses < VIN:
        return 'DECELERATION'
    return 'UNCHANGED'


VIN = 3
mass = [1, 2, 3, 4]
const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
print(future(*mass, **const))
# 3
from math import ceil


def circuit_resistance(*resistors, connection='serial'):
    if connection == 'serial':
        return sum(resistors)
    elif connection == 'parallel':
        s = sum(map(lambda x: 1 / x, resistors))
        return 1 / s
    else:
        raise ValueError("Bad connection type")


data = [30, 30, 30]
print(circuit_resistance(*data, connection='parallel'))


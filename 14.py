# 1
def groundhog_day(a):
    for i, (prev, curr) in enumerate(zip(a, a[1:]), 1):
        res = [i for i, (x, y) in enumerate(zip(prev, curr)) if x != y]
        if len(res) > 2:
            return (i,) + tuple(res)
    return (0, 0)


data = ["Groundhog Festival in Punxsutawney.",
        "Groundhog Festival in Punksutawney.",
        "Groundhog Festivel in Punxsutowney."]
print(groundhog_day(data))
# 2
def gears(rack: list, n: int, m: int):
    a = {}
    b = {}
    for box in rack:
        for gear in box:
            if gear > 0:
                if gear % n == 0:
                    rn = gear // n
                    if rn not in a:
                        if rn in b:
                            return (gear, b[rn])
                        a[rn] = gear
                if gear % m == 0:
                    rm = gear // m
                    if rm not in b:
                        if rm in a:
                            return (a[rm], gear)
                        b[rm] = gear
    return (None, None)


data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
print(gears(data, 30, 7))
# 3
from collections import deque


def brackets2(line):
    inv = {']': '[', ')': '(', '}': '{'}
    st = deque()
    for i in line:
        if i in '[({':
            st.append(i)
        if i in '])}':
            if len(st):
                i = inv[i]
                if i != st.pop():
                    return False
            else:
                return False
    if len(st):
        return False
    return True


line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
print(brackets2(line))
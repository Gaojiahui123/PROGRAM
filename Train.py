import numpy as np

a = [1,2]
a0 = []
l = [0]
a0.append(a[-1] - a[-2])
l.append(a0[-1] * 0.5 * 0.1 ** 2 + l[-1] * 0.1)
print(l)
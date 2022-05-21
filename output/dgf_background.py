import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/kunhao/Dropbox/code/CLASS/class_gsf_ede/output/dgf_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['dgf_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['w_gsf']
tex_names = ['(8\\pi G/3)w_gsf']
x_axis = 'z'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 17])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()
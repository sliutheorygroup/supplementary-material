import numpy as np
import matplotlib.pylab as plt
import group_plotconfig as gp

gp.set_mode('sc')

width_single_column = 4.0
height_single_column  = width_single_column * 0.618 

plt.rcParams.update({'lines.linewidth': 1.0, 'lines.markersize':6,
                     'figure.figsize' : (width_single_column, height_single_column)})


data = np.loadtxt("input.dat")
kpt = np.loadtxt("qpoints")
kpt_labels = [r"$\Gamma$", 'K', 'M', r"$\Gamma$", 'A', 'L', 'H', 'A']

nks, nbands = data.shape
print(nks, nbands)


x= data[:,0]

nkpt = kpt.shape[0]
xkpt = []

xkpt.append(0.0)
count = 0
for j in range(0, nkpt-1):
    count += int(kpt[j,3])
    xkpt.append(x[count])

print(xkpt)


fig, ax = plt.subplots()

for i in range(1,nbands):
    ax.plot(data[:,0], data[:,i], '-k')

#qpts = [0.000000000000000E+00, 0.541101690048164E+00, 0.108220338009633E+01, 1.653229]
ymin=-100
ymax=700

for xi in xkpt:
    ax.vlines(xi, ymin, ymax, colors='blue')

ax.hlines(0.0, x[0], x[-1], colors='blue', linestyle='dashed')
ax.set_xlim([0,x[-1]])
ax.set_ylim([ymin, ymax])
ax.set_xticks(xkpt)
ax.set_xticklabels(kpt_labels,fontsize=10)
ax.set_ylabel(r'Frequency (cm$^{-1}$)')
fig.tight_layout(pad=0.2)
fig.savefig('bands.png')
fig.savefig('bands.eps')
plt.show()


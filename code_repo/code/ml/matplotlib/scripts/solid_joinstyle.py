from pylab import *

size = 256, 16
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)
axes([0, 0, 1, 1], frameon=False)

plot(np.arange(3), [0, 1, 0], color="blue", linewidth=8, solid_joinstyle='miter')
plot(4 + np.arange(3), [0, 1, 0], color="blue", linewidth=8, solid_joinstyle='bevel')
plot(8 + np.arange(3), [0, 1, 0], color="blue", linewidth=8, solid_joinstyle='round')

xlim(0, 12), ylim(-1, 2)
xticks([]), yticks([])

savefig('../figures/solid_joinstyle.png', dpi=dpi)
# show()

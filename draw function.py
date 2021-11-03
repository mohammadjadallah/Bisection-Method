from matplotlib.pyplot import *
from numpy import *
from scipy.optimize import fsolve

#(5 * x ** 3) - (5 * x ** 2) + 6 * x - 2

def f(x):
    return (5 * x ** 3) - (5 * x ** 2) + 6 * x - 2

x = linspace(0, 5)
y = f(x)

res = fsolve(f, 5)

fig = figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')

plot(x, y, 'r', linestyle=':')
plot(res[0], f(res[0]), 'ko')
show()

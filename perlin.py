import matplotlib.pyplot as plt
import numpy as np

from perlin_noise import PerlinNoise


npoints = 300
nlines = 20

for line in range(nlines):
    noise = PerlinNoise(octaves=(line+1)*1.2, seed=line)
    data = [(noise([i/npoints])) for i in range(npoints)]
    data = np.array(data)
    data = data*0.1*line + line
    plt.plot(data, color="k")

plt.axis('off')
plt.savefig("perlin.svg")
# plt.show()

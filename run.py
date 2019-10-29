from Grid import Grid
import matplotlib.pyplot as plt


gr = Grid()

for i in range(100):
    gr.advance_time()

plt.plot(gr.creaturePopulation)
plt.show()
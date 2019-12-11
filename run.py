from Grid import Grid
import matplotlib.pyplot as plt
import numpy as np
import settings

# gr = [None] * 5
# graphData = {
#     'x': range(101),
# }
#
# n = 0
# for g in gr:
#     g = Grid()
#     for i in range(100):
#         print("running max_food = %d generation = %d" % (g.max_food, i))
#         g.advance_time()
#     settings.MAXIMUM_FOOD += 2
#     graphData['y%d'%n] = g.creaturePopulation
#     plt.plot('x', 'y%d'%n, data=graphData, label="Maximum food = %d" % g.max_food)
#     n += 1
# # plt.plot(gr.creaturePopulation)
# plt.ylabel("Number of Creatures")
# plt.xlabel("Generation")
# plt.title("Number of creatures over time, sharing food %s" % settings.SHARE_FOOD)
# plt.legend()
# plt.show()
# settings.MAXIMUM_FOOD = 3
# settings.SEXUAL_REPRODUCTION = True
# settings.MAXIMUM_BABIES = 3
#
#
# gr = [None] * 5
# graphData = {
#     'x': range(501),
# }
#
# n = 0
# for g in gr:
#     g = Grid()
#     for i in range(500):
#         print("running no sharing, min_age = %d generation = %d" % (g.min_age, i))
#         g.advance_time()
#     settings.NON_SEXUAL_AGE_MIN -= 1
#     graphData['y%d'%n] = g.creaturePopulation
#     plt.plot('x', 'y%d'%n, data=graphData, label="Minimum Reproduction age = %d" % g.min_age)
#     n += 1
# # plt.plot(gr.creaturePopulation)
# plt.ylabel("Number of Creatures")
# plt.xlabel("Generation")
# plt.title("Number of creatures over time, sharing food %s" % settings.SHARE_FOOD)
# plt.legend()
# plt.show()
#
settings.MAXIMUM_FOOD = 3
settings.SEXUAL_REPRODUCTION = True
settings.MAXIMUM_BABIES = 10
settings.SHARE_FOOD = False
settings.NON_SEXUAL_AGE_MIN = 10


gr = [None] * 2
graphData = {
    'x': range(101),
}

n = 0
for g in gr:
    g = Grid()
    for i in range(100):
        print("running not sharing, sex_rep = %s generation = %d" % (g.sex_rep, i))
        g.advance_time()
    settings.SEXUAL_REPRODUCTION = False
    graphData['y%d'%n] = g.creaturePopulation
    plt.plot('x', 'y%d'%n, data=graphData, label="Not Sharing, Sexual Reproduction = %s" % g.sex_rep)
    n += 1
n = 2
settings.SHARE_FOOD = True
settings.SEXUAL_REPRODUCTION = True
for g in gr:
    g = Grid()
    for i in range(100):
        print("running sharing, sex_rep = %s generation = %d" % (g.sex_rep, i))
        g.advance_time()
    settings.SEXUAL_REPRODUCTION = False
    graphData['y%d'%n] = g.creaturePopulation
    plt.plot('x', 'y%d'%n, data=graphData, label="Sharing, Sexual Reproduction = %s" % g.sex_rep)
    n += 1
# plt.plot(gr.creaturePopulation)
plt.ylabel("Number of Creatures")
plt.xlabel("Generation")
plt.title("Number of creatures over time, sharing food %s" % settings.SHARE_FOOD)
plt.legend()
plt.show()

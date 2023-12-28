import numpy as np

def f(n,m):
    population = np.zeros([n+1,m], dtype=np.int64)
    # print(population)
    population[1][0] = 1
    # print(population.shape)

    for month in range(2,population.shape[0]):
        for age in range(0,population.shape[1]):
            if age == 0:
                population[month][age] = np.sum(population[month-1,1:])
            else:
                population[month][age] = population[month-1][age-1]
    print(population)
    return np.sum(population[n])

n = 4
m = 3
print(f(n,m))
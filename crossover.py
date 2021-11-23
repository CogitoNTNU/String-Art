import numpy as np
import random

# Jon’s code 

def initialize_population(num_individuals: int, lines: int, pins: int):
    population = np.random.randint(0, pins, size = (num_individuals,lines + 1))
    for i in range(num_individuals):
        for j in range(lines + 1):
            while population[i][j] == population[i][j-1]:
                population[i][j] = random.randrange(pins)
    return population

# Inès’ code

n = 20 # Number of individuals 
l = 8 # Number of lines
p = 9 # Number of pins

pop = initialize_population(n, l, p) # Initialize population 

print("List of parents: ")

print(" ")

print(pop)

print(" ")

pop2 = np.zeros([n, p]) # New population
chi = np.zeros([2*n, p]) # Parents
par = np.zeros([2, p]) # Children 

index = random.randint(0, (len(pop[0]) - 1)) # Index for swapping

# Crossover
for i in range(0, len(pop), 2):
    m = random.randint(0, (len(pop) - 1)) # Extract random population index
    r = pop[m]  # Extract random parent 1
    par[0] = r # Put it in array of parents to cross
    pop2[0 + i] = par[0] # Put it in new population array
    pop = np.delete(pop, m, 0) # Erase from population array, so that same parent is not used twice
    m2 = random.randint(0, (len(pop) - 1)) # Extract random population index
    r2 = pop[m2] # Extract random parent 2
    par[1] = r2 # Put it in array of parents to cross
    pop2[1 + i] = par[1] # Put it in new population array
    pop = np.delete(pop, m2, 0) # Erase from population array, so that same parent is not used twice
    chi[0 + i] = np.concatenate((par[0][:index], par[1][index:])) # Crossover, swap after index
    chi[1 + i] = np.concatenate((par[1][:index], par[0][index:])) # Crossover, swap after index

print("List of children before mutation: ")

print(" ")

print(chi[:20])

print(" ")

n = random.randint(0, (len(chi[0]) - 1)) # Extract random index of children array
n2 = random.randint(0, (len(chi[0]) - 1)) # Extract random index of children array

# Mutate children
for i2 in range(len(chi)):
    # Swap values of indexes
    o = chi[i2][n]
    chi[i2][n] = chi[i2][n2]
    chi[i2][n2] = o

print("List of children after mutation: ")

print(" ")

print(chi[:20])

print(" ")
    
# Add children to new population array
for j in range(len(pop2)):
    chi[len(pop2) + j] = pop2[j]

print("List of parents already used: ")

print(" ")

print(pop2)

print(" ")

print("List of children: ")

print(" ")

print(chi)

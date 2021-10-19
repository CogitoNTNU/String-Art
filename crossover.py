import random

population = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]] #List of parents
population2 = [] #List of parents already used
parents_to_cross = [] #List for crossover function
children = [] #List of children

ind = random.randint(0, (len(population[0]) - 1)) #I do not know where to put this

#Function for crossover
#Creating two new children by swapping parents from randomly selected index
def crossover(a, b, index):
    child1 = a[:index] + b[index:]
    child2 = b[:index] + a[index:]
    children.append(child1) #Append child to list
    children.append(child2) #Append child to list

#Main function
def main(population): #“Population” is a list of all the parents, which are lists of points
    #Draw two candidates from the population randomly
    for i in range(int(len(population)/2)):
        for j in range (2):
            r_parent = random.choice(population) #Take random parent from population
            parents_to_cross.append(r_parent) #Append random parent to list
            population2.append(r_parent)
            population.remove(r_parent)
        crossover(parents_to_cross[0], parents_to_cross[1], ind) #Create two children
        parents_to_cross.clear() #Clear list
        
main(population)

print("List of parents: ", population)
print(" ")
print("List of parents already used: ", population2)
print(" ")
print("List for crossover function: ", parents_to_cross)
print(" ")
print("List of children: ", children)
print(" ")

population2.append(children)

print("New list of parents: ", population2)



    


    

import random

t = 0  
g = 0  

def calculate_fitness(individual):
    global t
    sum_val = individual[0] + individual[1]
    if sum_val > t:
        return 0
    else:
        return t - abs(t - sum_val)

def get_fittest_individuals(population):
    sorted_pop = sorted(population, key=calculate_fitness, reverse=True)
    return sorted_pop[0], sorted_pop[1]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual):
    global g
    mutation_point = random.randint(0, g - 1)
    individual[mutation_point] = random.randint(0, 9)
    return individual

def get_least_fittest_index(population):
    min_fitness = float('inf')
    min_index = 0
    for i in range(len(population)):
        fitness = calculate_fitness(population[i])
        if fitness < min_fitness:
            min_fitness = fitness
            min_index = i
    return min_index

def generate_random_population(size, gene_length):
    return [[random.randint(0, 9) for _ in range(gene_length)] for _ in range(size)]

def main():
    global t, g

    # Input
    t = int(input())
    g = int(input())

    population_size = 10
    population = generate_random_population(population_size, g)

    generation = 0

    fittest_individual = max(population, key=calculate_fitness)

    print(f"Generation: {generation} Fittest sum: {fittest_individual[0] + fittest_individual[1]}")

    # Loop until we get exact match
    while fittest_individual[0] + fittest_individual[1] != t:
        generation += 1

        parent1, parent2 = get_fittest_individuals(population)
        child1, child2 = crossover(parent1[:], parent2[:])
        child1 = mutate(child1)
        child2 = mutate(child2)

        fittest_child = child1 if calculate_fitness(child1) > calculate_fitness(child2) else child2

        least_idx = get_least_fittest_index(population)
        population[least_idx] = fittest_child

        fittest_individual = max(population, key=calculate_fitness)
        print(f"Generation: {generation} Fittest sum: {fittest_individual[0] + fittest_individual[1]}")

    # Output the result
    print(f"\nSolution found in generation {generation}")
    print(f"Sum of first two genes: {fittest_individual[0] + fittest_individual[1]}")
    print("Genes: ", *fittest_individual)

if __name__ == "__main__":
    main()

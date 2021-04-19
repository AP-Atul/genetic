from genetic import GeneticSolver, single_point, swap


def custom_fitness(gene):
    return max(gene)


solver = GeneticSolver(
    fitness_func=custom_fitness,  # pass custom function
    crossover_func=single_point,
    mutation_func=swap,
    pop_size=100,
    mut_prob=0.1,
    tourn_size=40,
    reverse=True  # to get the higher fitness as answer else False
)

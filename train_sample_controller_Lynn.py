from deap import base, creator
import random
from deap import tools
import time
import numpy as np

from asteroids.fuzzy_asteroids import TrainerEnvironment
from sample_controller_Lynn_12_13_for_GA import FuzzyController
from sample_score_Lynn import SampleScore


def evaluate(individual):
    # Run a single game
    score = game.run(controller=FuzzyController(individual), score=SampleScore())
    #frame_count = score.frame_count # how long is the player alive
    if score.asteroids_more_than_10 > 0:
        too_many_asteroids_penalty = score.asteroids_more_than_20 + score.asteroids_more_than_10
        if too_many_asteroids_penalty <= 100:
            too_many_asteroids_penalty = 120
    else:
        too_many_asteroids_penalty = 100

    asteroids_hit = score.asteroids_hit
    final_measure = asteroids_hit * (100/too_many_asteroids_penalty)
    return (final_measure),


def main(game, population_size, max_generations):
    pop = toolbox.population(n=population_size)
    CXPB, MUTPB, NGEN = 0.5, 0.4, max_generations

    # Evaluate the entire population
    fitnesses = map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print('Finished Initialization')
    track_best_fit = []
    for g in range(NGEN):
        tic = time.perf_counter()

        print("-- Generation %i --" % g)
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        # How long did this generation take
        toc = time.perf_counter()
        print(f"This generation took {toc - tic:0.4f} seconds")

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        track_best_fit.append(max(fits))
        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
    return pop


if __name__ == "__main__":
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    IND_SIZE = 54

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.random)
    toolbox.register("individual", tools.initRepeat, creator.Individual,
                     toolbox.attr_float, n=IND_SIZE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutUniformInt, low=0, up=1, indpb=0.1)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", evaluate)

    settings = {
        "lives": 1,
        "allow_key_presses": False
    }
    # To use the controller within the context of a training solution
    game = TrainerEnvironment(settings=settings)
    ga_run = main(game, 50, 200)
    print(ga_run)

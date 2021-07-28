from deap import base, creator
import random
from deap import tools
import time
import numpy as np

from asteroids.fuzzy_asteroids import TrainerEnvironment
from sample_controller_Lynn_12_13_for_GA import FuzzyController
from sample_score_Lynn import SampleScore


def evaluate(individual) -> tuple:
    # Run a single game
    score = game.run(controller=FuzzyController(individual), score=SampleScore())
    # how does the chromosome perform
    final_score = score.asteroids_hit
    # The comma after return is important when using DEAP
    return final_score,


def main(game, population_size, max_generations):

    # run the genetic algorithm loop - I used the DEAP examples online to make mine

    print('Finished Initialization')

    for g in range(NGEN):
        tic = time.perf_counter()

        print("-- Generation %i --" % g)

        # Track the results while runing to get a feeling of how training is going

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)
    return pop


if __name__ == "__main__":
    # Setup needed for DEAP algorithm

    settings = {
        "lives": 1,
        "allow_key_presses": False
    }
    # To use the controller within the context of a training solution
    game = TrainerEnvironment(settings=settings)

    ga_run = main(game, 50, 200)
    print(ga_run)

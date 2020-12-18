from typing import Tuple, Dict, Any

from sample_controller import FuzzyController
from asteroids.fuzzy_asteroids import FuzzyAsteroidGame, TrainerEnvironment

from contextlib import contextmanager
import multiprocessing


if __name__ == "__main__":
    # Available settings
    settings = {
        # "frequency": 60,
        # "lives": 3,
        # "prints": False,
    }

    # To use the controller within the context of a training solution
    # It is important to not create a new instance of the environment everytime
    game = TrainerEnvironment(settings=settings)

    for i in range(1000):
        # Call run() on an instance of the TrainerEnvironment
        # This function automatically manages cleanup
        score = game.run(controller=FuzzyController())

        print(f"Generation {i}: {str(score)}")

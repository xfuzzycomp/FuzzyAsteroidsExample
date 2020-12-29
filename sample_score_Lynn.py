import numpy as np

from asteroids.util import Score
from asteroids.game import AsteroidGame


class SampleScore(Score):
    """
    Sample of how to modify the Score class
    """
    def __init__(self):
        """
        Define constructor
        """
        self.number_asteroids = list()
        self.average_number_asteroids = 0
        self.asteroids_more_than_20 = 0
        self.asteroids_more_than_10 = 0

        # Constructor for this class should not miss call to parent class constructor
        super().__init__()

    def timestep_update(self, environment: AsteroidGame) -> None:
        """
        This function is called after the evaluation of each game time step

        :param environment: AsteroidGame environment instance
        """
        self.number_asteroids.append(len(environment.asteroid_list))

    def final_update(self, environment: AsteroidGame) -> None:
        """
        This function is called after the completion of the game

        :param environment: AsteroidGame environment instance
        """
        self.average_number_asteroids = sum(self.number_asteroids)/self.frame_count
        x = np.array(self.number_asteroids)
        max_asteroids = np.max(x)
        greater_than_20 = np.count_nonzero(x >= 20)
        greater_than_10 = np.count_nonzero(x >= 10)
        self.asteroids_more_than_20 = max_asteroids * greater_than_20
        self.asteroids_more_than_10 = .05 * max_asteroids * greater_than_10

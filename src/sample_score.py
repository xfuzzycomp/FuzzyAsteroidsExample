from fuzzy_asteroids.util import Score
from fuzzy_asteroids.game import AsteroidGame


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

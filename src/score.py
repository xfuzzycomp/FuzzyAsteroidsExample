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
        # TODO add your own attributes/properties to this claass

        # Constructor for this class should not miss call to parent class constructor
        super().__init__()

    def timestep_update(self, environment: AsteroidGame) -> None:
        """
        This function is called after the evaluation of each game time step

        :param environment: AsteroidGame environment instance
        """
        pass

    def final_update(self, environment: AsteroidGame) -> None:
        """
        This function is called after the completion of the game

        :param environment: AsteroidGame environment instance
        """
        pass

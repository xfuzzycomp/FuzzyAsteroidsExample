from typing import Tuple, Dict

from asteroids.fuzzy_controller import ControllerBase, SpaceShip
from asteroids.fuzzy_asteroids import FuzzyAsteroidGame


class FuzzyController(ControllerBase):
    """
    Class to be used by UC Fuzzy Challenge competitors to create a fuzzy logic controller
    for the Asteroid Smasher game.


    Note: Your fuzzy controller class can be called anything, but must inherit from the
    the ``ControllerBase`` class (imported above)

    Users must define the following:
    1. __init__()
    2. actions(self, ship: SpaceShip, input_data: Dict[str, Tuple])

    By defining these interfaces, this class will work correctly
    """
    def __init__(self):
        """
        Create your fuzzy logic controllers and other objects here
        """
        pass

    def actions(self, ship: SpaceShip, input_data: Dict[str, Tuple]) -> None:
        """
        Compute control actions of the ship. Perform all command actions via the ``ship``
        argument. This class acts as an intermediary between the controller and the environment.

        The environment looks for this function when calculating control actions for the Ship sprite.

        :param ship: Object to use when controlling the SpaceShip
        :param input_data: Input data which describes the current state of the environment
        """
        # ship.turn_rate = 180.0
        ship.thrust = ship.thrust_range[1]
        ship.shoot()


if __name__ == "__main__":
    # Available settings
    settings = {
        # "graphics_on": False,
        # "sound_on": True,
        # "frequency": 60,
        "real_time_multiplier": 2,
        # "lives": 3,
        # "prints": True,
        "allow_key_presses": False
    }

    """ Start the game """
    # Create a game instance
    game = FuzzyAsteroidGame(FuzzyController(), settings=settings)

    # To use the controller within the context of a training solution
    # game = TrainerEnvironment(FuzzyController(), settings=settings)

    # Run a single game
    score = game.run()

    print(score)
    #
    # score = game.run_headless()
    # print(score)

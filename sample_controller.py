from typing import List, Tuple, Dict

from fuzzy_controller import ControllerBase, SpaceShip
from fuzzy_asteroid_smasher import FuzzyAsteroidGame, TrainerEnvironment


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
        ship.change_angle = 0.0
        ship.thrust = 1
        ship.shoot()


if __name__ == "__main__":
    # Available settings
    settings = {
        # "graphics_on": True,
        # "sound_on": True,
        # "frequency": 60,
        # "real_time_multiplier": 1
        # "lives": 3,
        # "prints": True,
        "allow_key_presses": False
    }

    """ Start the game """
    # Create a game instance
    window = FuzzyAsteroidGame(FuzzyController(), settings=settings)

    # To use the controller within the context of a training solution
    # window = Trainer(settings)

    # Run a single game
    score = window.run_single_game()
    print(score)

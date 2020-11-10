from typing import List, Tuple, Dict

from fuzzy_asteroid_smasher import SpaceShip


class ControllerBase:
    """
    Abstract class used to manage the control of the AsteroidSmasher ship.

    Users must define a __init__() for the class to instantiate correctly
    """
    def actions(self, ship: SpaceShip, input_data: Dict[str, Tuple]) -> None:
        """
        Compute control actions of the ship. Perform all command actions via the ``ship``
        argument. This class acts as an intermediary between the controller and the environment.

        The environment looks for this function when calculating control actions for the Ship sprite.
        An instance of this class must be given to the environment to evaluate correctly.

        :param ship: Object to use when controlling the SpaceShip
        :param input_data: Input data which describes the current state of the environment
        """
        pass

"""
Asteroid Smasher

Shoot space rocks in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.asteroids
"""
import random
from typing import Any, Dict, List, Tuple

from asteroids.sprites import AsteroidSprite


class Score:
    """
    Class which is used to keep track of various scoring metrics
    """
    def __init__(self):
        """
        Default constructor requires no arguments as all values are initialized to default values, which
        are modified by the game environment over the span of each game
        """
        self.asteroids_hit = 0
        self.bullets_fired = 0
        self.deaths = 0
        self.distance_travelled = 0
        self.max_asteroids = 0
        self.max_distance = 0
        self.distance_travelled = 0

        self.frame_count = 0

    def __repr__(self):
        return str(self.__dict__)

    @property
    def accuracy(self) -> float:
        return 1.0 if not self.bullets_fired else self.asteroids_hit / self.bullets_fired

    @property
    def fraction_total_asteroids_hit(self):
        return 0.0 if not self.asteroids_hit else self.asteroids_hit / self.max_asteroids


class Map:
    """
    Class to be used to customize the game map
    """
    def __init__(self, width=800, height=600):
        """
        Class for specifying the Map dimensions (visible + otherwise)

        :param width: Width in pixels of the visible map
        :param height: Height in pixels of the visible map
        :param offscreen: Padding of the map to add space offscreen (not shown in window)
        """
        self.width = width
        self.height = height

        # Set limits of the map (outside of the visible window)
        self.LEFT_LIMIT = 0
        self.RIGHT_LIMIT = self.width
        self.BOTTOM_LIMIT = 0
        self.TOP_LIMIT = self.height

    @property
    def center(self) -> Tuple[float, float]:
        return self.width/2.0, self.height/2.0


class Scenario:
    def __init__(self, game_map: Map = None, num_asteroids: int = 0, asteroid_states: List[Dict[str, Any]]=None):
        """
        Specify the starting state of the environment, including map dimensions and optional features

        Make sure to only use

        :param map: Game Map using ``Map`` object
        :param num_asteroids: Optional Number of asteroids
        :param asteroid_states:
        """
        self.asteroid_states = list()

        # Store Map
        self.game_map = game_map if game_map else Map()

        # Check for mismatch between explicitly defined number of asteroids and Tuple of states
        if num_asteroids and asteroid_states:
            raise ValueError("Both `num_asteroids` and `asteroid_positions` are specified for Scenario() constructor."
                             "Make sure to only define one of these arguments")

        # Store asteroid states
        elif asteroid_states:
            self.asteroid_states = asteroid_states
        elif num_asteroids:
            self.asteroid_states = [dict() for _ in range(num_asteroids)]
        else:
            raise(ValueError("User should define `num_asteroids` or `asteroid_states` to create "
                             "valid custom starting states for the environment"))

    @property
    def num_starting_asteroids(self) -> float:
        return len(self.asteroid_states)

    @property
    def is_random(self) -> bool:
        return not all(state for state in self.asteroid_states) if self.asteroid_states else True

    @property
    def max_asteroids(self) -> int:
        return sum([Scenario.count_asteroids(asteroid.size) for asteroid in self.asteroids(60)])

    @staticmethod
    def count_asteroids(asteroid_size) -> float:
        # Counting based off of each asteroid making 3 children when destroyed
        return sum([3 ** (4 - size) for size in range(1, asteroid_size+1)])

    def asteroids(self, frequency: float) -> List[AsteroidSprite]:
        """
        Create
        :param frequency: OPerating frequency of the game
        :return: List of ShipSprites
        """
        asteroids = list()

        for asteroid_state in self.asteroid_states:
            if asteroid_state:
                asteroids.append(AsteroidSprite(frequency, **asteroid_state))
            else:
                asteroids.append(AsteroidSprite(frequency,
                                                position=(random.randrange(self.game_map.LEFT_LIMIT, self.game_map.RIGHT_LIMIT),
                                                          random.randrange(self.game_map.BOTTOM_LIMIT, self.game_map.TOP_LIMIT)),
                                                ))

        return asteroids


if __name__ == "__main__":
    # print(all([]))
    # print("is_random", Scenario(Map(), num_asteroids=3).is_random)
    # print("states", Scenario(Map(), num_asteroids=3).asteroid_states)
    #
    # print()
    scenario2 = Scenario(Map(), asteroid_states=[{"position": (100, 100)}])

    # assert not scenario2
    # print("states", Scenario(Map(), num_asteroids=3).asteroid_states)

    print("num_starting_asteroids", scenario2.num_starting_asteroids)
    print()
    print("max_asteroids", scenario2.max_asteroids)

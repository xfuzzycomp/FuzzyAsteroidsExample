"""
Asteroid Smasher

Shoot space rocks in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.asteroids
"""


class Score:
    """
    Class which is used to keep track of various scoring metrics
    """
    def __init__(self):
        self.asteroids_hit = 0
        self.bullets_fired = 0
        self.deaths = 0
        self.distance_travelled = 0

        self.frame_count = 0

    def __repr__(self):
        return str(self.__dict__)

    @property
    def accuracy(self) -> float:
        return 1.0 if not self.bullets_fired else self.asteroids_hit/self.bullets_fired


class Map:
    def __init__(self, width=800, height=600, offscreen=0):
        """
        Class for specifying the Map dimensions (visible + otherwise)

        :param width: Width in pixels of the visible map
        :param height: Height in pixels of the visible map
        :param offscreen: Padding of the map to add space offscreen (not shown in window)
        """
        self.width = width
        self.height = height
        self.offscreen = offscreen

        # Set limits of the map (outside of the visible window)
        self.LEFT_LIMIT = -self.offscreen
        self.RIGHT_LIMIT = self.width + self.offscreen
        self.BOTTOM_LIMIT = -self.offscreen
        self.TOP_LIMIT = self.height + self.offscreen


class Scenario:
    def __init__(self, starting_asteroid_count=3):
        self.starting_asteroid_count = starting_asteroid_count

from fuzzy_asteroids.util import Scenario
from fuzzy_asteroids.game import AsteroidGame
import numpy as np

# We recommend always using the `name`, as this puts the Scenario name into the
# game graphics window. This can be helpful for debugging your code


# A scenario with a big non moving box
scenario_big_box = Scenario(
    name="asteroid_big_box",
    asteroid_states=[{"position": (100, 600), "angle": 0.0, "speed": 0},
                     {"position": (200, 600), "angle": 0.0, "speed": 0},
                     {"position": (300, 600), "angle": 0.0, "speed": 0},
                     {"position": (400, 600), "angle": 0.0, "speed": 0},
                     {"position": (500, 600), "angle": 0.0, "speed": 0},
                     {"position": (600, 600), "angle": 0.0, "speed": 0},
                     {"position": (700, 600), "angle": 0.0, "speed": 0},
                     {"position": (100, 0), "angle": 0.0, "speed": 0},
                     {"position": (200, 0), "angle": 0.0, "speed": 0},
                     {"position": (300, 0), "angle": 0.0, "speed": 0},
                     {"position": (400, 0), "angle": 0.0, "speed": 0},
                     {"position": (500, 0), "angle": 0.0, "speed": 0},
                     {"position": (600, 0), "angle": 0.0, "speed": 0},
                     {"position": (700, 0), "angle": 0.0, "speed": 0},
                     {"position": (800, 0), "angle": 0.0, "speed": 0},
                     {"position": (0, 0), "angle": 0.0, "speed": 0},
                     {"position": (0, 100), "angle": 0.0, "speed": 0},
                     {"position": (0, 200), "angle": 0.0, "speed": 0},
                     {"position": (0, 300), "angle": 0.0, "speed": 0},
                     {"position": (0, 400), "angle": 0.0, "speed": 0},
                     {"position": (0, 500), "angle": 0.0, "speed": 0},
                     {"position": (0, 600), "angle": 0.0, "speed": 0},
                     {"position": (800, 100), "angle": 0.0, "speed": 0},
                     {"position": (800, 200), "angle": 0.0, "speed": 0},
                     {"position": (800, 300), "angle": 0.0, "speed": 0},
                     {"position": (800, 400), "angle": 0.0, "speed": 0},
                     {"position": (800, 500), "angle": 0.0, "speed": 0},
                     {"position": (800, 600), "angle": 0.0, "speed": 0},
                     ],
    ship_state={"position": (400, 300)},
)

# A scenario with a little non moving box
scenario_small_box = Scenario(
    name="asteroid_small_box",
    asteroid_states=[{"position": (200, 500), "angle": 0.0, "speed": 0},
                     {"position": (300, 500), "angle": 0.0, "speed": 0},
                     {"position": (400, 500), "angle": 0.0, "speed": 0},
                     {"position": (500, 500), "angle": 0.0, "speed": 0},

                     {"position": (200, 100), "angle": 0.0, "speed": 0},
                     {"position": (300, 100), "angle": 0.0, "speed": 0},
                     {"position": (400, 100), "angle": 0.0, "speed": 0},
                     {"position": (500, 100), "angle": 0.0, "speed": 0},
                     {"position": (600, 100), "angle": 0.0, "speed": 0},

                     {"position": (200, 200), "angle": 0.0, "speed": 0},
                     {"position": (200, 300), "angle": 0.0, "speed": 0},
                     {"position": (200, 400), "angle": 0.0, "speed": 0},

                     {"position": (600, 200), "angle": 0.0, "speed": 0},
                     {"position": (600, 300), "angle": 0.0, "speed": 0},
                     {"position": (600, 400), "angle": 0.0, "speed": 0},
                     {"position": (600, 500), "angle": 0.0, "speed": 0},
                     ],
    ship_state={"position": (400, 300)},
)

# A scenario with a big non moving box
scenario_2_still_corridors = Scenario(
    name="scenario_2_still_corridors",
    asteroid_states=[{"position": (0, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (50, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (100, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (150, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (200, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (250, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (300, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 250), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (0, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (50, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (100, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (150, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (200, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (250, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (300, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 350), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (450, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (500, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (550, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (600, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (650, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (700, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (750, 250), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (800, 250), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (450, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (500, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (550, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (600, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (650, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (700, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (750, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (800, 350), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (350, 0), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 50), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 100), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 150), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 200), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (450, 0), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 50), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 100), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 150), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 200), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (350, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 400), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 450), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 500), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 550), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (350, 600), "angle": 0.0, "speed": 0, "size": 2},

                     {"position": (450, 350), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 400), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 450), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 500), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 550), "angle": 0.0, "speed": 0, "size": 2},
                     {"position": (450, 600), "angle": 0.0, "speed": 0, "size": 2},
                     ],
    ship_state={"position": (400, 300)},
)

portfolios = [scenario_2_still_corridors]

if __name__ == "__main__":
    game = AsteroidGame()
    for por in portfolios:
        score = game.run(scenario=por)

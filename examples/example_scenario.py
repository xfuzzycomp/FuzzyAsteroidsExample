from fuzzy_asteroids.util import Scenario
from fuzzy_asteroids.game import AsteroidGame

# A scenario with randomly placed 3 asteroids
# We recommend always using the `name`, as this puts the Scenario name into the
# game graphics window. This can be helpful for debugging your code
scenario_random = Scenario(name="random_asteroids_3", num_asteroids=3)

# A scenario with randomly placed 3 asteroids - note these random positions
# are "seeded" such that this "random" scenario can be reproduced
# Read more about random seeding here https://docs.python.org/3/library/random.html#random.seed
scenario_random_repeatable = Scenario(name="random_repeatable", num_asteroids=3, seed=1)

# A scenario with random asteroids, but the ship is defined to be
# - Starting at (300, 500)
# - Pointing downward
# - Has 5 lives
scenario_ship = Scenario(name="scenario_ship",
                         num_asteroids=4,
                         ship_states=[{"position": (300, 500), "angle": 180, "lives": 5}])

# A scenario with random asteroids, and multiple ship sis defined to be
# - Ship 1: Starting at (300, 500), Pointing downward,  Has 5 lives
# - Ship 2: Starting at (400, 500), Pointing upward,  Has 4 lives
scenario_ships = Scenario(name="scenario_ship",
                          num_asteroids=4,
                          ship_states=[{"position": (300, 500), "angle": 180, "lives": 5},
                                       {"position": (400, 500), "angle": 0, "lives": 3}]
                          )

# Scenario which uses default ship state and placed asteroids in a line which fly toward the ship
scenario_asteroid_wall = Scenario(
    name="asteroid_wall",
    asteroid_states=[{"position": (200, 200), "angle": 0.0, "speed": 40},
                     {"position": (300, 200), "angle": 0.0, "speed": 40},
                     {"position": (400, 200), "angle": 0.0, "speed": 40},
                     {"position": (500, 200), "angle": 0.0, "speed": 40},
                     {"position": (600, 200), "angle": 0.0, "speed": 40},
                     ],
    ship_states=[{"position": (100, 500)}],
)


# Scenario where 1 "very-small" asteroid is declared
# Size can be between 1 and 4
scenario_asteroids_small = Scenario(
    name="asteroids-small-1",
    asteroid_states=[{"position": (200, 200), "angle": 0.0, "speed": 0, "size": 1},
                     ],
    ship_states=[{"position": (100, 500)}],
)

portfolio = [
    scenario_random,
    scenario_random_repeatable,
    scenario_ship,
    scenario_ships,
    scenario_asteroid_wall,
    scenario_asteroids_small
]

if __name__ == "__main__":
    game = AsteroidGame()
    score = game.run(scenario=scenario_ships)

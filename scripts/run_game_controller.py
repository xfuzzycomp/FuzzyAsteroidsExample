from fuzzy_asteroids.fuzzy_controller import *
from fuzzy_asteroids.fuzzy_asteroids import FuzzyAsteroidGame, Scenario
from src.controller import FuzzyController


if __name__ == "__main__":
    # Available settings
    settings = {
        "frequency": 60,
        "real_time_multiplier": 2,
        "graphics_on": True,
        "sound_on": False,
        "prints": True,
    }

    # Instantiate an instance of FuzzyAsteroidGame
    game = FuzzyAsteroidGame(settings=settings,
                             track_compute_cost=True,
                             controller_timeout=True,
                             ignore_exceptions=False)

    scenario_ship = Scenario(name="Multi-Ship",
                             num_asteroids=4,
                             ship_states=[{"position": (300, 500), "angle": 180, "lives": 1},
                                          {"position": (500, 300), "angle": 180, "lives": 5},
                                          {"position": (400, 300), "angle": 180, "lives": 3},
                                          ])

    score = game.run(controller=FuzzyController(), scenario=scenario_ship)

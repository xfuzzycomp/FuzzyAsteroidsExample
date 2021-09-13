from fuzzy_asteroids.game import AsteroidGame

if __name__ == "__main__":
    # Settings dictionary
    settings = {
        "frequency": 60,
        "real_time_multiplier": 1,
        "time_limit": 100,
        "sound_on": True,
        "graphics_on": True,
        "prints": False,
        "allow_key_presses": True,
    }

    # To use the controller within the context of a training solution
    # It is important to not create a new instance of the environment everytime
    game = AsteroidGame(settings=settings)

    # Call run() on an instance of the TrainerEnvironment
    # This function automatically manages cleanup
    score = game.run()


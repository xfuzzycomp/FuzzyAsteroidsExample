import random
import time
from asteroid_smasher import *


class Controller:
    def __init__(self):
        pass

    def calculate_actions(self, *args, **kwargs):
        pass


class FuzzyAsteroidGame(AsteroidGame):
    def __init__(self, settings: Dict[str, Any] = None):
        settings = settings if settings else {}

        # Call constructor of AsteroidGame to set up the environment
        super().__init__(settings=settings)

    @property
    def data(self) -> Dict[str, Tuple]:
        # Getting data via this "getter" method will be read-only and un-assignable
        return {
            "frame": self.frame_count,
            "map_dimensions": self.get_size(),
            "ship": tuple(sprite.state for sprite in self.player_sprite_list),
            "asteroids": tuple(sprite.state for sprite in self.asteroid_list),
            "bullets": tuple(sprite.state for sprite in self.asteroid_list),
        }

    @property
    def output_space(self) -> Dict[str, Tuple[float, float]]:
        return {
            "change_angle": (-3.0, 3.0),
            "thrust": (-0.2, 0.15),
            "fire_bullet": (False, True),
        }

    def fuzzy_control(self) -> None:
        """
        Perform Fuzzy Control here with
        """
        # Available inputs
        # data = self.data

        # Available outputs
        self.player_sprite.change_angle = 3  # Sprite turning
        self.player_sprite.thrust = 0.0  # Sprite acceleration
        # self.fire_bullet()  # Fire a bullet

    def on_update(self, delta_time: float) -> None:
        self.fuzzy_control()

        # Call on_update() of AsteroidGame parent
        AsteroidGame.on_update(self, delta_time)

    # def on_key_press(self, symbol, modifiers) -> None:
    #     # Turned off to enable "on_update" AI function
    #     pass
    #
    # def on_key_release(self, symbol, modifiers) -> None:
    #     # Turned off to enable "on_update" AI function
    #     pass


class Trainer(FuzzyAsteroidGame):
    def __init__(self, settings: Dict[str, Any] = None):
        settings = settings if settings else {}

        # Override with desired settings for training
        settings.update({
            "sound_on": False,
            "graphics_on": False,
            "real_time_multiplier": 0,
            "prints": True
        })

        # Call constructor of FuzzyAsteroidGame
        super().__init__(settings=settings)

    def on_key_press(self, symbol, modifiers) -> None:
        # Turned off during training
        pass

    def on_key_release(self, symbol, modifiers) -> None:
        # Turned off during training
        pass

    def on_draw(self) -> None:
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw message reminding the
        output = f"Running in Training Mode"
        arcade.draw_text(output, start_x=self.get_size()[0]/2.0, start_y=self.get_size()[1]/2.0,
                         color=arcade.color.WHITE, font_size=16, align="center", anchor_x="center")


if __name__ == "__main__":
    # Optional settings
    settings = {
        # "graphics_on": True,
        # "sound_on": True,
        # "frequency": 60,
        # "real_time_multiplier": 1
    }

    """ Start the game """
    # Create a game instance
    # window = FuzzyAsteroidGame(settings)
    window = Trainer(settings)

    # Run a single game
    score = window.run_single_game()
    print(score)

    score = window.run_single_game()
    print(score)

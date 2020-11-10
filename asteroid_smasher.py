"""
Asteroid Smasher

Shoot space rocks in this demo program created with
Python and the Arcade library.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.asteroid_smasher
"""
import random
import math
import arcade
import os
from typing import cast, Dict, Tuple, List, Any

VOLUME = 0.05
STARTING_ASTEROID_COUNT = 3
SCALE = 0.5
OFFSCREEN_SPACE = 300
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Asteroid Smasher"
LEFT_LIMIT = -OFFSCREEN_SPACE
RIGHT_LIMIT = SCREEN_WIDTH + OFFSCREEN_SPACE
BOTTOM_LIMIT = -OFFSCREEN_SPACE
TOP_LIMIT = SCREEN_HEIGHT + OFFSCREEN_SPACE


class BulletSprite(arcade.Sprite):
    """ Sprite that sets its angle to the direction it is traveling in. """
    def __init__(self, filename, scale, starting_angle: float, starting_position: Tuple[float, float]):
        """ Set up a bullet. """
        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        # Set the starting states
        self.bullet_speed = 13
        self.change_y = math.cos(math.radians(starting_angle)) * self.bullet_speed
        self.change_x = -math.sin(math.radians(starting_angle)) * self.bullet_speed

        self.center_x, self.center_y = starting_position

    def update(self):
        """ Move the sprite """
        super().update()
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))

    @property
    def state(self) -> Dict[str, Tuple[float, float]]:
        return {
            "position": tuple(self.position),
            "velocity": tuple(self.velocity)
        }


class ShipSprite(arcade.Sprite):
    """
    Sprite that represents our space ship.

    Derives from arcade.Sprite.
    """
    def __init__(self, filename, scale):
        """ Set up the space ship. """

        # Call the parent Sprite constructor
        super().__init__(filename, scale)

        # Info on where we are going.
        # Angle comes in automatically from the parent class.
        self.thrust = 0
        self.speed = 0
        self.max_speed = 4
        self.drag = 0.05
        self.respawning = 0

        # Mark that we are respawning.
        self.respawn()

    @property
    def state(self) -> Dict[str, Tuple]:
        return {
            "position": tuple(self.position),
            "velocity": tuple(self.velocity),
            "angle": self.angle
        }

    def respawn(self):
        """
        Called when we die and need to make a new ship.
        'respawning' is an invulnerability timer.
        """
        # If we are in the middle of respawning, this is non-zero.
        self.respawning = 1
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0

    def update(self):
        """
        Update our position and other particulars.
        """
        if self.respawning:
            self.respawning += 1
            self.alpha = self.respawning
            if self.respawning > 250:
                self.respawning = 0
                self.alpha = 255
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0

        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0

        self.speed += self.thrust
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed

        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed

        self.center_x += self.change_x
        self.center_y += self.change_y

        # If the ship goes off-screen, move it to the other side of the window
        if self.right < 0:
            self.left = SCREEN_WIDTH

        if self.left > SCREEN_WIDTH:
            self.right = 0

        if self.bottom < 0:
            self.top = SCREEN_HEIGHT

        if self.top > SCREEN_HEIGHT:
            self.bottom = 0

        """ Call the parent class. """
        super().update()


class AsteroidSprite(arcade.Sprite):
    """ Sprite that represents an asteroid. """

    def __init__(self, image_file_name, scale):
        super().__init__(image_file_name, scale=scale)
        self.size = 0

    @property
    def state(self) -> Dict[str, Tuple[float, float]]:
        return {
            "position": tuple(self.position),
            "velocity": tuple(self.velocity)
        }

    def update(self):
        """ Move the asteroid around. """
        super().update()
        if self.center_x < LEFT_LIMIT:
            self.center_x = RIGHT_LIMIT
        if self.center_x > RIGHT_LIMIT:
            self.center_x = LEFT_LIMIT
        if self.center_y > TOP_LIMIT:
            self.center_y = BOTTOM_LIMIT
        if self.center_y < BOTTOM_LIMIT:
            self.center_y = TOP_LIMIT


class AsteroidGame(arcade.Window):
    """
    Main application class.

    Based on Asteroid Smasher Example provied in arcade.examples/asteroid_smasher

    Shoot space rocks in this demo program created with
    Python and the Arcade library.

    Artwork from http://kenney.nl
    """

    def __init__(self, settings: Dict[str, Any] = None):
        settings = settings if settings else {}

        # Store game settings
        self.frequency = settings.get("frequency", 60)  # Hz
        self.real_time_multiplier = settings.get("real_time_multiplier", 1)
        self.sound_on = settings.get("sound_on", False)  # Whether sounds should play
        self.graphics_on = settings.get("graphics_on", True)  # Whether graphics should be on
        self.lives = settings.get("lives", 3)  # Number of starting lives
        self.prints = settings.get("prints", True)
        self.allow_key_presses = settings.get("allow_key_presses", True)

        if self.real_time_multiplier:
            self.timestep = (1 / float(self.frequency + 1E-6)) / float(self.real_time_multiplier)
        else:
            self.timestep = float(1E-9)

        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE, update_rate=self.timestep)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        self.directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(self.directory)

        self.frame_count = 0

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.game_over = False
        self.player_sprite = None

        # Track active keys (from eligible controls)
        self.available_keys = (arcade.key.SPACE, arcade.key.LEFT, arcade.key.RIGHT, arcade.key.UP, arcade.key.DOWN)
        self.active_key_presses = list()

        # Sounds
        self.laser_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound1 = arcade.load_sound(":resources:sounds/explosion1.wav")
        self.hit_sound2 = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.hit_sound3 = arcade.load_sound(":resources:sounds/hit1.wav")
        self.hit_sound4 = arcade.load_sound(":resources:sounds/hit2.wav")

    def _play_sound(self, sound):
        # Private sound playing function (checks stored sound_on) using globally specified volume
        if self.sound_on:
            sound.play(VOLUME)

    def _print_terminal(self, msg: str):
        if self.prints:
            print(msg)

    def start_new_game(self) -> None:
        """ Set up the game and initialize the variables. """
        self.score = 0
        self.frame_count = 0
        self.game_over = False

        # Sprite lists
        self.player_sprite_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = ShipSprite(":resources:images/space_shooter/playerShip1_orange.png", SCALE)
        self.player_sprite_list.append(self.player_sprite)

        # Set up the little icons that represent the player lives.
        cur_pos = 10
        for i in range(self.lives):
            life = arcade.Sprite(":resources:images/space_shooter/playerLife1_orange.png", SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.ship_life_list.append(life)

        # Make the asteroids
        image_list = (":resources:images/space_shooter/meteorGrey_big1.png",
                      ":resources:images/space_shooter/meteorGrey_big2.png",
                      ":resources:images/space_shooter/meteorGrey_big3.png",
                      ":resources:images/space_shooter/meteorGrey_big4.png")
        for i in range(STARTING_ASTEROID_COUNT):
            image_no = random.randrange(4)
            enemy_sprite = AsteroidSprite(image_list[image_no], SCALE)
            enemy_sprite.guid = "Asteroid"

            enemy_sprite.center_y = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
            enemy_sprite.center_x = random.randrange(LEFT_LIMIT, RIGHT_LIMIT)

            enemy_sprite.change_x = random.random() * 2 - 1
            enemy_sprite.change_y = random.random() * 2 - 1

            enemy_sprite.change_angle = (random.random() - 0.5) * 2
            enemy_sprite.size = 4
            self.asteroid_list.append(enemy_sprite)

    def on_draw(self) -> None:
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.asteroid_list.draw()
        self.ship_life_list.draw()
        self.bullet_list.draw()
        self.player_sprite_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 70, arcade.color.WHITE, 13)

        output = f"Asteroid Count: {len(self.asteroid_list)}"
        arcade.draw_text(output, 10, 50, arcade.color.WHITE, 13)

    def fire_bullet(self) -> None:
        """Call to fire a bullet"""
        bullet_sprite = BulletSprite(":resources:images/space_shooter/laserBlue01.png", SCALE,
                                     starting_angle=self.player_sprite.angle,
                                     starting_position=(self.player_sprite.center_x, self.player_sprite.center_y))
        bullet_sprite.guid = "Bullet"
        bullet_sprite.update()

        self.bullet_list.append(bullet_sprite)
        self._play_sound(self.laser_sound)

    def on_key_press(self, symbol, modifiers) -> None:
        """ Called whenever a key is pressed. """
        if self.allow_key_presses:
            # Track active keys
            if symbol in self.available_keys:
                self.active_key_presses.append(symbol)

            # Shoot if the player hit the space bar and we aren't respawning.
            if not self.player_sprite.respawning and symbol == arcade.key.SPACE:
                self.fire_bullet()

            if symbol == arcade.key.LEFT:
                self.player_sprite.change_angle = 3
            elif symbol == arcade.key.RIGHT:
                self.player_sprite.change_angle = -3
            elif symbol == arcade.key.UP:
                self.player_sprite.thrust = 0.15
            elif symbol == arcade.key.DOWN:
                self.player_sprite.thrust = -.2

    def on_key_release(self, symbol, modifiers) -> None:
        """ Called whenever a key is released. """
        if self.allow_key_presses:

            # Remove released key from active keys list
            if symbol in self.available_keys:
                self.active_key_presses.pop(self.active_key_presses.index(symbol))

            if symbol == arcade.key.LEFT:
                self.player_sprite.change_angle = 0
            elif symbol == arcade.key.RIGHT:
                self.player_sprite.change_angle = 0
            elif symbol == arcade.key.UP:
                self.player_sprite.thrust = 0
            elif symbol == arcade.key.DOWN:
                self.player_sprite.thrust = 0

    def split_asteroid(self, asteroid: AsteroidSprite) -> None:
        """ Split an asteroid into chunks. """
        x = asteroid.center_x
        y = asteroid.center_y
        self.score += 1

        if asteroid.size == 4:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = (":resources:images/space_shooter/meteorGrey_med1.png",
                              ":resources:images/space_shooter/meteorGrey_med2.png")

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 2.5 - 1.25
                enemy_sprite.change_y = random.random() * 2.5 - 1.25

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 3

                self.asteroid_list.append(enemy_sprite)
                self._play_sound(self.hit_sound1)

        elif asteroid.size == 3:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = (":resources:images/space_shooter/meteorGrey_small1.png",
                              ":resources:images/space_shooter/meteorGrey_small2.png")

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3 - 1.5
                enemy_sprite.change_y = random.random() * 3 - 1.5

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 2

                self.asteroid_list.append(enemy_sprite)
                self._play_sound(self.hit_sound2)

        elif asteroid.size == 2:
            for i in range(3):
                image_no = random.randrange(2)
                image_list = (":resources:images/space_shooter/meteorGrey_tiny1.png",
                              ":resources:images/space_shooter/meteorGrey_tiny2.png")

                enemy_sprite = AsteroidSprite(image_list[image_no],
                                              SCALE * 1.5)

                enemy_sprite.center_y = y
                enemy_sprite.center_x = x

                enemy_sprite.change_x = random.random() * 3.5 - 1.75
                enemy_sprite.change_y = random.random() * 3.5 - 1.75

                enemy_sprite.change_angle = (random.random() - 0.5) * 2
                enemy_sprite.size = 1

                self.asteroid_list.append(enemy_sprite)
                self._play_sound(self.hit_sound3)

        elif asteroid.size == 1:
            self._play_sound(self.hit_sound4)

    def on_update(self, delta_time) -> None:
        """
        Move everything

        :param delta_time: Time since last time step
        """
        self.frame_count += 1

        if not self.game_over:
            self.asteroid_list.update()
            self.bullet_list.update()
            self.player_sprite_list.update()

            for bullet in self.bullet_list:
                asteroids = arcade.check_for_collision_with_list(bullet, self.asteroid_list)

                for asteroid in asteroids:
                    self.split_asteroid(cast(AsteroidSprite, asteroid))  # expected AsteroidSprite, got Sprite instead
                    asteroid.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()

                # Remove bullet if it goes off-screen
                size = max(bullet.width, bullet.height)
                if bullet.center_x < 0 - size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_x > SCREEN_WIDTH + size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_y < 0 - size:
                    bullet.remove_from_sprite_lists()
                if bullet.center_y > SCREEN_HEIGHT + size:
                    bullet.remove_from_sprite_lists()

            if not self.player_sprite.respawning:
                asteroids = arcade.check_for_collision_with_list(self.player_sprite, self.asteroid_list)
                if len(asteroids) > 0:
                    if self.lives > 0:
                        self.lives -= 1
                        self.player_sprite.respawn()
                        self.split_asteroid(cast(AsteroidSprite, asteroids[0]))
                        asteroids[0].remove_from_sprite_lists()
                        self.ship_life_list.pop().remove_from_sprite_lists()
                        self._print_terminal("Crash")
                    else:
                        self.game_over = True
                        self._print_terminal("Game over")

    def run_single_game(self) -> float:
        """
        Run a single instance of the game with the specified settings
        :return: Score from the environment
        """
        self.start_new_game()
        arcade.run()
        return self.score

    def run(self):
        self.start_new_game()
        arcade.run()


if __name__ == "__main__":
    """ Start the game """
    settings = {
        "frequency": 60,
        "sound_on": False
    }
    window = AsteroidGame(settings)
    window.start_new_game()
    arcade.run()


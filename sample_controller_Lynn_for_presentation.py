from typing import List, Tuple, Dict
import math
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from asteroids.fuzzy_controller import ControllerBase, SpaceShip


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

    def __init__(self, chromosome):
        """
        Create your fuzzy logic controllers and other objects here
        """
        # Define the Input Mfs
        ################### Asteroid Direction relative to plane ######################
        Asteroid_Angle_from_plane = ctrl.Antecedent(np.arange(-180, 180, 1), 'Asteroid_Angle_from_plane')

        Asteroid_Angle_from_plane['neg_small'] = fuzz.trimf(Asteroid_Angle_from_plane.universe, [-60, 0, 1])
        Asteroid_Angle_from_plane['neg_medium'] = fuzz.trimf(Asteroid_Angle_from_plane.universe, [-120, -60, 0])
        Asteroid_Angle_from_plane['neg_large'] = fuzz.trimf(Asteroid_Angle_from_plane.universe, [-180, -180, -60])
        Asteroid_Angle_from_plane['small'] = fuzz.trimf(Asteroid_Angle_from_plane.universe, [-1, 0, 60])
        Asteroid_Angle_from_plane['medium'] = fuzz.trimf(Asteroid_Angle_from_plane.universe, [0, 60, 120])
        Asteroid_Angle_from_plane['large'] = fuzz.trimf(Asteroid_Angle_from_plane.universe, [60, 180, 180])


        # Define the Output Mfs


        # convert values from chromosome in GA to correct format for rules in fuzzy system



        # Define the Rule Base
        rule1 = ctrl.Rule(Asteroid_Angle_from_plane['neg_small'] & input2['small'], consequent=(
        output1[0], output2[0], Plane_Shooting[0]))[shoot_strings[12]]))

        # more rules, all the rules

        self.plane_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, ...])

        ## May need to flush after run so that less memory is used!!
        self.flying = ctrl.ControlSystemSimulation(self.plane_ctrl, flush_after_run=100)


    def actions(self, ship: SpaceShip, input_data: Dict[str, Tuple]) -> None:
        """
        Compute control actions of the ship. Perform all command actions via the ``ship``
        argument. This class acts as an intermediary between the controller and the environment.

        The environment looks for this function when calculating control actions for the Ship sprite.

        :param ship: Object to use when controlling the SpaceShip
        :param input_data: Input data which describes the current state of the environment
        """

        # Functions to define any actions needed
        def get_distance(self, asteroid_list):

            return (distance, current_asteroid)

        def get_angle():
            angle = 2
            return angle

        asteroid_list = []
        distance, current_asteroid = get_distance(self, asteroid_list)

        self.flying.input['Asteroid_Angle_from_plane'] = get_angle()


        self.flying.compute()

        ship.thrust = self.flying.output['Plane Thrust']

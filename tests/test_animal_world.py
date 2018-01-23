# -*- coding: utf-8 -*-

import unittest
import animal_world


class TestAnimalWorld(unittest.TestCase):

    def setUp(self):
        """ Create a test world. """
        self.test_world = animal_world.World()

    def tearDown(self):
        pass

    def test_load_world(self):
        """ Load the world. """
        self.world_json = False
        self.test_world.load_world()
        self.world_json = self.test_world.world_json
        self.assertTrue(self.world_json, "World not loaded.")

    def test_save_world(self):
        result = False
        self.test_world.worl_json = self.test_world.load_world()
        result = self.test_world.save_world()
        self.assertTrue(result, "World could not be saved.")

    def test_get_hazards(self):
        """ Load the hazards. """
        self.hazards = False
        self.test_load_world()
        self.hazards = self.test_world.get_hazards()
        self.assertTrue(self.hazards, "Hazards not loaded.")

    def test_get_animals(self):
        """ Load the hazards. """
        self.animals = False
        self.test_load_world()
        self.animals = self.test_world.get_animals()
        self.assertTrue(self.animals, "Animals not loaded.")


if __name__ == '__main__':
    unittest.__main__()

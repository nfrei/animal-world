#!/usr/bin/env python

import json
import random


class World:

    json_init = """
{
    "hazards": {
        "hunters": {
            "mortality_increase": 0.1,
            "probability": 0.3
        },
        "disease": {
            "mortality_increase": 0.2,
            "probability": 0.25
        }
    },
    "animals": {
        "rabbits": {
            "mortality": 0.4,
            "number": 100,
            "reproduction": 2.0
        },
        "foxes": {
            "mortality": 0.02,
            "number": 10,
            "reproduction": 1.7
        }
    }
}
    """

    world_path = "./world.json"
    world_json = {}

    def load_world(self):
        try:
            with open(self.world_path, 'r') as f:
                json_file = json.loads(f.read())
                self.world_json = json_file
        except IOError:
            print "Could not read file: ", self.world_path
            print "Starting a new world."
            self.world_json = self.json_init

    def save_world(self):
        try:
            with open(self.world_path, 'w') as f:
                world_dump = json.dumps(self.world_json, indent=4)
                f.write(world_dump)
            return True
        except IOError:
            print "Could not save file: ", self.world_path

    def get_hazards(self):
        hazards = self.world_json['hazards']

        for h in hazards:
            probability = hazards[h]['probability']
            mortality_increase = hazards[h]['mortality_increase']

        return hazards

    def get_animals(self):
        """To do."""
        return True

    def one_cycle(self):
        self.load_world()

        hazards = self.get_hazards()

        for a in self.world_json['animals']:
            current_number = self.world_json['animals'][a]['number']
            reproduction = self.world_json['animals'][a]['reproduction']
            mortality = self.world_json['animals'][a]['mortality']
            hazard_mortality = 0

            for h in hazards:
                r = random.random()
                hazard_probability = hazards[h]['probability']

                if hazard_probability <= r:
                    mortality_increase = hazards[h]['mortality_increase']
                    mortality = mortality + mortality_increase
                    print "Mortality for %s increases by %f because of %s." \
                          % (a, mortality_increase, h)
                else:
                    pass

            new_number = current_number * (reproduction - mortality)

            if new_number < 0:
                new_number = 0

            self.world_json['animals'][a]['number'] = int(new_number)
            print "New number of %s is %d." % (a, new_number)

        return self.save_world()


my_world = World()
my_world.one_cycle()

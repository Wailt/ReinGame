from numpy import random as npr
import numpy as np

temperature = 10

class Brain():
    #only for movement
    def __init__(self, npc):
        self.dec = {'nearest': 0, 'random': 0, 'stop': 0}

    def decide(self, npc, world):


        x = npc.phisics['x']()
        y = npc.phisics['y']()
        if world:
            sorted_world = sorted(world, key=lambda entity: (entity.phisics['x']() - x)**2 + (entity.phisics['y']() - y)**2)

            nearest_x, nearest_y = sorted_world[0].phisics['x'](), sorted_world[0].phisics['y']()

            decision = {'moove': {key: (0, 0) for key in self.dec}}

            #TODO: here without stainding. Add standing in future
            decision['moove']['nearest'] = (((x - nearest_x) > 0) * 2 - 1, ((y - nearest_y) > 0) * 2 - 1)
                                            # #(((x - nearest_x) < 0) * 2 - 1, ((y - nearest_y) < 0) * 2 - 1)
            decision['moove']['random'] = (npr.randint(0, 3) - 1, npr.randint(0, 3) - 1)
            decision['moove']['stop'] = (0, 0)
            # TODO: here temperature
            norma = sum(np.exp(temperature * np.array([self.dec[k] for k in self.dec])))
            level = npr.rand()

            cumsum = 0

            print(np.exp([temperature * self.dec[key] for key in self.dec]) / norma)

            for key in self.dec:
                #TODO: here temperature
                cumsum += np.exp(temperature * self.dec[key]) / norma

                if cumsum >= level:
                    return {'moove': (key, decision['moove'][key])}
            return {'moove': ('random', decision['moove'][''])}

    def count_regret(self, npc, world_one_stats, world_two_stats):
        learn_rate = 0.01
        regret = {key: (world_two_stats[key] - world_one_stats[key]) * learn_rate for key in world_one_stats}
        return regret

    def stat(self, npc, world):
        stats = {'moove': 0}
        if world:
            x = npc.phisics['x']()
            y = npc.phisics['y']()

            sorted_world = sorted(world, key=lambda entity: (entity.phisics['x']() - x)**2 + (entity.phisics['y']() - y)**2)

            #TODO: error when world is empty
            nearest_x, nearest_y = sorted_world[0].phisics['x'](), sorted_world[0].phisics['y']()

            stats['moove'] = ((nearest_x - x) ** 2 + (nearest_y - y) ** 2) ** 0.5

        return stats

    def learn(self, action, regret):
        #TODO: now works only for moove
        #TODO: what if many fields in regret. SO i have to make a dict of actions
        forgot_index = 1e-7
        for key in regret:
            self.dec[action] += regret[key] + forgot_index
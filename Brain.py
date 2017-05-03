from numpy import random as npr

class Brain():
    #only for movement
    def __init__(self, npc):
        self.dec = {'nearst': 1, 'random': 1}

    def decide(self, npc, world):
        x = npc.phisics['x']
        y = npc.phisics['y']

        sorted_world = sorted(world, key=lambda entity: (entity.phisics['x'] - x)**2 + (entity.phisics['y'] - y)**2)

        nearest_x, nearest_y = sorted_world[0].phisics['x'], sorted_world[0].phisics['y']

        decision = {'moove': {key: (0, 0) for key in self.dec}}
        decision['nearest'] = (((x - nearest_x) > 0) * 3 - 1, ((y - nearest_y) > 0) * 3 - 1)
        decision['random'] = (npr.randint(0, 3) - 1, npr.randint(0, 3) - 1)

        norma = sum([self.dec[i] for i in self.dec])

        level = npr.rand()

        cumsum = 0
        for key in self.dec:
            cumsum += self.dec[key] / norma
            if cumsum >= level:
                return (key, decision['key'])

    def count_regret(self):
        pass

    def stat(self):
        pass

from environment import Environment
from collections import OrderedDict
import numpy as np


class FakeEnvironment(Environment):
    ACTION_LIST = ["left", "stay", "right"]

    def __init__(self):
        self.draw = 0
        self.last_state = np.ones((84, 84, 3))
        self.terminal = False
        self.last_action = 1
        self.last_reward = 0.0
        self.lim = 300

    @staticmethod
    def get_action_size():
        return len(FakeEnvironment.ACTION_LIST)

    def reset(self):
        self.draw = 0
        self.terminal = False

    def process(self, action):
        self.draw += 1
        if self.lim is not None and self.draw >= self.lim:
            self.terminal = True

        rewards = [-1.0, 0.0, 1.0]

        reward = rewards[action]
        self.last_reward = reward
        self.last_action = action

        return self.last_state, reward, self.terminal, self._calc_pixel_change(self.last_state,
                                                                               self.last_state)

    def stop(self):
        pass

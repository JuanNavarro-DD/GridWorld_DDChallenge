#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 21:25:05 2021

@author: oliver
"""

import gymnasium as gym
import matplotlib.pyplot as plt
from minigrid.utils.window import Window


import time

env_name = "MiniGrid-Empty-16x16-v0"


def mypolicy(env, obs):
    # this selects a random action. replace it with something better.
    action = env.action_space.sample()
    return action


if __name__ == "__main__":
    seed = 1
    # torch.manual_seed(seed)
    render = True

    env = gym.make(env_name)

    starttime = time.time()

    obs, ep_reward, done = env.reset(), 0, False
    window = Window(f'minigrid - {env_name}')

    for t in range(1, 1000):  # Don't infinite loop while learning

        # select action (according to my policy)
        action = mypolicy(env, obs)

        # take the action
        obs, reward, done, _, _ = env.step(action)
        

        if render:
            img = env.get_frame()
            window.show_img(img)
            

        ep_reward += reward
        if done:
            break

    print(ep_reward)
    finishtime = time.time()

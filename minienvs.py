#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 22:51:42 2021

@author: oliver
"""

from minigrid.envs import EmptyEnv
from minigrid.register import register, env_list


class EmptyRandomEnv10x10(EmptyEnv):
    def __init__(self):
        super().__init__(size=10, agent_start_pos=None)


if "MiniGrid-Empty-Random-10x10-v0" not in env_list:
    register(
        id="MiniGrid-Empty-Random-10x10-v0", entry_point="minienvs:EmptyRandomEnv10x10"
    )

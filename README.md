# GridWorld_DDChallenge

As previously explored in our previous D-learn, Reinforcement learning is an area of machine learning, where an agent will take steps to maximize a reward, and looks for the path that returns the highest reward. There's more information online about this, for example, this [Reinforcement learning](https://www.geeksforgeeks.org/?p=195593) article

## first challenge

Create a policy that takes the arrow to the green square (No RL required yet)

## Second challenge

Create a temporal difference agent that learns how to move and resolve the minigrid environment, use `MiniGrid-Empty-16x16-v0`. use this article about [epsilon greedy algorithm](https://www.geeksforgeeks.org/epsilon-greedy-algorithm-in-reinforcement-learning/) and this [Qlearning in python](https://www.geeksforgeeks.org/q-learning-in-python/?ref=lbp) one as guides.

## Third Challenge

Explore different environment available in the `minigrid` library and create a neural network based RL agent to solve this problems. (use `MiniGrid-DoorKey-8x8-v0` for example)

# Notes and useful repositories

Use the [requirement](requirements.txt) file to install the required libraries for the minigrid environments. For the agent policies you may want to explore this [article](https://www.geeksforgeeks.org/sarsa-reinforcement-learning/) or this [repository](https://github.com/lcswillems/rl-starter-files). And for more information about the minigrid environments visit its [repository](https://github.com/Farama-Foundation/Minigrid/tree/ad6b82ed2811b1f7b3da6c0c0948c8e0bfc8b708).

You can use the [minigrid.py](minigrid.py) file as an example for your first steps in this challenge. It is a good exercise to practice with this [interactive tool](http://rl-lab.com/gridworld-td) as part of an exploration phase of this challenge and reading this [article](https://towardsdatascience.com/td-in-reinforcement-learning-the-easy-way-f92ecfa9f3ce) that explains TD reinforcement learning techniques.

# Virtual environment instructions

I recommend you to create a virtual environment and this can be done by running

```bash
python -m venv venv
```

to understand the challenge better let's first understand the first environment by running:

```bash
python .\venv\Lib\site-packages\minigrid\manual_control.py --env MiniGrid-Empty-16x16-v0
```

to have a manual control over the environment.

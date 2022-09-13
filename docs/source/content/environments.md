---
layout: "contents"
title: Environments
firstpage:
---

# Distributional shift environment

This environment is based on one of the DeepMind [AI safety gridworlds](https://github.com/deepmind/ai-safety-gridworlds).
The agent starts in the top-left corner and must reach the goal which is in the top-right corner, but has to avoid stepping
into lava on its way. The aim of this environment is to test an agent's ability to generalize. There are two slightly
different variants of the environment, so that the agent can be trained on one variant and tested on the other.

<p align="center">
  <img src="figures/DistShift1.png" width=200 alt="Figure of the DistShift1 environment">
  <img src="figures/DistShift2.png" width=200 alt="Figure of the DistShift2 environment">
</p>

Registered configurations:
- `MiniGrid-DistShift1-v0`
- `MiniGrid-DistShift2-v0`

# Lava gap environment

The agent has to reach the green goal square at the opposite corner of the room,
and must pass through a narrow gap in a vertical strip of deadly lava. Touching
the lava terminate the episode with a zero reward. This environment is useful
for studying safety and safe exploration.

Registered configurations:
- `MiniGrid-LavaGapS5-v0`
- `MiniGrid-LavaGapS6-v0`
- `MiniGrid-LavaGapS7-v0`

<p align="center">
  <img src="figures/LavaGapS6.png" width=200 alt="Figure of the LavaGap environment">
</p>

# Lava crossing environment

The agent has to reach the green goal square on the other corner of the room
while avoiding rivers of deadly lava which terminate the episode in failure.
Each lava stream runs across the room either horizontally or vertically, and
has a single crossing point which can be safely used;  Luckily, a path to the
goal is guaranteed to exist. This environment is useful for studying safety and
safe exploration.

<p align="center">
  <img src="figures/LavaCrossingS9N1.png" width=200 alt="Figure of the LavaCrossingS9N1 environment">
  <img src="figures/LavaCrossingS9N2.png" width=200 alt="Figure of the LavaCrossingS9N2 environment">
  <img src="figures/LavaCrossingS9N3.png" width=200 alt="Figure of the LavaCrossingS9N3 environment">
  <img src="figures/LavaCrossingS11N5.png" width=250 alt="Figure of the LavaCrossingS11N5 environment">
</p>

Registered configurations:
- `MiniGrid-LavaCrossingS9N1-v0`
- `MiniGrid-LavaCrossingS9N2-v0`
- `MiniGrid-LavaCrossingS9N3-v0`
- `MiniGrid-LavaCrossingS11N5-v0`

# Simple crossing environment

Similar to the `LavaCrossing` environment, the agent has to reach the green
goal square on the other corner of the room, however lava is replaced by
walls. This MDP is therefore much easier and maybe useful for quickly
testing your algorithms.

<p align="center">
  <img src="figures/SimpleCrossingS9N1.png" width=200 alt="Figure of the SimpleCrossingS9N1 environment">
  <img src="figures/SimpleCrossingS9N2.png" width=200 alt="Figure of the SimpleCrossingS9N2 environment">
  <img src="figures/SimpleCrossingS9N3.png" width=200 alt="Figure of the SimpleCrossingS9N3 environment">
  <img src="figures/SimpleCrossingS11N5.png" width=250 alt="Figure of the SimpleCrossingS11N5 environment">
</p>

Registered configurations:
- `MiniGrid-SimpleCrossingS9N1-v0`
- `MiniGrid-SimpleCrossingS9N2-v0`
- `MiniGrid-SimpleCrossingS9N3-v0`
- `MiniGrid-SimpleCrossingS11N5-v0`

## Dynamic obstacles environment

This environment is an empty room with moving obstacles. 
The goal of the agent is to reach the green goal square without colliding with any obstacle. 
A large penalty is subtracted if the agent collides with an obstacle and the episode finishes. 
This environment is useful to test Dynamic Obstacle Avoidance for mobile robots with Reinforcement Learning in Partial Observability.

<p align="center">
    <img src="figures/dynamic_obstacles.gif" alt="GIF of the Dynamic Obstacles environment">
</p>

Registered configurations:
- `MiniGrid-Dynamic-Obstacles-5x5-v0`
- `MiniGrid-Dynamic-Obstacles-Random-5x5-v0`
- `MiniGrid-Dynamic-Obstacles-6x6-v0`
- `MiniGrid-Dynamic-Obstacles-Random-6x6-v0`
- `MiniGrid-Dynamic-Obstacles-8x8-v0`
- `MiniGrid-Dynamic-Obstacles-16x16-v0`


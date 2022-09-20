---
title: Empty Environment
---

# Empty

This environment is an empty room, and the goal of the agent is to reach the
green goal square, which provides a sparse reward. A small penalty is
subtracted for the number of steps to reach the goal. This environment is
useful, with small rooms, to validate that your RL algorithm works correctly,
and with large rooms to experiment with sparse rewards and exploration.
The random variants of the environment have the agent starting at a random
position for each episode, while the regular variants have the agent always
starting in the corner opposite to the goal.

```{figure} ../_static/img/figures/empty-env.png
   :alt: Figure of the empty environment
   :width: 250
```

Registered configurations: 
- `MiniGrid-Empty-5x5-v0`
- `MiniGrid-Empty-Random-5x5-v0`
- `MiniGrid-Empty-6x6-v0`
- `MiniGrid-Empty-Random-6x6-v0`
- `MiniGrid-Empty-8x8-v0`
- `MiniGrid-Empty-16x16-v0`
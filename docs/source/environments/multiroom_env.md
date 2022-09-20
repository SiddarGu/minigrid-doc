---
title: Multi-room Environment
---

# Multi-room

This environment has a series of connected rooms with doors that must be
opened in order to get to the next room. The final room has the green goal
square the agent must get to. This environment is extremely difficult to
solve using RL alone. However, by gradually increasing the number of
rooms and building a curriculum, the environment can be solved.

```{figure} ../_static/img/figures/multi-room.gif
   :alt: Figure of the Multi-room environment
```

Registered configurations:
- `MiniGrid-MultiRoom-N2-S4-v0` (two small rooms)
- `MiniGrid-MultiRoom-N4-S5-v0` (four rooms)
- `MiniGrid-MultiRoom-N6-v0` (six rooms)
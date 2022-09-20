---
title: Lava Crossing Environment
---

# Lava crossing

The agent has to reach the green goal square on the other corner of the room
while avoiding rivers of deadly lava which terminate the episode in failure.
Each lava stream runs across the room either horizontally or vertically, and
has a single crossing point which can be safely used;  Luckily, a path to the
goal is guaranteed to exist. This environment is useful for studying safety and
safe exploration.

```{figure} ../_static/img/figures/LavaCrossingS9N1.png
   :alt: Figure of the LavaCrossingS9N1 environment
   :width: 200
```
```{figure} ../_static/img/figures/LavaCrossingS9N2.png
   :alt: Figure of the LavaCrossingS9N2 environment
   :width: 200
```
```{figure} ../_static/img/figures/LavaCrossingS9N3.png
   :alt: Figure of the LavaCrossingS9N3 environment
   :width: 200
```
```{figure} ../_static/img/figures/LavaCrossingS11N5.png
   :alt: Figure of the LavaCrossingS11N5 environment
   :width: 250
```

Registered configurations:
- `MiniGrid-LavaCrossingS9N1-v0`
- `MiniGrid-LavaCrossingS9N2-v0`
- `MiniGrid-LavaCrossingS9N3-v0`
- `MiniGrid-LavaCrossingS11N5-v0`
---
title: Go-to-door Environment
---

# Go-to-door

This environment is a room with four doors, one on each wall. The agent
receives a textual (mission) string as input, telling it which door to go to,
(eg: "go to the red door"). It receives a positive reward for performing the
`done` action next to the correct door, as indicated in the mission string.

```{figure} ../_static/img/figures/gotodoor-6x6.png
   :alt: Figure of the go-to-door environment
   :width: 400
```

Registered configurations:
- `MiniGrid-GoToDoor-5x5-v0`
- `MiniGrid-GoToDoor-6x6-v0`
- `MiniGrid-GoToDoor-8x8-v0`
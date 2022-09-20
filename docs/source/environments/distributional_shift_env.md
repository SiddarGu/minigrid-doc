---
title: Distributional Shift Environment
---

# Distributional shift

This environment is based on one of the DeepMind [AI safety gridworlds](https://github.com/deepmind/ai-safety-gridworlds).
The agent starts in the top-left corner and must reach the goal which is in the top-right corner, but has to avoid stepping
into lava on its way. The aim of this environment is to test an agent's ability to generalize. There are two slightly
different variants of the environment, so that the agent can be trained on one variant and tested on the other.


```{figure} ../_static/img/figures/DistShift1.png
   :alt: Figure of the DistShift1 environment
   :width: 200
```

```{figure} ../_static/img/figures/DistShift2.png
   :alt: Figure of the DistShift2 environment
   :width: 200
```

Registered configurations:
- `MiniGrid-DistShift1-v0`
- `MiniGrid-DistShift2-v0`
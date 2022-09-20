---
title: Locked Room Environment
---

# Locked room

The environment has six rooms, one of which is locked. The agent receives
a textual mission string as input, telling it which room to go to in order
to get the key that opens the locked room. It then has to go into the locked
room in order to reach the final goal. This environment is extremely difficult
to solve with vanilla reinforcement learning alone.

Registered configurations:
- `MiniGrid-LockedRoom-v0`
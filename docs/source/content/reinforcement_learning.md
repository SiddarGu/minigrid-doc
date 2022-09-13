---
layout: "contents"
title: Reinforcement Learning
firstpage:
---

# Reinforcement Learning

If you want to train an agent with reinforcement learning, I recommend using the code found in the [torch-rl](https://github.com/lcswillems/torch-rl) repository. 
This code has been tested and is known to work with this environment. The default hyper-parameters are also known to converge.

A sample training command is:

```
cd torch-rl
python3 -m scripts.train --env MiniGrid-Empty-8x8-v0 --algo ppo
```

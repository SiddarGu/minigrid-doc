---
layout: "contents"
title: Included Environments
firstpage:
---

# Included Environments

The environments listed below are implemented in the [gym_minigrid/envs](/gym_minigrid/envs) directory.
Each environment provides one or more configurations registered with OpenAI gym. Each environment
is also programmatically tunable in terms of size/complexity, which is useful for curriculum learning
or to fine-tune difficulty.

## Empty environment

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

## Four rooms environment

Classic four room reinforcement learning environment. The agent must navigate
in a maze composed of four rooms interconnected by 4 gaps in the walls. To
obtain a reward, the agent must reach the green goal square. Both the agent
and the goal square are randomly placed in any of the four rooms.

```{figure} ../_static/img/figures/four-rooms-env.png
   :alt: Figure of the four room environment
```

Registered configurations: 
- `MiniGrid-FourRooms-v0`

## Door & key environment

This environment has a key that the agent must pick up in order to unlock
a goal and then get to the green goal square. This environment is difficult,
because of the sparse reward, to solve using classical RL algorithms. It is
useful to experiment with curiosity or curriculum learning.

```{figure} ../_static/img/figures/door-key-env.png
   :alt: Figure of the door key environment
```

Registered configurations: 
- `MiniGrid-DoorKey-5x5-v0`
- `MiniGrid-DoorKey-6x6-v0`
- `MiniGrid-DoorKey-8x8-v0`
- `MiniGrid-DoorKey-16x16-v0`

## Multi-room environment

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

## Fetch environment

This environment has multiple objects of assorted types and colors. The
agent receives a textual string as part of its observation telling it
which object to pick up. Picking up the wrong object terminates the
episode with zero reward.

```{figure} ../_static/img/figures/fetch-env.png
   :alt: Figure of the fetch environment
   :width: 450
```

Registered configurations:
- `MiniGrid-Fetch-5x5-N2-v0`
- `MiniGrid-Fetch-6x6-N2-v0`
- `MiniGrid-Fetch-8x8-N3-v0`

## Go-to-door environment

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

## Put-near environment

The agent is instructed through a textual string to pick up an object and
place it next to another object. This environment is easy to solve with two
objects, but difficult to solve with more, as it involves both textual
understanding and spatial reasoning involving multiple objects.

Registered configurations:
- `MiniGrid-PutNear-6x6-N2-v0`
- `MiniGrid-PutNear-8x8-N3-v0`

## Red and blue doors environment

The agent is randomly placed within a room with one red and one blue door
facing opposite directions. The agent has to open the red door and then open
the blue door, in that order. Note that, surprisingly, this environment is
solvable without memory.

Registered configurations:
- `MiniGrid-RedBlueDoors-6x6-v0`
- `MiniGrid-RedBlueDoors-8x8-v0`

## Memory environment

This environment is a memory test. The agent starts in a small room
where it sees an object. It then has to go through a narrow hallway
which ends in a split. At each end of the split there is an object,
one of which is the same as the object in the starting room. The
agent has to remember the initial object, and go to the matching
object at split.

Registered configurations:
- `MiniGrid-MemoryS17Random-v0`
- `MiniGrid-MemoryS13Random-v0`
- `MiniGrid-MemoryS13-v0`
- `MiniGrid-MemoryS11-v0`

## Locked room environment

The environment has six rooms, one of which is locked. The agent receives
a textual mission string as input, telling it which room to go to in order
to get the key that opens the locked room. It then has to go into the locked
room in order to reach the final goal. This environment is extremely difficult
to solve with vanilla reinforcement learning alone.

Registered configurations:
- `MiniGrid-LockedRoom-v0`

## Key corridor environment

This environment is similar to the locked room environment, but there are
multiple registered environment configurations of increasing size,
making it easier to use curriculum learning to train an agent to solve it.
The agent has to pick up an object which is behind a locked door. The key is
hidden in another room, and the agent has to explore the environment to find
it. The mission string does not give the agent any clues as to where the
key is placed. This environment can be solved without relying on language.

```{figure} ../_static/img/figures/KeyCorridorS3R1.png
   :alt: Figure of the Key Corridor for config S3R1
   :width: 250
```
```{figure} ../_static/img/figures/KeyCorridorS3R2.png
   :alt: Figure of the Key Corridor for config S3R2
   :width: 250
```
```{figure} ../_static/img/figures/KeyCorridorS3R3.png
   :alt: Figure of the Key Corridor for config S3R3
   :width: 250
```
```{figure} ../_static/img/figures/KeyCorridorS4R3.png
   :alt: Figure of the Key Corridor for config S4R3
   :width: 250
```
```{figure} ../_static/img/figures/KeyCorridorS5R3.png
   :alt: Figure of the Key Corridor for config S5R3
   :width: 250
```
```{figure} ../_static/img/figures/KeyCorridorS6R3.png
   :alt: Figure of the Key Corridor for config S6R3
   :width: 250
```

Registered configurations:
- `MiniGrid-KeyCorridorS3R1-v0`
- `MiniGrid-KeyCorridorS3R2-v0`
- `MiniGrid-KeyCorridorS3R3-v0`
- `MiniGrid-KeyCorridorS4R3-v0`
- `MiniGrid-KeyCorridorS5R3-v0`
- `MiniGrid-KeyCorridorS6R3-v0`

## Unlock environment

The agent has to open a locked door. This environment can be solved without
relying on language.

```{figure} ../_static/img/figures/Unlock.png
   :alt: Figure of the unlock environment
   :width: 200
```

Registered configurations:
- `MiniGrid-Unlock-v0`

## Unlock pickup environment

The agent has to pick up a box which is placed in another room, behind a
locked door. This environment can be solved without relying on language.

```{figure} ../_static/img/figures/UnlockPickup.png
   :alt: Figure of the unlock pickup environment
   :width: 250
```
Registered configurations:
- `MiniGrid-UnlockPickup-v0`

## Blocked unlock pickup environment

The agent has to pick up a box which is placed in another room, behind a
locked door. The door is also blocked by a ball which the agent has to move
before it can unlock the door. Hence, the agent has to learn to move the ball,
pick up the key, open the door and pick up the object in the other room.
This environment can be solved without relying on language.

```{figure} ../_static/img/figures/BlockedUnlockPickup.png
   :alt: Figure of the blocked-unlock-pickup environment
   :width: 250
```

Registered configurations:
- `MiniGrid-BlockedUnlockPickup-v0`

## Obstructed maze environment

The agent has to pick up a box which is placed in a corner of a 3x3 maze.
The doors are locked, the keys are hidden in boxes and doors are obstructed
by balls. This environment can be solved without relying on language.

```{figure} ../_static/img/figures/ObstructedMaze-1Dl.png
   :width: 250
```
```{figure} ../_static/img/figures/ObstructedMaze-1Dlh.png
   :width: 250
```
```{figure} ../_static/img/figures/ObstructedMaze-1Dlhb.png
   :width: 250
```
```{figure} ../_static/img/figures/ObstructedMaze-2Dl.png
   :width: 100
```
```{figure} ../_static/img/figures/ObstructedMaze-2Dlh.png
   :width: 100
```
```{figure} ../_static/img/figures/ObstructedMaze-2Dlhb.png
   :width: 100
```
```{figure} ../_static/img/figures/ObstructedMaze-1Q.png
   :width: 250
```
```{figure} ../_static/img/figures/ObstructedMaze-2Q.png
   :width: 250
```
```{figure} ../_static/img/figures/ObstructedMaze-4Q.png
   :width: 250
```

Registered configurations:
- `MiniGrid-ObstructedMaze-1Dl-v0`
- `MiniGrid-ObstructedMaze-1Dlh-v0`
- `MiniGrid-ObstructedMaze-1Dlhb-v0`
- `MiniGrid-ObstructedMaze-2Dl-v0`
- `MiniGrid-ObstructedMaze-2Dlh-v0`
- `MiniGrid-ObstructedMaze-2Dlhb-v0`
- `MiniGrid-ObstructedMaze-1Q-v0`
- `MiniGrid-ObstructedMaze-2Q-v0`
- `MiniGrid-ObstructedMaze-Full-v0`
__author__ = "Feng Gu"
__email__ = "contact@fenggu.me"

import re
import os
from functools import reduce

import numpy as np
from tqdm import tqdm
from utils import kill_strs, trim

import gymnasium as gym

from gym.envs.registration import registry

LAYOUT = "env"

pattern = re.compile(r"(?<!^)(?=[A-Z])")

all_envs = list(registry.values())

filtered_envs_by_type = {}

# Obtain filtered list
for env_spec in tqdm(all_envs):
    # gym_minigrid.envs:Env
    split = env_spec.entry_point.split(".")
    # ignore gymnasium.envs.env_type:Env
    env_module = split[0]
    if env_module != "gym_minigrid":
        continue

    env_name = split[1]
    filtered_envs_by_type[env_name] = env_spec


filtered_envs = {k.split(':')[1] : v for k, v in sorted(filtered_envs_by_type.items(), key=lambda item: item[1].entry_point.split(".")[1])}

for env_name, env_spec in filtered_envs.items():
    made = env_spec.make()

    docstring = trim(made.unwrapped.__doc__)

    pascal_env_name = env_spec.id.split("-")[1]
    snake_env_name = pattern.sub("_", pascal_env_name).lower()
    title_env_name = snake_env_name.replace("_", " ").title()

    v_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "source",
            "environments",
            snake_env_name + ".md",
        )

    front_matter = f"""---
AUTOGENERATED: DO NOT EDIT FILE DIRECTLY
title: {title_env_name}
---
"""
    title = f"# {title_env_name}"

    if docstring is None:
        docstring = "No information provided"
    all_text = f"""{front_matter}

{title}

{docstring}
"""
    file = open(v_path, "w+", encoding="utf-8")
    file.write(all_text)
    file.close()

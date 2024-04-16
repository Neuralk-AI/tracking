import os, re
import json
import yaml
import numpy as np
import pandas as pd


def load(path):
    """Load file."""
    _, file_extension = os.path.splitext(path)
    if file_extension.lower() == ".json":
        with open(path, "r") as json_file:
            data = json.load(json_file)
    elif file_extension.lower() in [".yml", ".yaml"]:
        with open(path, "r") as yaml_file:
            data = yaml.safe_load(yaml_file)
    elif file_extension.lower() == ".txt":
        with open(path, "r") as text_file:
            data = text_file.readlines()
    elif file_extension.lower() == ".csv":
        with open(path, "r") as csv_file:
            data = pd.read_csv(csv_file)
    elif file_extension.lower() == ".npy":
        with open(path, "r") as numpy_file:
            data = np.load(numpy_file)
    return data


def save(path, data):
    """Save file."""
    _, file_extension = os.path.splitext(path)
    if file_extension.lower() == ".json":
        with open(path, "w") as json_file:
            json.dump(data, json_file)
    elif file_extension.lower() in [".yml", ".yaml"]:
        with open(path, "w") as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
    elif file_extension.lower() == ".txt":
        with open(path, "w") as text_file:
            text_file.write(data)
    elif file_extension.lower() == ".csv":
        with open(path, "w") as csv_file:
            data.to_csv(csv_file)
    elif file_extension.lower() == ".npy":
        with open(path, "w") as numpy_file:
            np.save(numpy_file, data)


def fill_args(string, **kwargs):
    pattern = r"\{([^}]*)\}"
    matches = re.findall(pattern, string)
    for key in matches:
        if key in kwargs:
            string = string.replace("{" + key + "}", kwargs[key])
    return string

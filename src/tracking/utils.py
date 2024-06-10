import json
import csv
import yaml
import uuid
import time
import os, re
import inspect
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
            data = [item.strip("\n") for item in data]
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
    pattern = "\{(?:" + "|".join(kwargs.keys()) + ")\}"
    matches = re.findall(pattern, string)
    for key in matches:
        if str(kwargs[key[1:-1]]) != "None":
            string = string.replace(key, str(kwargs[key[1:-1]]))
    return string


def add_row_to_csv(file_path, row_data):
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row_data)


def save_list_to_file(lst, file_path):
    # Extract directory from the file path
    directory = os.path.dirname(file_path)

    # Create the directory if it doesn't exist
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Write list content to the file
    with open(file_path, "w") as file:
        for item in lst:
            file.write(str(item) + "\n")


def read_list_from_file(file_path):
    # Initialize an empty list to store the content
    content_list = []

    # Read the file and append each line to the list
    with open(file_path, "r") as file:
        for line in file:
            content_list.append(line.strip())

    return content_list


def add_line_to_file(file_path, line):
    with open(file_path, "a") as file:
        if type(line) == str:
            file.write(line + "\n")
        elif type(line) == list:
            for l in line:
                file.write(l + "\n")
        else:
            file.write(str(line) + "\n")


def filter_args(func, d):
    """Filter dictionary keys to match the function arguments.
    Arguments:
        - func: function
        - d: dict
    Returns:
        - args: dict
    """
    keys = inspect.getfullargspec(func).args
    args = {key: d[key] for key in keys if (key != "self" and key in d.keys())}
    return args


def check_folder(path):
    """Create adequate folders if necessary.
    Args:
        - path: str
    """
    try:
        if not os.path.isdir(path):
            check_folder(os.path.dirname(path))
            os.mkdir(path)
    except:
        pass


def set_reproducible(seed: int):
    """Set all seeds for reproducible experiments."""
    import os
    import random
    import numpy as np
    import torch

    # Set PYTHONHASHSEED environment variable
    os.environ["PYTHONHASHSEED"] = "42"

    # Set seeds for reproducibility
    random.seed(42)
    np.random.seed(42)
    torch.manual_seed(42)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(42)
        torch.cuda.manual_seed_all(42)  # if you are using multi-GPU
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    try:
        import tensorflow as tf

        tf.random.set_seed(42)
    except:
        print("Couldn't import tensorflow. Ignored.")


def create_uuid(anything: str = "", include_time=True) -> str:
    """Create a unique uuid from timestamp and optional input string."""
    if include_time:
        return str(
            uuid.uuid5(uuid.NAMESPACE_DNS, str(time.time()) + "-" + str(anything))
        )
    else:
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, str(anything)))

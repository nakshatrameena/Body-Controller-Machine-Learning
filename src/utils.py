import csv
import os
import numpy as np


def save_to_csv(filename, data, label):
    """
    Save hand landmark data to CSV.

    Supports:
    - Flat list of 42 values
    - List of (x, y) points

    Args:
        filename (str): CSV file path
        data (list): landmark data
        label (str): gesture label
    """

    # -------------------------------
    # Ensure directory exists
    # -------------------------------
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # -------------------------------
    # Convert data to flat list
    # -------------------------------
    if isinstance(data[0], list) or isinstance(data[0], tuple):
        # Convert [[x,y], [x,y]] → flat list
        flat_data = [val for point in data for val in point]
    else:
        # Already flat
        flat_data = data

    # -------------------------------
    # Validate length
    # -------------------------------
    if len(flat_data) != 42:
        print(f"❌ Invalid data length: {len(flat_data)} (expected 42)")
        return

    # -------------------------------
    # Save row
    # -------------------------------
    row = flat_data + [label]

    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
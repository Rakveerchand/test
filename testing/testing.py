import json

import argparse
from pathlib import Path

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


def _testing(args):
    data = {'x_train': 1,
            'y_train': 2,
            'x_test': 3,
            'y_test': 4}

    # Creates a json object based on `data`
    data_json = json.dumps(data)

    # Saves the json object into a file
    with open(args.data, 'w') as out_file:
        json.dump(data_json, out_file)


if __name__ == '__main__':
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str)

    args = parser.parse_args()

    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)

    _testing(args)

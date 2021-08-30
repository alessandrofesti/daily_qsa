import sys
import os

import argparse
import configparser
from datetime import datetime
import pandas as pd
import numpy as np
import pickle
import json
import feather
import plotly.graph_objects as go
import webbrowser
import glob
import time
from typing import Union
from datetime import date
import pdb
from line_profiler import LineProfiler


def load_file(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.feather'):
        return feather.read_dataframe(file_path)
    elif file_path.endswith('.pickle'):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    elif file_path.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)
    elif file_path.endswith('.zip'):
        return pd.read_csv(file_path, compression='zip', sep=';')
    else:
        print('file ext not recongized')


def write_file(data, file_path):
    if file_path.endswith('.csv'):
        data.to_csv(file_path, index=False)
    elif file_path.endswith('.xlsx'):
        data.to_excel(file_path, index=False)
    elif file_path.endswith('.feather'):
        feather.write_dataframe(data, file_path)
    elif file_path.endswith('.pickle'):
        pickle.dump(data, open(file_path, 'wb'))
    elif file_path.endswith('.zip'):
        data.to_csv(file_path, index=False, compression='zip')
    else:
        print('file ext not recognized')


def configparser_set(file_config):
    # parse config arguments
    Config = configparser.ConfigParser()
    Config.read(file_config)
    return Config


def write_configparser_set(file_config, elapsed_time):
    # read config
    Config = configparser.ConfigParser()
    Config.read(file_config)
    # Add date and elapsed time
    Config['GENERAL']['Date'] = str(datetime.now())
    Config['GENERAL']['elapsed_time'] = f'{elapsed_time} seconds'
    # write it
    with open('configfile.ini', 'w') as configfile:
        Config.write(configfile)


def do_profile(follow=[]):
    def inner(func):
        def profiled_func(*args, **kwargs):
            try:
                profiler = LineProfiler()
                profiler.add_function(func)
                for f in follow:
                    profiler.add_function(f)
                profiler.enable_by_count()
                return func(*args, **kwargs)
            finally:
                profiler.print_stats()
        return profiled_func
    return inner





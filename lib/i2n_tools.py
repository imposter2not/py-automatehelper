#! python3
"""
i2n-tools.py
"""


def get_time_name():
    return time.strftime("%Y%m%d-%H%M%S", time.localtime())


def get_next_name(file_name):
# check the folder for existing filename, if exists, bump up and try again

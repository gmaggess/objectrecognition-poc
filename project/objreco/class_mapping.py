import json
import logging
import os
import pprint

__CLASS_MAPPING = 'class_mapping.json'


def __get_mapping():
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    return os.path.join(script_dir, __CLASS_MAPPING)


def add_class(clazz):
    data = get_classes()
    total = len(data)
    data[clazz] = total
    logging.debug('New mapping: ' + pprint.pformat(data))
    with open(__get_mapping(), 'w') as outfile:
        json.dump(data, outfile)
    return total


def total_classes():
    data = get_classes()
    return data.length


def get_classes():
    return json.load(open(__get_mapping(), 'r'))

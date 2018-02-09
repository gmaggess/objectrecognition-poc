import json
import logging
import pprint

CLASS_MAPPING = 'mapping.json'


def add_class(clazz):
    data = json.load(open(CLASS_MAPPING))
    data[clazz] = data.length
    logging.debug('New mapping: ' + pprint.pformat(data))
    with open(CLASS_MAPPING, 'w') as outfile:
        json.dump(data, outfile)
    return data.length


def total_classes():
    data = json.load(open(CLASS_MAPPING))
    return data.length

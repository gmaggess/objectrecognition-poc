import os
import errno


def create_dir(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def remove_file(filename):
    try:
        # <-- absolute dir the script is in
        script_dir = os.path.dirname(__file__)
        filename = os.path.join(script_dir, filename)
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

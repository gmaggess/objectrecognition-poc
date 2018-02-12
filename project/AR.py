from objreco.class_mapping import add_class, total_classes, get_classes
from objreco.pickle_images import convert_images
from util.file_manager import create_dir, remove_file
from util.resize_image import resize_images
from util.video_transformer import video_to_image
import argparse
import logging
import os
import shutil
import sys

OUTPUT_DIR = 'bin/'
DATA_DIR = OUTPUT_DIR + 'data/'
DATA_FILE = DATA_DIR + 'data.pkl'
DEST_DIR = OUTPUT_DIR + 'target/'
MODEL_DIR = 'project/model/'
SOURCE_DIR = OUTPUT_DIR + 'images/'

IMAGE_HEIGHT = 28
IMAGE_WIDTH = 28
FRAME_RATE = 10

STEPS = 100


def reset():
    try:
        shutil.rmtree(OUTPUT_DIR)
    except:
        logging.warning(OUTPUT_DIR + ' directory not found')


def train(video, image_width=IMAGE_WIDTH, image_height=IMAGE_HEIGHT, steps=100):
    create_dir(DATA_DIR)
    if video:
        clazz = video_to_image(video, SOURCE_DIR, FRAME_RATE)
        add_class(clazz)
        create_dir(DEST_DIR)
        resize_images(SOURCE_DIR + clazz + '/', DEST_DIR,
                      image_width, image_height)
    convert_images(DEST_DIR, get_classes(), DATA_FILE)
    print '******** TOTAL CLASSES: ' + str(total_classes())
    os.system(' python project/objreco/multi_classifier.py --mode train --classes ' + str(total_classes()) +
              ' --steps ' + str(steps) + ' --model_dir=' + MODEL_DIR + ' --data_set=' + DATA_FILE)


def evaluate():
    os.system('python project/objreco/multi_classifier.py --mode eval --classes ' + str(total_classes()) +
              ' --model_dir=' + MODEL_DIR + ' --data_set=' + DATA_FILE)


def infer(target):
    os.system('python project/objreco/multi_classifier.py --mode infer --classes ' + str(total_classes()) +
              ' --model_dir=' + MODEL_DIR + ' --img_file ' + target)


def main():
    '''Main function'''
    mode = FLAGS.mode
    video = FLAGS.video
    img_w = FLAGS.img_w
    img_h = FLAGS.img_h
    steps = FLAGS.steps
    img_file = FLAGS.img_file

    if mode == 'train':
        train(video, img_w, img_h, steps)
    elif mode == 'eval':
        evaluate()
    elif mode == 'infer':
        infer(img_file)
    elif mode == 'reset':
        reset()
    else:
        sys.stdout = 'Wrong arguments'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--mode',
        type=str,
        required=True,
        choices=['train', 'eval', 'infer', 'reset'],
        help="""\
        Mode to run the script.\
        Train - trains a new model based on the provided --data_set.\
        Eval - evaluates the trained model accurancy based on the provided --data_set.\
        Infer - infer an image, --img_file, based on the saved model.\
        """
    )
    parser.add_argument(
        '--img_w',
        type=int,
        required=False,
        default=28,
        help="""\
        The new image width\
        """
    )
    parser.add_argument(
        '--img_h',
        type=int,
        required=False,
        default=28,
        help="""\
        The new image height\
        """
    )
    parser.add_argument(
        '--steps',
        type=str,
        required=False,
        default='./',
        help="""\
        Number of training steps to train the model. If not provided defaults to 500\
        """
    )
    parser.add_argument(
        '--video',
        type=str,
        required=False,
        help="""\
        Video used as training resource. Required if --mode is train\
        """
    )
    parser.add_argument(
        '--img_file',
        type=str,
        required=False,
        help="""\
        Image to be inferred. Required if --mode is infer\
        """
    )
    FLAGS, _ = parser.parse_known_args()
    main()

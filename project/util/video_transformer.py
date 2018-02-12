import argparse
import cv2
import errno
import logging
import os
from os.path import basename

IMAGE_EXT = '.jpg'


def __create_directory(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def __get_filename(path):
    filename = os.path.splitext(path)[0]
    return basename(filename)


def video_to_image(path, output_dir, rate):
    vidcap = cv2.VideoCapture(path)
    success, image = vidcap.read()
    count = 0
    total = 1
    success = True
    clazz = __get_filename(path)
    directory = output_dir + clazz
    __create_directory(directory)
    while success:
        success, image = vidcap.read()
        if (divmod(count, rate)[1] == 0):
            cv2.imwrite(directory + "/" + str(clazz) + "_" +
                        str(total) + IMAGE_EXT, image)     # save frame as JPEG file
            logging.debug('Read frame ' + str(total) + ': ' + str(success))
            total += 1
        count += 1

    return clazz


def main():
    '''Main function'''
    image_path = FLAGS.file
    frame_rate = FLAGS.rate
    video_to_image(image_path, frame_rate)


if __name__ == '__main__':
    # args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description='Convert video to several images')
    parser.add_argument(
        '--file',
        type=str,
        required=True,
        default='./',
        help="""\
        Video file\
        """
    )
    parser.add_argument(
        '--rate',
        type=int,
        required=False,
        default=10,
        help="""\
        Frame rate. Default value: 10\
        """
    )
    FLAGS, _ = parser.parse_known_args()
    main()

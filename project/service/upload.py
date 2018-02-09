import logging
from werkzeug.utils import secure_filename
from os.path import join

UPLOAD_FOLDER = 'tmp/uploads'
ALLOWED_VIDEOS = set(['mp4'])
ALLOWED_IMAGES = set(['jpg'])


def upload_image(request):
    return __upload_file(request.files, ALLOWED_IMAGES)


def upload_video(request):
    return __upload_file(request.files, ALLOWED_VIDEOS)


def __allowed_file(filename, file_type):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in file_type


def __upload_file(files, file_type):
    # check if the post request has the file part
    if 'file' not in files:
        logging.error('No file part')
        raise ValueError('No file part')

    file = files['file']

    if file.filename == '':
        logging.error('No file has bee uploaded')
        raise ValueError('No file has bee uploaded')

    if file and __allowed_file(file.filename, file_type):
        filename = secure_filename(file.filename)
        file.save(join('UPLOAD_FOLDER', filename))
    else:
        raise ValueError('File not allowed')

    return True

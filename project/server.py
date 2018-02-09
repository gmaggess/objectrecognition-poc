from flask import Flask, request, make_response
from service.upload import upload_image, upload_video

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'tmp/uploads'
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'mp4'])


@app.route('/')
def index():
    return 'Please refer to /upload to upload videos and /infer for image recognition'


@app.route('/upload', methods=['POST'])
def upload():
    response = make_response()
    try:
        upload_video(request)
        response.headers['Content-Type'] = 'application/json'
        response.data = '{ "status": "ok" }'
    except ValueError as e:
        response.headers['Content-Type'] = 'application/json'
        response.data = '{ "status": "fail", "message": "' + e.message + '" }'

    return response


@app.route('/infer')
def infer():
    response = make_response()
    try:
      upload_image(request)
      response.headers['Content-Type'] = 'application/json'
      response.data = '{ "status": "ok" }'
    except ValueError as e:
        response.headers['Content-Type'] = 'application/json'
        response.data = '{ "status": "fail", "message": "' + e.message + '" }'

    return response


if __name__ == '__main__':
    app.run()

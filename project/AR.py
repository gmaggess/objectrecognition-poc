from flask import Flask
from service.file_upload import upload

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def index():
  return 'Please refer to /upload to upload videos and /recognition for image recognition'

@app.route('/upload', methods=['POST'])
def upload():
  try:
    return upload(request)
  except:
    return 'Invalid file'

@app.route('/infer')
def infer():
  return 'infer photo'

if __name__=='__main__':
  app.run()

UPLOAD_FOLDER = 'tmp/uploads'
ALLOWED_EXTENSIONS = set(['jpg', 'mp4'])

def allowed_file(filename):
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def upload(request):
  # check if the post request has the file part
  if 'file' not in request.files:
      flash('No file part')
      return 'fail'
  file = request.files['file']
  # if user does not select file, browser also
  # submit a empty part without filename
  if file.filename == '':
      flash('No selected file')
      return 'fail'
  if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  return 'ok'

from flask import Flask, request, send_file
from main import do_everything  # Assuming you have a module for compression

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file and allowed_file(file.filename):
        # Call your compression function
        output = do_everything(file)
        return send_file(output, as_attachment=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'pdf'}

if __name__ == '__app__':
    app.run()

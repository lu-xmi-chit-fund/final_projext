
from flask import *
import os

UPLOAD_FOLDER = 'C:/Users/Abhijeet/Desktop/Development/python/final project/uploads'


app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def upload_file():
    uploaded_file=request.files.get('file')
    if uploaded_file.filename!='':
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
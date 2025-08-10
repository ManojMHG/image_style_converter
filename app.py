from flask import Flask, render_template, request
import os
import cv2
from utils.image_styles import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

STYLE_FUNCTIONS = {
    'black_white': black_white,
    'sketch': sketch,
    'cartoon': cartoon,
    'sepia': sepia,
    'inverted': inverted,
    'hdr': hdr,
    'oil_painting': oil_painting,
    'pencil_color': pencil_color,
    'ghibli_style': ghibli_style,
    'neural_style': neural_style
}

@app.route('/', methods=['GET', 'POST'])
def index():
    output_image = None
    if request.method == 'POST':
        style = request.form['style']
        file = request.files['image']
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        img = cv2.imread(filepath)
        img = cv2.resize(img, (500, 500))

        processed = STYLE_FUNCTIONS[style](img)
        out_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
        cv2.imwrite(out_path, processed)
        output_image = 'output.png'

    return render_template('index.html', output_image=output_image)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment
    app.run(host="0.0.0.0", port=port, debug=True)
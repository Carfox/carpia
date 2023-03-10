from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import modelo as modelo
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        file.save(secure_filename('image.jpg'))
        #pred = modelo.process_image()
    return 'Imagen Recibida'





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6400)

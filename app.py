from flask import Flask, request, render_template
#import modelo
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("/home/adminaz/Desktop/rpi/index.html")


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    file.save('image.jpg')
    #pred = modelo.process_image()
    return 'Imagen Recibida'





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6400)

from flask import Flask, render_template, request

from faces import detect_face

app = Flask(__name__)


@app.route('/', methods=['GET'])
def start():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    imagefile1 = request.files['imagefile1']
    imagefile2 = request.files['imagefile2']

    image_path1 = "./images/" + imagefile1.filename
    imagefile1.save(image_path1)

    image_path2 = "./images/" + imagefile2.filename
    imagefile2.save(image_path2)

    results = detect_face(image_path1, image_path2)

    return render_template('index.html', prediction=results)


if __name__ == '__main__':
    app.run(port=3000, debug=False)
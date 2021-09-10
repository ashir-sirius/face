from flask import Flask, render_template, request

from faces import detect_face

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def predict():
    
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        imagefile1 = request.files['imagefile1']
        imagefile2 = request.files['imagefile2']

        image_path1 = "./images/" + imagefile1.filename
        imagefile1.save(image_path1)

        image_path2 = "./images/" + imagefile2.filename
        imagefile2.save(image_path2)

        files = request.files.getlist("images")
    
        results = detect_face(image_path1, image_path2)
    
        print(results)
    
        return render_template('index.html', prediction=results)


if __name__ == '__main__':
    app.run(port=3000, debug=False)
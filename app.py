from flask import Flask, render_template, request, send_file
import cv2
import os
from cartoon import cartoonize

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(RESULT_FOLDER, "cartoon_" + file.filename)

        file.save(input_path)

        img = cv2.imread(input_path)
        cartoon = cartoonize(img)
        cv2.imwrite(output_path, cartoon)

        return render_template(
            "index.html",
            original=input_path,
            result=output_path
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

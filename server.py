from flask import Flask,request
from thumbnail_maker import image_converter
import sys

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def resize_image():
    try:
        original_file = request.form.get('image')
        resized_image_data = image_converter(original_file)

        return resized_image_data

    except Exception as err:
        pass


if __name__ == '__main__':
    app.run(host="localhost", port=5000)

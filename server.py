from flask import Flask, request, jsonify
from thumbnail_maker import image_converter
from flask_executor import Executor, executor


app = Flask(__name__)
executor = Executor(app)

@app.route('/image', methods=['POST'])
def resize_image():
    try:
        original_file = request.form.get('image')
        executor.submit_stored('image_converter', image_converter, original_file)

        return jsonify({'result':'success'})

    except Exception as err:
        print(err)

@app.route('/result', methods=['GET'])
def get_image():
    try:
        if not executor.futures.done('image_converter'):
            future_status = executor.futures._state('image_converter')
            return jsonify({'status': future_status})
        future = executor.futures.pop('image_converter')
        return future.result()

    except Exception as err:
        print(err)

if __name__ == '__main__':
    app.run(host="localhost", port=5000)

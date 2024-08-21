from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import os
import logging

app = Flask(__name__)

@app.route('/api/endpoint', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('test.jpg')
        img = np.array(Image.open('test.jpg'))
        return jsonify({'message': f'File uploaded successfully, {img.shape}'})

@app.route('/api/get', methods=['GET'])
def handle_get_request():
    # data = request.get_json()
    # print(data)
    return 'HELLO THERE OKK!!!!!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
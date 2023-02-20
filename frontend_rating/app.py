import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def predict():
    """
    Return the anime rating prediction based on its information input
    """
    if request.method == 'POST':

        data = {
            'title':request.form.get('title'),
            'synopsis':request.form.get('synopsis'),
            'type': request.form.get('media'),
            'genders': request.form.getlist('genres'),
            'producers': request.form.getlist('producers'),
            'studio': request.form.getlist('studio')
        }
        
        response = requests.post('http://localhost:5000/', json=data)
        return render_template('result.html', result=response.json()["rating"])
    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.run(port=5001)
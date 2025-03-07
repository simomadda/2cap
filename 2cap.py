# https://github.com/2captcha/2captcha-python

import sys
import os
import random
import time
from flask import Flask, jsonify

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

app = Flask(__name__)

api_key = 'e5a8b13cd265750003893f8186c44728'
solver = TwoCaptcha(api_key)

@app.route('/get_recaptcha_token', methods=['GET'])
def get_recaptcha_token():
    try:
        result = solver.recaptcha(
            sitekey='6Leioo4nAAAAAMcu1LhvJ0m2W3ccS-zSw3E4yUMz',
            url='https://app.flouci.com/',
            invisible=1,
            enterprise=1,
            version='v3',
            score=0.9,
        )
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/time', methods=['GET'])
def time_endpoint():
    return jsonify({
        'generated_session_pre_reg': random.randint(0, 1000000000) + int(time.time() * 1000)
    })

if __name__ == '__main__':
    app.run(debug=True)
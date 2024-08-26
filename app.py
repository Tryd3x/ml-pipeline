from flask import Flask
from src.logger import logging
from src.exception import CustomException
import sys

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    try:
        logging.info('User tried to access the homepage')
        raise Exception("Testing CustomException handler")
    except Exception as e:
        logging.info(CustomException(e,sys).error_message)
        return "Hello! World!"

if __name__ == '__main__':
    app.run(debug=True)
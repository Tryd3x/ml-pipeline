from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    logging.info('User accessed the homepage')
    return "Hello, world!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
import pytz
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def get_time():
    tz = pytz.timezone('US/Eastern')
    current_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z")
    return "Current time: " + current_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)

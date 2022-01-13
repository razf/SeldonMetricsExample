from time import sleep

import numpy as np
from flask import Flask
from prometheus_client import Histogram

h = Histogram("pred_runtime" "Runtime of prediction")
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict_raw():
    sleep_time = abs(np.random.normal(loc=1))
    sleep(sleep_time)
    h.observe(sleep_time)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8890)

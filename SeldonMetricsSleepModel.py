from time import sleep

import numpy as np



class SeldonMetricsSleepModel:
    def predict_raw(self, X):
        sleep_time = abs(np.random.normal(loc=1))
        sleep(sleep_time)
        return {
            "meta":
                {"metrics":
                     {"type": "TIMER", "key": "pred_runtime", "value": sleep_time}
                 },
            "data": X
        }



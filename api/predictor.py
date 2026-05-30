import numpy as np
import joblib
import os
from .defaults import DEFAULT_FEATURES


model_path = os.path.join(os.path.dirname(__file__), '../models/cat_model.joblib')

class Predictor:
    def __init__(self):
        self.model = joblib.load(model_path)
        self.feature_names = DEFAULT_FEATURES.keys()
    
    def predict(self, data: dict):
        features = []
        for name in self.feature_names:
            if name in data:
                features.append(data[name])
            else:
                features.append(DEFAULT_FEATURES.get(name, 0))
        
        X = np.array(features).reshape(1, -1)
        proba = self.model.predict_proba(X)[0, 1]
        return proba

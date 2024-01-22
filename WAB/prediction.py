import numpy as np

def predict_classes(model, x):
    predictions = model.predict(x)
    return np.argmax(predictions, axis=1)

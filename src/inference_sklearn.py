import pickle    
import pandas as pd
from util import *

def encode_to_label(sample):
    filename = f'../decision_trees_sklearn/label_encoder/label_encoders.pkl'
    label_encoders = pickle.load(open(filename, 'rb'))

    encoded_data = {}
    for attribute, value in sample.items():
        if attribute  == 'age':
            value = age_to_class(value)
        elif attribute  == 'bmi':
            value = bmi_to_class(value)
        
        encoded_data[attribute] = label_encoders[attribute].transform([value])
    return pd.DataFrame(encoded_data)

def infer(sample):
    predicted = {}
    for attribute in ["proteins", "carbohydrates", "fats", "calcium", "vitamin_a", "vitamin_c", "calories"]:
        filename = f'../decision_trees_sklearn/models/{attribute}.pkl'
        clf = pickle.load(open(filename, 'rb'))

        # Make a prediction using the trained model
        prediction = clf.predict(sample)
        predicted[attribute] = prediction[0]

    return convert_to_ranges(predicted)

    

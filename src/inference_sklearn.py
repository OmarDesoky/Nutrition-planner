import pickle    
# import pandas as pd
from util import *



# sample = pd.DataFrame({
#     "age": label_encoders["age"].transform(["twenties"]),
#     "gender": label_encoders["gender"].transform(["male"]),  # 1 = Male, 0 = Female
#     "bmi": label_encoders["bmi"].transform(["normal"]),
#     "metabolic rate": label_encoders["metabolic rate"].transform(["high"]),  # 0 = very low, 1 = low, 2 = mid, 3 = high, 4 = very high
#     "physical activity intensity": label_encoders["physical activity intensity"].transform(["low"]),  # 0 = very low, 1 = low, 2 = mid, 3 = high, 4 = very high
#     "blood pressure": label_encoders["blood pressure"].transform(["normal"]),  # 0 = hypotension, 1 = normal, 2 = hypertension
#     "diabetic": label_encoders["diabetic"].transform(["normal"]),  # 0 = normal, 1 = high, 2 = severely high
#     "heart disease": label_encoders["heart disease"].transform(["false"]),  # 0 = no, 1 = yes
#     "anemia": label_encoders["anemia"].transform(["normal"]),  # 0 = normal, 1 = abnormal, 2 = severely abnormal
#     "lactose intolerance": label_encoders["lactose intolerance"].transform(["normal"]),  # 0 = normal, 1 = abnormal
#     "nutrition goal": label_encoders["nutrition goal"].transform(["gain weight"]),  # 0 = gain weight, 1 = lose weight, 2 = maintain weight, 3 = gain muscle, 4 = gain endurance
# })

def encode_to_label(sample):
    print(sample)
    filename = f'../decision_trees_sklearn/label_encoder/label_encoders.pkl'
    label_encoders = pickle.load(open(filename, 'rb'))
    # breakpoint()
    encoded_data = {}
    for attribute in sample:
        # print(attribute)
        if attribute  == 'age':
            encoded_data['age'] = age_to_class(sample['age'])
        elif attribute  == 'bmi':
            encoded_data['bmi'] = bmi_to_class(sample['bmi'])
        else:
            encoded_data[attribute] = num_to_label(attribute, sample[attribute]) 
        # encoded_data[attribute] = label_encoders[attribute].transform[sample[attribute]]
    return encoded_data

def infer(sample):
    predicted = {}
    for attribute in ["proteins", "carbohydrates", "fats", "calcium", "vitamin_a", "vitamin_c", "calories"]:
        filename = f'../decision_trees_sklearn/models/{attribute}.pkl'
        clf = pickle.load(open(filename, 'rb'))

        # Make a prediction using the trained model
        prediction = clf.predict(sample)
        predicted[attribute] = prediction[0]

    return convert_to_ranges(predicted)

    

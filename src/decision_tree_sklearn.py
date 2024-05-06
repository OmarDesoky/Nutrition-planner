import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle
from util import *

# Load the data sample
data = pd.read_csv('../data/data_gpt.csv')

# Convert columns to lowercase
data.columns = data.columns.str.lower()

y = data[["proteins","carbohydrates","fats","calcium","vitamin_a","vitamin_c","calories"]]

data['age'] = data['age'].apply(age_to_class)
data['bmi'] = data['bmi'].apply(bmi_to_class)
for attribute in y.columns:
    data[attribute] = data[attribute].apply(lambda row: num_to_label(attribute, row))

# Convert rows to lowercase
data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# # Define the feature columns
X = data[["age","gender","bmi","metabolic rate","physical activity intensity","blood pressure","diabetic","heart disease", "anemia", "lactose intolerance","nutrition goal"]]

label_encoders = {}

for attribute in X.columns:
   label_encoders[attribute] = LabelEncoder()
   X[attribute] = label_encoders[attribute].fit_transform(X[attribute])

# save the label encoders to disk
filename = f'../decision_trees_sklearn/label_encoder/label_encoders.pkl'
pickle.dump(label_encoders, open(filename, 'wb'))

for attribute in y.columns:
    # Define the target column
    y = data[attribute]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a DecisionTreeClassifier object with the ID3 algorithm
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=9)

    # Train the model on the training data
    clf.fit(X_train, y_train)

    # Evaluate the model on the testing data
    accuracy = clf.score(X_test, y_test)
    print(attribute, "accuracy:", accuracy)

    # save the model to disk
    filename = f'../decision_trees_sklearn/models/{attribute}.pkl'
    pickle.dump(clf, open(filename, 'wb'))
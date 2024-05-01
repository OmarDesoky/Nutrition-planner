import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def age_to_class(age):
    try:
        age = int(age)
        if age < 20:
            return 'teens'
        elif age < 30:
            return 'twenties'
        elif age < 40:
            return 'thirties'
        elif age < 50:
            return 'forties'
        elif age < 60:
            return 'fifties'
        elif age < 70:
            return 'sixties'
        else:
            return 'seventies'
    except ValueError:
        pass 

def bmi_to_class(bmi):
    try:
        bmi = int(bmi)
        if bmi < 18.5:
            return 'underweight'
        elif bmi < 24.9:
            return 'normal'
        elif bmi < 29.9:
            return 'overweight'
        elif bmi < 34.9:
            return 'obesity 1'
        elif bmi < 39.9:
            return 'obesity 2'
        else:
            return 'obesity 3'
    except ValueError:
        pass
    
def protien_to_class(protien):
    try:
        protien = int(protien)
        protien -= 50
        return int(protien//25.001)
    except ValueError:
        pass
    
# Load the data sample
data = pd.read_csv('../data/data_llama.csv')

# Convert columns to lowercase
data.columns = data.columns.str.lower()

data['age'] = data['age'].apply(age_to_class)
data['bmi'] = data['bmi'].apply(bmi_to_class)
data['proteins'] = data['proteins'].apply(protien_to_class)

# Convert rows to lowercase
data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)


# # Define the feature columns
X = data[["age","gender","bmi","metabolic rate","physical activity intensity","blood pressure","diabetic","heart disease","nutrition goal"]]
le = LabelEncoder()
X["age"] = le.fit_transform(X["age"])
X["gender"] = le.fit_transform(X["gender"])
X["bmi"] = le.fit_transform(X["bmi"])
X["metabolic rate"] = le.fit_transform(X["metabolic rate"])
X["physical activity intensity"] = le.fit_transform(X["physical activity intensity"])
X["blood pressure"] = le.fit_transform(X["blood pressure"])
X["diabetic"] = le.fit_transform(X["diabetic"])
X["heart disease"] = le.fit_transform(X["heart disease"])
# X["anemia"] = le.fit_transform(X["anemia"])
# X["lactose intolerance"] = le.fit_transform(X["lactose intolerance"])
X["nutrition goal"] = le.fit_transform(X["nutrition goal"])

print(X)
# Define the target column
y = data["proteins"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a DecisionTreeClassifier object with the ID3 algorithm
clf = DecisionTreeClassifier(criterion="entropy", max_depth=9)

# Train the model on the training data
clf.fit(X_train, y_train)

# Evaluate the model on the testing data
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)


new_sample = pd.DataFrame({
    "age": [35],
    "gender": [1],  # 1 = Male, 0 = Female
    "bmi": [25.5],
    "metabolic rate": [2],  # 0 = very low, 1 = low, 2 = mid, 3 = high, 4 = very high
    "physical activity intensity": [3],  # 0 = very low, 1 = low, 2 = mid, 3 = high, 4 = very high
    "blood pressure": [1],  # 0 = hypotension, 1 = normal, 2 = hypertension
    "diabetic": [0],  # 0 = normal, 1 = high, 2 = severely high
    "heart disease": [0],  # 0 = no, 1 = yes
    # "anemia": [0],  # 0 = normal, 1 = abnormal, 2 = severely abnormal
    # "lactose intolerance": [0],  # 0 = normal, 1 = abnormal
    "nutrition goal": [2]  # 0 = gain weight, 1 = lose weight, 2 = maintain weight, 3 = gain muscle, 4 = gain endurance
})

# Make a prediction using the trained model
prediction = clf.predict(new_sample)

print("Predicted Proteins:", prediction[0])
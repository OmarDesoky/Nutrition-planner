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
        if bmi < 20:
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

def fats_to_class(fats):
    try:
        fats = int(fats)
        fats -= 20
        return int(fats//10.001)
    except ValueError:
        pass    
    
def calcium_to_class(calcium):
    try:
        calcium = int(calcium)
        calcium -= 1100
        return int(calcium//20.001)
    except ValueError:
        pass

def carbohydrates_to_class(carbohydrates):
    try:
        carbohydrates = int(carbohydrates)
        carbohydrates -= 200
        return int(carbohydrates//30.001)
    except ValueError:
        pass

def vitamin_a_to_class(vitamin_a):
    try:
        vitamin_a = int(vitamin_a)
        vitamin_a -= 1100
        return int(vitamin_a//20.001)
    except ValueError:
        pass

def vitamin_c_to_class(vitamin_c):
    try:
        vitamin_c = int(vitamin_c)
        vitamin_c -= 700
        return int(vitamin_c//20.001)
    except ValueError:
        pass

def calories_to_class(calories):
    try:
        calories = int(calories)
        calories -= 1500
        return int(calories//300.001)
    except ValueError:
        pass

# Load the data sample
data = pd.read_csv('../data/data_gpt.csv')

# Convert columns to lowercase
data.columns = data.columns.str.lower()

data['age'] = data['age'].apply(age_to_class)
data['bmi'] = data['bmi'].apply(bmi_to_class)
data['proteins'] = data['proteins'].apply(protien_to_class)
data['calcium'] = data['calcium'].apply(calcium_to_class)
data['carbohydrates'] = data['carbohydrates'].apply(carbohydrates_to_class)
data['fats'] = data['fats'].apply(fats_to_class)
data['vitamin_a'] = data['vitamin_a'].apply(vitamin_a_to_class)
data['vitamin_c'] = data['vitamin_c'].apply(vitamin_c_to_class)
data['calories'] = data['calories'].apply(calories_to_class)
# Convert rows to lowercase
data = data.applymap(lambda x: x.lower() if isinstance(x, str) else x)


# # Define the feature columns
X = data[["age","gender","bmi","metabolic rate","physical activity intensity","blood pressure","diabetic","heart disease", "anemia", "lactose intolerance","nutrition goal"]]
le_age = LabelEncoder()
le_gender = LabelEncoder()
le_bmi = LabelEncoder()
le_metabolic_rate = LabelEncoder()
le_phy_intensity = LabelEncoder()
le_blood_pressure = LabelEncoder()
le_diabetic = LabelEncoder()
le_heart_disease = LabelEncoder()
le_anemia = LabelEncoder()
le_lactose_inol = LabelEncoder()
le_nutrition_goal = LabelEncoder()


X["age"] = le_age.fit_transform(X["age"])
X["gender"] = le_gender.fit_transform(X["gender"])
X["bmi"] = le_bmi.fit_transform(X["bmi"])
X["metabolic rate"] = le_metabolic_rate.fit_transform(X["metabolic rate"])
X["physical activity intensity"] = le_phy_intensity.fit_transform(X["physical activity intensity"])
X["blood pressure"] = le_blood_pressure.fit_transform(X["blood pressure"])
X["diabetic"] = le_diabetic.fit_transform(X["diabetic"])
X["heart disease"] = le_heart_disease.fit_transform(X["heart disease"])
X["anemia"] = le_anemia.fit_transform(X["anemia"])
X["lactose intolerance"] = le_lactose_inol.fit_transform(X["lactose intolerance"])
X["nutrition goal"] = le_nutrition_goal.fit_transform(X["nutrition goal"])


y = data[["proteins","carbohydrates","fats","calcium","vitamin_a","vitamin_c","calories"]]


new_sample = pd.DataFrame({
    "age": le_age.transform(["twenties"]),
    "gender": le_gender.transform(["male"]),  # 1 = Male, 0 = Female
    "bmi": le_bmi.transform(["normal"]),
    "metabolic rate": le_metabolic_rate.transform(["high"]),  # 0 = very low, 1 = low, 2 = mid, 3 = high, 4 = very high
    "physical activity intensity": le_phy_intensity.transform(["low"]),  # 0 = very low, 1 = low, 2 = mid, 3 = high, 4 = very high
    "blood pressure": le_blood_pressure.transform(["normal"]),  # 0 = hypotension, 1 = normal, 2 = hypertension
    "diabetic": le_diabetic.transform(["normal"]),  # 0 = normal, 1 = high, 2 = severely high
    "heart disease": le_heart_disease.transform(["false"]),  # 0 = no, 1 = yes
    "anemia": le_anemia.transform(["normal"]),  # 0 = normal, 1 = abnormal, 2 = severely abnormal
    "lactose intolerance": le_lactose_inol.transform(["normal"]),  # 0 = normal, 1 = abnormal
    "nutrition goal": le_nutrition_goal.transform(["gain muscle"]),  # 0 = gain weight, 1 = lose weight, 2 = maintain weight, 3 = gain muscle, 4 = gain endurance
})

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
    print("Accuracy:", accuracy)

    # Make a prediction using the trained model
    prediction = clf.predict(new_sample)

    print("Predicted", attribute, prediction[0])
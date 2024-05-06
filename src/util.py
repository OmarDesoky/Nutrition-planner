import json
import math
import random
import toml
from pandas import read_csv
import csv

EPS = 0.000001

def get_attributes_meta_data(filepath):
    attribute_meta_data = {}
    with open(f'../{filepath}', "r") as file:
        attribute_meta_data = toml.load(file)
    return attribute_meta_data

attributes = get_attributes_meta_data('attributes.toml')

def num_to_label(attribute_name, value):
    try:
        range_attr = attributes['range'][attribute_name]
        value = range_attr['min'] if value < range_attr['min'] else value
        value = range_attr['max'] if value > range_attr['max'] else value
        if value < range_attr['min'] or value > range_attr['max']:
            raise f'Value for attribute {attribute_name} out of range'
        value -= range_attr['min']
        precision = (range_attr['max'] - range_attr['min'])/range_attr['divisions']
        return int(value/(precision+EPS))
    except Exception as err:
        print(err)
        return None
    
def label_to_range(attribute_name, label):
    try:
        range_attr = attributes['range'][attribute_name]
        precision = (range_attr['max'] - range_attr['min'])//range_attr['divisions']
        mini = range_attr['min'] + precision*label
        maxi = mini+precision
        if mini < range_attr['min'] or maxi > range_attr['max']:
            raise f'Value for attribute {attribute_name} out of range'
        return {'min': mini, 'max': maxi}
    except Exception as err:
        print(err)
        return None

def convert_to_labels(data_row):
    for attribute_name,value in data_row.items():
        if isinstance(value, str):
            data_row[attribute_name] = value.lower()
        if attributes['range'].get(attribute_name):
            data_row[attribute_name] = num_to_label(attribute_name, value)
        if data_row[attribute_name] is None:
            print('Invalid Data Row')
    return data_row

def convert_to_ranges(data_row):
    for attribute_name,value in data_row.items():
        if isinstance(value, str):
            data_row[attribute_name] = value.lower()
        if attributes['range'].get(attribute_name):
            data_row[attribute_name] = label_to_range(attribute_name, value)
        if data_row[attribute_name] is None:
            print('Invalid Data Row')
    return data_row

def upload_data_set(file_path, shuffle = False):
    dataset = read_csv(f'../{file_path}')
    dataset.columns = dataset.columns.str.lower()
    dataset_attr = dataset.columns.tolist()
    input_attributes = [attribute for attribute in attributes['input_attributes'] if attribute in dataset_attr]
    output_attributes = [attribute for attribute in attributes['output_attributes'] if attribute in dataset_attr]
    dataset_attr = input_attributes + output_attributes
    dict_data = dataset.to_dict()
    dict_dataset = []
    for i in range(dataset.shape[0]):
        if shuffle:
            dict_dataset.append({attribute:dict_data[attribute][i] for attribute in dataset_attr})
        else:
            dict_dataset.append(convert_to_labels({attribute:dict_data[attribute][i] for attribute in dataset_attr}))
    return dict_dataset, input_attributes, output_attributes

def save_json(file_path, data):
    with open(f'../{file_path}', 'w') as json_file:
        json.dump(data, json_file)

def load_json(file_path):
    with open(f'../{file_path}', 'r') as json_file:
        json_data = json.load(json_file)
    return json_data

def shuffle_data_set(file_path):
    dataset, input_attributes, output_attributes = upload_data_set(file_path, shuffle=True)
    random.shuffle(dataset)
    keys = dataset[0].keys()
    with open(f'../{file_path}', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        for row in dataset:
            writer.writerow(row)

def validate_ui_attributes(row):
    issues= []
    for attribute, value in row.items():
        if attribute in attributes['range']:
            attr_range = attributes['range'][attribute]
            try:
                value = float(value)
            except Exception as err:
                issues.append(
                    f"Please add Integer value for attribute {attribute} in the range [{attr_range['min']},{attr_range['max']}]"
                )
                continue
            if value > attr_range['max'] or value < attr_range['min']:
                issues.append(
                    f"Please add Integer value for attribute {attribute} in the range [{attr_range['min']},{attr_range['max']}]"
                )
            else:
                row[attribute] = value
        if attribute in attributes['values']:
            if value not in attributes['values'][attribute]:
                issues.append(
                    f"Please add a value for attribute {attribute} from this set of values {attributes['values'][attribute]}"
                )
    return issues

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
    
# def protien_to_class(protein):
    try:
        protein = int(protein)
        protein -= 50
        return int(protein//25.001)
    except ValueError:
        pass

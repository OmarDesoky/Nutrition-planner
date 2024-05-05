from util import upload_data_set
from inference import infer_for_testing

def print_accuracy(dataset_name):
    data_set, input_attributes, output_attributes = upload_data_set(f'data/{dataset_name}.csv')
    data_set = data_set[int(len(data_set)*0.9):]
    output_rows = infer_for_testing(data_set, f'decision_trees/{dataset_name}.json')
    output_attributes_accuracy = { output_attribute: {"success": 0, "fail": 0} for output_attribute in output_attributes }
    for row in output_rows:
        for output_attribute in output_attributes:
            true_val = row[output_attribute]
            infered_val = row['inference'][output_attribute]
            if row[output_attribute] == row['inference'][output_attribute]:
                output_attributes_accuracy[output_attribute]["success"] += 2
            elif abs(true_val-infered_val) < 2:
                output_attributes_accuracy[output_attribute]["success"] += 1
                output_attributes_accuracy[output_attribute]["fail"] += 1
            else:
                output_attributes_accuracy[output_attribute]["fail"] += 2
    over_all_success = over_all_fail = 0
    for k,v in output_attributes_accuracy.items():
        print(f'{v["success"]} Success and {v["fail"]} Fail, Accuracy for {k} = {v["success"]/(v["success"]+v["fail"])}')
        over_all_fail += v["fail"]
        over_all_success += v["success"]
    print(f'Overall accuracy = {over_all_success/(over_all_success+over_all_fail)}, {over_all_success} Success and {over_all_fail} Fail')

print_accuracy('data_llama')
print_accuracy('data_gpt')
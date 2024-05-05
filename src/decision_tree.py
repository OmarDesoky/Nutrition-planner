from copy import deepcopy
from math import log
from util import upload_data_set, save_json, shuffle_data_set

def build_decision_trees(data_set, input_attributes, output_attributes):
    decision_trees = {}
    nodes_count = 0

    def compute_entropy(values_map, output_values_map):
        # normalize
        input_value_probability = {k:val/__builtins__.sum(values_map.values()) for k,val in values_map.items()} # P(x)
        input_value_probability_given_output_value = {
            b: { k:val/__builtins__.sum(t.values()) for k,val in t.items() } 
            for b,t in output_values_map.items()
        }
        entropy = 0
        for x, p_x in input_value_probability.items():
            sum = 0
            for y_x, p_y_x in input_value_probability_given_output_value[x].items():
                sum += p_y_x*log(p_y_x, 2)
            entropy -= p_x*sum
        return entropy

    def get_minimum_entropy_attribute(data_set, input_attributes, output_attribute):
        min_entropy = 1000000
        optimal_attribute = -1
        attribute_values_count = {attr:{} for attr in input_attributes}
        attribute_values_output_count = {attr:{} for attr in input_attributes}
        
        for row in data_set:
            for attr in input_attributes:
                value = row[attr]
                output_value = row[output_attribute]
                if not attribute_values_count[attr].get(value):
                    attribute_values_count[attr][value] = 0
                    attribute_values_output_count[attr][value] = {}
                if not attribute_values_output_count[attr][value].get(output_value):
                    attribute_values_output_count[attr][value][output_value] = 0
                attribute_values_count[attr][value] += 1
                attribute_values_output_count[attr][value][output_value] += 1
        
        for attr in input_attributes:
            attribute_entropy = compute_entropy(attribute_values_count[attr], attribute_values_output_count[attr])
            optimal_attribute = attr if attribute_entropy < min_entropy else optimal_attribute
            min_entropy = min(min_entropy, attribute_entropy)
        value_dataset_map = {}
        new_data_set = deepcopy(data_set)
        for row in new_data_set:
            value = row.pop(optimal_attribute)
            if not value_dataset_map.get(value):
                value_dataset_map[value] = []
            value_dataset_map[value].append(row)
        return optimal_attribute, value_dataset_map

    def get_dominent_output_value(data_set, output_attribute):
        output_values_map = {}
        for row in data_set:
            output_values_map[row[output_attribute]] = output_values_map.get(row[output_attribute], 0) + 1
        return max(output_values_map, key=output_values_map.get)

    def check_one_output_value(data_set, output_attribute):
        output_values_map = {}
        for row in data_set:
            output_values_map[row[output_attribute]] = output_values_map.get(row[output_attribute], 0) + 1
        return list(output_values_map.keys())[0] if len(output_values_map) == 1 else None

    def build_decision_tree(data_set, input_attributes, output_attribute, decision_tree):
        nonlocal nodes_count
        one_output_value = check_one_output_value(data_set, output_attribute)
        node = {
            'node_id': nodes_count,
            'children': {},
            'attribute': None,
            'inference': one_output_value
        }
        nodes_count += 1
        if not input_attributes:
            node['inference'] = get_dominent_output_value(data_set,output_attribute)
            decision_tree.append(node)
            return node['node_id']
        if one_output_value:
            decision_tree.append(node)
            return node['node_id']
        optimal_attribute, attr_values_datasets_map = get_minimum_entropy_attribute(
            data_set, input_attributes, output_attribute
        )
        node['attribute'] = optimal_attribute
        decision_tree.append(node)
        new_input_attributes = [attr for attr in input_attributes if attr != optimal_attribute]
        for attr_value, sub_data_set in attr_values_datasets_map.items():
            node['children'][attr_value] = build_decision_tree(
                sub_data_set,
                new_input_attributes,
                output_attribute,
                decision_tree
            )
        decision_tree[node['node_id']] = node
        return node['node_id']

    for output_attribute in output_attributes:
        decision_tree = []
        nodes_count = 0
        build_decision_tree(
            data_set=data_set, 
            input_attributes=input_attributes, 
            output_attribute=output_attribute,
            decision_tree=decision_tree
        )
        decision_trees[output_attribute] = {
            'tree': decision_tree,
            'most_freq_value': get_dominent_output_value(data_set, output_attribute)
        }
    return decision_trees

def build_trees_with_datasets(dataset_name):
    data_set, input_attributes, output_attributes = upload_data_set(f'data/{dataset_name}.csv')
    data_set = data_set[:int(len(data_set)*0.9)]
    decision_trees = build_decision_trees(data_set,input_attributes,output_attributes)
    save_json(f'decision_trees/{dataset_name}.json', decision_trees)

build_trees_with_datasets('data_llama')
build_trees_with_datasets('data_gpt')

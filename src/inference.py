from util import load_json, attributes, convert_to_ranges

def infer(row, decision_tree_path):
    decision_tree = load_json(decision_tree_path)
    out_put_attributes = attributes['output_attributes']
    output_values = {}
    for attribute in out_put_attributes:
        cur_node = 0
        while decision_tree[attribute]['tree'][cur_node]['inference'] is None:
            cur_attr = decision_tree[attribute]['tree'][cur_node]['attribute']
            if decision_tree[attribute]['tree'][cur_node]['children'].get(row[cur_attr]):
                cur_node = decision_tree[attribute]['tree'][cur_node]['children'][row[cur_attr]]
            else:
                break
        output_values[attribute] = decision_tree[attribute]['tree'][cur_node]['inference'] or decision_tree[attribute]['most_freq_value']
    return convert_to_ranges(output_values)
    
def infer_for_testing(rows, decision_tree_path):
    decision_tree = load_json(decision_tree_path)
    out_put_attributes = attributes['output_attributes']
    output_rows = []
    for row in rows:
        output_values = {}
        for attribute in out_put_attributes:
            cur_node = 0
            while decision_tree[attribute]['tree'][cur_node]['inference'] is None:
                cur_attr = decision_tree[attribute]['tree'][cur_node]['attribute']
                if decision_tree[attribute]['tree'][cur_node]['children'].get(row[cur_attr]):
                    cur_node = decision_tree[attribute]['tree'][cur_node]['children'][row[cur_attr]]
                else:
                    break
            output_values[attribute] = decision_tree[attribute]['tree'][cur_node]['inference'] or decision_tree[attribute]['most_freq_value']
        row['inference'] = output_values
        output_rows.append(row)
    return output_rows
    
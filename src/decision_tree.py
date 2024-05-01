

def compute_entropy(data):
    pass

def build_decision_trees(data_set, input_attributes, output_attributes):

    decision_trees = {}
    def build_decision_tree(data_set, input_attributes, output_attribute, decision_tree):
        pass

    for output_attribute in output_attributes:
        decision_tree = []
        build_decision_tree(
            data_set=data_set, 
            input_attributes=input_attributes, 
            output_attribute=output_attribute,
            decision_tree=decision_tree
        )
        decision_trees[output_attribute] = decision_tree
    return decision_trees
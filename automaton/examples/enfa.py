################################################################################
# ENFA examples
# ab        ==>     ab
# a|c       ==>     a_or_c
# (a|b)*c   ==>     __a_or_b__as_c
################################################################################
__a_or_b__as = {
    'symbols': {'a', 'b'},
    'states': {'1', '2', '3'},
    'initial_state': '2',
    'final_states': {'1', '2', '3'},
    'transitions': {
        '2': {'a': '1', 'b': '3'},
        '3': {'a': '1', 'b': '3'},
        '1': {'a': '1', 'b': '3'}
    }
}

__abc__as_c = {
    'symbols': {'a', 'c', 'b'},
    'states': {'1', '2', '3', '4', '5', 'e'},
    'initial_state': '2', 'final_states': {'5'},
    'transitions': {
        '2': {'b': 'e', 'a': '3', 'c': '5'},
        '5': {'b': 'e', 'a': '3', 'c': 'e'},
        'e': {'b': 'e', 'a': 'e', 'c': 'e'},
        '3': {'b': '1', 'a': 'e', 'c': 'e'},
        '1': {'b': 'e', 'a': 'e', 'c': '4'},
        '4': {'b': 'e', 'a': '3', 'c': '5'}
    }
}

a_as_b_as_c_pl = {
    'symbols': {'b', 'a', 'c'},
    'states': {'e', '1', '2', '3', '4'},
    'initial_state': '3', 'final_states': {'1', '4'},
    'transitions': {
        '3': {'b': '2', 'c': '4', 'a': '1'},
        '1': {'b': '2', 'c': '4', 'a': '1'},
        '4': {'b': 'e', 'c': '4', 'a': '1'},
        'e': {'b': 'e', 'c': 'e', 'a': 'e'},
        '2': {'b': '2', 'c': '4', 'a': '1'}
    }
}

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.items():
        if value in v:
            del a_dictionary[k]
    return dict({k: v for (k, v) in a_dictionary.items() if value not in v})



def show_value(key, dictionary_name):
    if key in dictionary_name:
        return dictionary_name[key]
    else:
        invalid_key = key
        return str(invalid_key) + " is not a valid key."


test_dictionary = {1:'a', 2:'b', 3:'c', 4:'d'}



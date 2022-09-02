import json


def open_file(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


def generate_diff(file1, file2):
    data_from_file1 = open_file(file1)
    data_from_file2 = open_file(file2)

    dict_with_keys_of_data_file1 = data_from_file1.keys()
    dict_with_keys_of_data_file2 = data_from_file2.keys()
    all_keys_sorted = sorted(set(list(dict_with_keys_of_data_file1) + (list(dict_with_keys_of_data_file2))))
    common_keys = list(set(dict_with_keys_of_data_file1).intersection(set(dict_with_keys_of_data_file2)))
    different_keys = list(set(dict_with_keys_of_data_file1).symmetric_difference(set(dict_with_keys_of_data_file2)))

    comparing_string = ''
    for key in all_keys_sorted:
        if key in common_keys:
            if data_from_file1[key] == data_from_file2[key]:
                comparing_string += f"  {key} : {data_from_file1[key]}\n"
            else:
                comparing_string += f"- {key} : {data_from_file1[key]}\n"
                comparing_string += f"+ {key} : {data_from_file2[key]}\n"
        elif key in different_keys:
            if key in data_from_file1:
                comparing_string += f"- {key} : {data_from_file1[key]}\n"
            elif key in data_from_file2:
                comparing_string += f"+ {key} : {data_from_file2[key]}\n"

    print('{' + '\n' + comparing_string + '}')

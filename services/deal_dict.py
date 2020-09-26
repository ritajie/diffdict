import json
import copy

from dictdiffer import diff, patch, swap, revert


def _change_dict_value(target: dict, keys: list, new_value):
    # 1.给 keys 转化一下，
    # str -> "str"；
    # int -> str(int)
    keys = copy.deepcopy(keys)
    for index, key in enumerate(keys):
        if isinstance(key, str):
            keys[index] = f'"{key}"'
        elif isinstance(key, int):
            keys[index] = str(key)

    # 2.do change
    exec(f'target[{"][".join(keys)}] = new_value')


def deal_dict(first_dict: dict, second_dict: dict):
    DIFF_LABEL = "__DIFF__"
    DEL_INT_LABLE = "__DEL_INT__"
    ADD_INT_LABLE = "__ADD_INT__"

    result = diff(first_dict, second_dict)

    # each_diff like (
    #   'change', 
    #   ['settings', 'assignees', 2], 
    #   (201, 202)
    # )
    for each_diff in list(result):
        diff_type = each_diff[0]
        diff_keys = each_diff[1]
        diff_content = each_diff[2]

        first_value_with_lable = DEL_INT_LABLE + str(diff_content[0])
        second_value_with_lable = ADD_INT_LABLE + str(diff_content[1])
        _change_dict_value(target=first_dict, keys=diff_keys, new_value=first_value_with_lable)
        _change_dict_value(target=second_dict, keys=diff_keys, new_value=second_value_with_lable)
        
        
    return first_dict, second_dict

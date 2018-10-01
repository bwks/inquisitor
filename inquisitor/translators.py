def textfsm_to_dict(textfsm_obj, data_type, data):
    """
    Convert a TextFSM data into a list of dictionaries. Each row
    in the TextFSM data will be converted to a list of dictionaries.
    :param textfsm_obj: TextFSM template object
    :param data_type: Type of data IE: interfaces, vrfs, etc...
    :param data: The text output from a command to convert
    :return: Dictionary of data.
    """
    dict_keys = [i.lower() for i in textfsm_obj.header]
    data_list = textfsm_obj.ParseText(data)

    data_dict = {data_type: []}
    for row in data_list:
        data_dict[data_type].append(dict(zip(dict_keys, row)))

    return data_dict

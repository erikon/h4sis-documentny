import json

new_data = {}
with open('data/wage_theft_data.json') as json_file:
    data = json.load(json_file)
    for key in data.keys():
        indexed_data = data[key]
        new_data[indexed_data['trade_nm']] = data[key]
        new_data[indexed_data['trade_nm']]['case_id'] = key


with open('wage_theft_data_cleaned.json', 'w') as fp:
    list_keys = list(new_data.keys())
    new_data['all_trade_names'] = list_keys
    json.dump(new_data, fp)

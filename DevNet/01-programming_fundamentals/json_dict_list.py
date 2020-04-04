import json
import pprint


json_array_read = open('json_array_example.json').read()
pprint.pprint(json_array_read)

""" JSON.loads method convert json to either directory or list, IF it is JSON object then it will get converted
to jSON directory or if it is the JSON array then it will get converted to list

JSON dumps convert back dict or list into json object or json array
"""

json_dict_list = json.loads(json_array_read)
pprint.pprint(json_dict_list)

print(json_dict_list['cars'][0])
print(json_dict_list['age'])

data = {"A":'1', "B":'2'}

dict_list_json = json.dumps(data)

print(dict_list_json)
print(type(dict_list_json))
print(type(data))


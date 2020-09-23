import json

def unique_id():
    json_to_dict = open('bank.json', 'r')
    coverted_dict = json.load(json_to_dict)
    json_to_dict.close()

    unique_id = []
    unique_id.sort()
    for i in coverted_dict:
        unique_id.append(i)
    try:
        id = int(unique_id[-1]) + 1
    except:
        id = 1
    return id


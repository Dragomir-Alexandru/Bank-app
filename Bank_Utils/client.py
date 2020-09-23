import json
from ID import unique_id

def add_client():
    id = unique_id()
    client = {
        'name': input('Numele clientului:\n=>'),
        'telephone': input('Numarul de telefon\n=>'),
        'city': input('Orasul clientului:\n=>'),
        'balance': 0
    }


    read_json_file = open('bank.json', 'r')
    converted_json_to_dict = json.load(read_json_file)
    read_json_file.close()

    converted_json_to_dict[id] = client
    new_client_json = json.dumps(converted_json_to_dict, indent=4)

    write_json_file = open('bank.json', 'w')
    write_json_file.write(new_client_json)


def check_client():
    print('\nClients:')
    print('*' * 50)
    json_client_file = open('bank.json', 'r')
    client_dict = json.load(json_client_file)
    json_client_file.close()

    for i in client_dict:
        print(f'{i}.{client_dict[i]["name"]}')
    print('*' * 50)

    while True:
        options = input('Please select a client or type EXIT to return to main menu\n=>')

        if options.lower() == 'exit':
            break
        elif options not in client_dict:
            print('Please select a valid ID\n')
            continue
        else:
            print('-' * 50)
            print(f"Nume: {client_dict[options]['name']}")
            print(f"Telefon: {client_dict[options]['telephone']}")
            print(f"Oras: {client_dict[options]['city']}")
            print(f"Balanta: {client_dict[options]['balance']}")
            print('-' * 50)
            break



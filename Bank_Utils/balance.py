import json

def edit_balance():
    print('\nClients:')
    print('*' * 50)
    json_file = open('bank.json', 'r')
    converted_dict = json.load(json_file)
    json_file.close()


    for i in converted_dict:
        print(f'{i}.{converted_dict[i]["name"]}')
    print('*' * 50)

    while True:
        options = input('Please select a client or type EXIT to return to main menu\n=>')
        if options.lower() == 'exit':
            break
        elif options not in converted_dict:
            print('Please select a valid ID\n')
            continue
        else:
            while True:
                new_balance = input('Please enter the amount:\n=>')
                try:
                    updated_balance = int(new_balance)
                except:
                    print('Please enter a valid amount')
                    continue
                converted_dict[options]['balance'] = int(new_balance)
                break
        break

    balance_json = json.dumps(converted_dict, indent=4)
    file = open('bank.json', 'w')
    file.write(balance_json)
    file.close()





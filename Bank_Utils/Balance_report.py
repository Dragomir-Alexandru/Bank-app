from reportlab.pdfgen.canvas import Canvas
import json


def balance_report():
    print('\nClients:')
    print('*' * 50)
    json_file = open('bank.json', 'r')
    json_to_dict = json.load(json_file)
    json_file.close()

    for i in json_to_dict:
        print(f'{i}.{json_to_dict[i]["name"]}')
    print('*' * 50)

    while True:
        options = input('Please select a client or type EXIT to return to main menu\n=>')
        if options.lower() == 'exit':
            break
        elif options not in json_to_dict:
            print('Please select a valid ID\n')
            continue
        else:
            print('*' * 50)
            canvas = Canvas(f'./{json_to_dict[options]["name"]}.pdf')
            canvas.drawString(200, 750, f'Balance report - {json_to_dict[options]["name"]}')
            canvas.drawString(25,680, f'Name: {json_to_dict[options]["name"]}')
            canvas.drawString(25, 640, f'Telephone: {json_to_dict[options]["telephone"]}')
            canvas.drawString(25, 600, f'City: {json_to_dict[options]["city"]}')
            canvas.setFont('Helvetica-Bold',15)
            canvas.saveState()
            canvas.drawString(25, 560, f'Balance: {json_to_dict[options]["balance"]}')
            canvas.save()
            break




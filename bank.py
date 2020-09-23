import Bank_Utils



while True:
    for i in Bank_Utils.menu.menu:
        print(i)
    print('*' * 50)
    x = input('Please select an option:\n=>')
    try:
        x_temp = int(x)
    except:
        print("-" * 50)
        print("\nI don't have this option, please select a valid option\n")
        print("-" * 50)
        continue
    if int(x) == 1:
        Bank_Utils.client.add_client()
        print('Client added')
        continue
    elif int(x) == 2:
        Bank_Utils.client.check_client()
        continue
    elif int(x) == 3:
        Bank_Utils.balance.edit_balance()
        continue
    elif int(x) == 4:
        Bank_Utils.Balance_report.balance_report()
        print('Balance report will be created once you close the current seesion')
        continue
    elif int(x) == 5:
        print('Program ended')
        break
    elif int(x) >= 6:
        print('Please select a valid option')
        continue

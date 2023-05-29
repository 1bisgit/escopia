#!/usr/bin/env python
import requests
print('''
                           _                _       
                          (_)              (_)      
  ___  ___  ___ ___  _ __  _  __ _          _  __ _ 
 / _ \/ __|/ __/ _ \| '_ \| |/ _` |        | |/ _` |
|  __/\__ \ (_| (_) | |_) | | (_| |        | | (_| |
 \___||___/\___\___/| .__/|_|\__,_|        |_|\__, |
                    | |                        __/ |
                    |_|                       |___/ 
''')
user = input("Insira o usuário do Instagram: ")
def denunciar_conta():
    url = 'https://www.instagram.com/' + user
    payload = {'action': 'report_account'}
    r = requests.post(url, data=payload)
    print("Conta denunciada com sucesso!")
for i in range(0, 10):
    denunciar_conta()
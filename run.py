import random
import requests
import time
import urllib.parse
import json
import base64
import socket
from datetime import datetime

with open('query_id.txt', 'r') as f:
        queries = [line.strip() for line in f.readlines()]

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Length': '472',
    'Content-Type': 'application/json',
    'Origin': 'https://tgapp.matchain.io',
    'Priority': 'u=1, i',
    'Referer': 'https://tgapp.matchain.io/',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

def decode_user_data(user_data):
    decoded_data = urllib.parse.unquote(user_data)
    return json.loads(decoded_data)

def get_first_name(user_data):
    return user_data["first_name"]

def get_last_name(user_data):
    return user_data["last_name"]

def get_uid(user_data):
    return int(user_data["id"])

def get_username(user_data):
    return user_data["username"]

def get_tg_login_params(chat_instance, chat_type, auth_date, hash):
    return {
        "chat_instance": chat_instance,
        "chat_type": chat_type,
        "auth_date": auth_date,
        "hash": hash
    }



def login(headers, user_data):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/user/login'
    # if auth_token:
    #     headers['Authorization'] = f'Bearer {auth_token}'
    
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    # chat_instance = int(user_data.split("chat_instance=")[1].split("&")[0])
    # chat_type = user_data.split("chat_type=")[1].split("&")[0]
    # auth_date = int(user_data.split("auth_date=")[1].split("&")[0])
    # hash = user_data.split("hash=")[1]

    data = {
        'first_name': get_first_name(user_data_dict),
        'last_name' : get_last_name(user_data_dict),
        'tg_login_params' : user_data,
        'uid' : get_uid(user_data_dict),
        'username' : get_username(user_data_dict),
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claim(headers, token, user_data):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/reward/claim'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    data = {
        'uid' : get_uid(user_data_dict)
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def startfarming(headers, token, user_data):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/reward/farming'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    data = {
        'uid' : get_uid(user_data_dict)
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimref(headers, token, user_data):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/invite/claim'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    data = {
        'uid' : get_uid(user_data_dict)
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getstatus(headers, token, user_data):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/landing/status'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    data = {
        'uid' : get_uid(user_data_dict)
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        elif response.status_code in response_code_notfound:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getlistquest(headers, token, user_data):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/task/list'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    data = {
        'uid' : get_uid(user_data_dict)
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def clearquests(headers, token, user_data, name):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/task/complete'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    headers['Content-Length'] = '46'
    data = {
        'uid' : get_uid(user_data_dict),
        'type': name
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response_code_notfound = range(400, 410)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimquest(headers, token, user_data, name):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/point/task/claim'
    user_data_dict = decode_user_data(user_data.split("user=")[1].split("&")[0])
    headers['Authorization'] = f'{token}'
    data = {
        'uid' : get_uid(user_data_dict),
        'type': name
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=headers, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def getgame(headers, token):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/game/rule'
    # headers['Authorization'] = f'{token}'
    head = {
        'Authorization': token
    }
    response_codes_done = range(200, 211)
    response_code_failed = range(500, 530)
    response_code_notfound = range(400, 410)
    try:
        response = requests.get(url, headers=head)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def play(token):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/game/play'
    # headers['Authorization'] = f'{token}'
    head = {
        'Authorization': token
    }
    response_codes_done = range(200, 211)
    response_code_failed = range(500, 530)
    response_code_notfound = range(400, 410)
    try:
        response = requests.get(url, headers=head)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        elif response.status_code in response_code_notfound:
            print(response.text)
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def claimplay(token, game_id, point):
    url = 'https://tgapp-api.matchain.io/api/tgapp/v1/game/claim'
    # headers['Authorization'] = f'{token}'
    head = {
        'Authorization': token
    }
    data = {
        'game_id' : game_id,
        'point': point
    }
    try:
        response_codes_done = range(200, 211)
        response_code_failed = range(500, 530)
        response = requests.post(url, headers=head, json=data)
        if response.status_code in response_codes_done:
            return response.json()
        elif response.status_code in response_code_failed:
            return None
        else:
            raise Exception(f'Unexpected status code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error making request: {e}')
        return None

def dailymain():

    while True:
        selector_ref = input("Claim ref point ? (default n) (y/n): ").strip().lower()
        if selector_ref in ['y', 'n', '']:
            selector_ref = selector_ref or 'n'
            break
        else:
            print("Input 'y' or 'n'.")

    while True:
        selector_game = input("Auto play game ? (default n) (y/n): ").strip().lower()
        if selector_game in ['y', 'n', '']:
            selector_game = selector_game or 'n'
            break
        else:
            print("Input 'y' or 'n'.")

    while True:
        for index, query in enumerate(queries):
           user = login(headers, query)
           if user is not None:
                data = user.get('data')
                token = data.get('token')
                users = data.get('user')
                print(f"ID : {users.get('uid')} | username : {users.get('username')} | name : {users.get('first_name')} {users.get('last_name')}")
                time.sleep(3)

                #CLAIM
                data_claim = claim(headers, token, query)
                while True:
                    if data_claim is not None:
                        code = data_claim.get('code')
                        if code == 200:
                            print(f"Claim Reward : {int(data_claim.get('data'))/1000}")
                            break
                        else:
                            err = data_claim.get('err')
                            if err == "Claim failed":
                                time.sleep(1)
                                print("Repeat Claim")
                                data_claim = claim(headers, token, query)
                            else:
                                print(f"{data_claim.get('err')}")
                                time.sleep(1)
                                break
                time.sleep(2)
                #STARTFARMING
                data_farming = startfarming(headers, token, query)
                if data_farming is not None:
                    code = data_farming.get('code')
                    if code == 200:
                        print(f"Start Farming")
                    else:
                        print(f"{data_farming.get('err')}")
                    time.sleep(1)

                time.sleep(2)
                #CLAIM REF
                if selector_ref == 'y':
                    data_ref = claimref(headers, token, query)
                    while True:
                        if data_ref is not None:
                            code = data_ref.get('code')
                            if code == 200:
                                print(f"Claim Reward Ref : {int(data_ref.get('data'))/1000}")
                                break
                            else:
                                err = data_ref.get('err')
                                if err == "Claim failed":
                                    time.sleep(1)
                                    print("repeat claim")
                                    data_ref = claimref(headers, token, query)
                                else:
                                    print(f"{data_ref.get('err')}")
                                    time.sleep(1)
                                    break
                        
                
                #START GAME
                if selector_game == 'y':
                    data_game = getgame(headers, token)
                    time.sleep(3)
                    if data_game is not None:
                        data = data_game.get('data')
                        game_count = int(data.get('game_count'))
                        for i in range(game_count):
                            data_play = play(token)
                            if data_game is not None:
                                data_game = data_play.get('data')
                                game_id = data_game.get('game_id')
                                point = random.randint(50, 60)
                                print('Start Playing')
                                time.sleep(35)
                                data_claimplay = claimplay(token, game_id, point)
                                if data_claimplay is not None:
                                    print(f'Game playing Done, got point : {point}')
           else:
                print('user not found')

               
        delay_time = random.randint(7200, 7500)
        printdelay(delay_time)
        time.sleep(delay_time)

def mainclearquest():
    for index, query in enumerate(queries):
        user = login(headers, query)

        if user is not None:
            data = user.get('data')
            token = data.get('token')
            users = data.get('user')
            print(f"ID : {users.get('uid')} | username : {users.get('username')} | name : {users.get('first_name')} {users.get('last_name')}")
            time.sleep(3)
            data_quest = getlistquest(headers, token, query)
            if data_quest is not None:
                data = data_quest.get('data')
                for task in data:
                    if task.get('complete') == False:
                        name = task.get('name')
                        data_quest = clearquests(headers, token, query, name)
                        time.sleep(2)
                        if data_quest is not None:
                            data_claim_quest = claimquest(headers, token, query, name)
                            if data_claim_quest is not None:
                                print(f"Task : {name} | DONE")
                        time.sleep(2)



############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hours, {minutes} minutes, and {sec} seconds")

def main():
    print(r"""
        
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sanscryptox
              
        select this one :
        1. claim quest
        2. claim daily
          
          """)
    while True:
        selector = input("Select the one ? (default 2): ").strip().lower()
        if selector in ['1', '2', '']:
            selector = selector or 'n'
            break
        else:
            print("Input '1' or '2'.")

    if selector == '1':
        mainclearquest()
    elif selector == '2':
        dailymain()
    else:
        exit()


def print_welcome_message(serial=None):
    print(r"""
              
            Created By Snail S4NS Group
    find new airdrop & bot here: t.me/sansxgroup
              
          """)
    print()
    if serial is not None:
        print(f"Copy, tag bot @SnailHelperBot and paste this key in discussion group t.me/sansxgroup")
        print(f"Your key : {serial}")

def read_serial_from_file(filename):
    serial_list = []
    with open(filename, 'r') as file:
        for line in file:
            serial_list.append(line.strip())
    return serial_list

serial_file = "serial.txt"
serial_list = read_serial_from_file(serial_file)


def read_initdata_from_file(filename):
    initdata_list = []
    with open(filename, 'r') as file:
        for line in file:
            initdata_list.append(line.strip())
    return initdata_list

def get_user_id_from_init_data(init_data):
    parsed_data = urllib.parse.parse_qs(init_data)
    if 'user' in parsed_data:
        user_data = parsed_data['user'][0]
        user_data_json = urllib.parse.unquote(user_data)
        user_data_dict = json.loads(user_data_json)
        if 'id' in user_data_dict:
            return user_data_dict['id']
    return None

def get_nama_from_init_data(init_data):
    parsed_data = urllib.parse.parse_qs(init_data)
    if 'user' in parsed_data:
        user_data = parsed_data['user'][0]
        data = ""
        user_data_json = urllib.parse.unquote(user_data)
        user_data_dict = json.loads(user_data_json)
        if 'first_name' in user_data_dict:
            data = user_data_dict['first_name']
        if 'last_name' in user_data_dict:
            data = data + " " + user_data_dict['last_name']
        if 'username' in user_data_dict :
            data = data + " " + f"({user_data_dict['username']})"
    return data


def get_serial(current_date, getpcname, name, status):
    formatted_current_date = current_date.strftime("%d-%m-%Y")
    # Encode each value using base64
    getpcname += "knjt"
    name    += "knjt"
    encoded_getpcname = base64.b64encode(getpcname.encode()).decode().replace("=", "")
    encoded_current_date = base64.b64encode(formatted_current_date.encode()).decode().replace("=", "")
    encoded_name = base64.b64encode(name.encode()).decode().replace("=", "")
    encoded_status = base64.b64encode(str(status).encode()).decode().replace("=", "")

    # Calculate the length of each encoded value
    getpcname_len = len(encoded_getpcname)
    current_date_len = len(encoded_current_date)
    name_len = len(encoded_name)
    status_len = len(encoded_status)

    # Concatenate the encoded values with their lengths
    serial = "S4NS-"
    serial += str(getpcname_len).zfill(2) + encoded_getpcname
    serial += str(current_date_len).zfill(2) + encoded_current_date
    serial += str(name_len).zfill(2) + encoded_name
    serial += str(status_len).zfill(2) + encoded_status
    return serial

def decode_pc(serial, getpcname, name, current_date):
    try:
        getpcname_len = int(serial[5:7])
        encoded_getpcname = serial[7:7+getpcname_len]
        current_date_len = int(serial[7+getpcname_len:9+getpcname_len])
        encoded_current_date = serial[9+getpcname_len:9+getpcname_len+current_date_len]
        name_len = int(serial[9+getpcname_len+current_date_len:11+getpcname_len+current_date_len])
        encoded_name = serial[11+getpcname_len+current_date_len:11+getpcname_len+current_date_len+name_len]
        status_len = int(serial[11+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len])
        encoded_status = serial[13+getpcname_len+current_date_len+name_len:13+getpcname_len+current_date_len+name_len+status_len]

        # Decode each value using base64
        decoded_getpcname = base64.b64decode(encoded_getpcname + "==").decode()
        decoded_current_date = base64.b64decode(encoded_current_date + "==").decode()
        decoded_name = base64.b64decode(encoded_name + "==").decode()
        decoded_status = base64.b64decode(encoded_status + "==").decode()
        
        dates = compare_dates(decoded_current_date)

        if decoded_status != '1':
            print("Key Not Generated")
            return None
            
        elif decoded_getpcname.replace("knjt", "") != getpcname:
            print("Different devices registered")
            return None
        
        elif decoded_name.replace("knjt", "") != name:
            print("Different bot registered")
            return None
        
        elif dates < 0:
            print("Key Expired")
            return None
        else:
            print(f"            Key alive until : {decoded_current_date} ")
            return dates
    except Exception as e:
        print(f'Key Error : {e}')

def compare_dates(date_str):
    tanggal_compare_dt = datetime.strptime(date_str, '%d-%m-%Y')
    tanggal_now = datetime.now()
    perbedaan_hari = (tanggal_compare_dt - tanggal_now).days
    return perbedaan_hari

def started():
    getpcname = socket.gethostname()
    name = "MATCHAIN"
    current_date = datetime.now() # Get the current date
    status = '0'

    if len(serial_list) == 0:
        serial = get_serial(current_date, getpcname, name, status)
        print_welcome_message(serial)
    else:
        serial = serial_list[0]
        if serial == 'S4NS-XXWEWANTBYPASSXX':
            main()
        else:
            decodeds = decode_pc(serial, getpcname, name, current_date)
            if decodeds is not None:
                    print_welcome_message()
                    time.sleep(10)
                    main()         
            else:
                serial = get_serial(current_date, getpcname, name, status)
                print_welcome_message(serial)
                print("Please submit the key to bot for get new key")
            

if __name__ == "__main__":
    started()


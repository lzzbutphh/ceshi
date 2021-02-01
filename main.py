# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

import requests
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data = {
        "data": {
            "card_module": "0",
            "group": "自己",
            "name": "李宗aaaa",
            "company": "北京邮电大学",
            "phone": "12345678901",
            "we_chat": "15590698879",
            "qq": "3225152107",
            "home": "吉林公主岭",
            "email": "@edu.cn",
            "is_own": "true",

        },
        "user_id": "41208289e0ec7eb1a8d1bc2298933ba6",
        'card_id': 'ded8a0930feb88e67ae5d927b86a6d19',
        "icon": "true",
        "is_own": "true",
        "image": "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"
        # "key": '清华',
        # "operate": "insert",
        # "key_name": "company",

    }
    header = {
        "token": "eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxMjAwMjc3NSwiZXhwIjoxNjEyNjA3NTc1fQ.eyJvcGVuaWQiOiJvdTJ0YTVOcGtfMjh4RUxRMkRMNE1ZWmZKbkwwIiwic2Vzc2lvbl9rZXkiOiJNUTNGRDlmdkJiRzFUcnVnVGJJNk9RPT0ifQ.vZnZohTCyceSPiWMBLGO1aPMupr6E9Lri5BkoxJ0PspEFkywbD0R3tEg_stn9_AlhulKqBMv2qieObK586oRYw",
        "user_id": "41208289e0ec7eb1a8d1bc2298933ba6"
    }
    a = requests.post('http://39.101.204.166/CheckImage', json=data, headers=header)
    # a = requests.post('https://123.56.139.158/api/card/show', json=data, headers=header ,verify=False)
    print(a.text)
    a = "家人"

    '''python manage.py runserver -h 0.0.0.0 -p 4430 '''
    # print(isinstance(a, list))
    # a = requests.get('http://127.0.0.1:8088/image/qrcode/qrcode.png')
    # fire = open('a.png', 'wb')
    # fire.write(a.content)
    # fire.close()
    #
    # print(a.content)

    # time.sleep(100)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

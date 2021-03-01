import platform
import os

def extract_token(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        token_list = [line.strip('\n') for line in f]

    return token_list

def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')
    else:
        print('\n')*120
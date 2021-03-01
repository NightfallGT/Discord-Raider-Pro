import platform
import os
import argparse

def clear():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    elif system == 'Linux':
        os.system('clear')
    else:
        print('\n')*120

def extract_token(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        token_list = [line.strip('\n') for line in f]

    return token_list

def start_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--insert', help="Add path to file", required=True)
    parser.add_argument('-m', '--message', help="Add id", required=True)
    parser2 = parser.parse_args()
    return parser2

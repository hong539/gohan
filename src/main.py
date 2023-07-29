# import os
from pathlib import Path
import pykakasi
# from bs4 import BeautifulSoup
import pandas as pd

gohan_project_path = Path.cwd()
tests_path = str(gohan_project_path) + "/tests"
# test_file = tests_path + "/self_test.txt"
test_file = tests_path + "/example.txt"

f = open(test_file, 'r')
lines = f.readlines()
# print(f)
# print(lines)

def transfer(text):
    kks = pykakasi.kakasi()
    result = kks.convert(text)
    for item in result:
        print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

count = 0
for line in lines:
    count += 1
    # print(line.strip())
    transfer(line.strip())


def parser():
        target_table = pd.read_html("https://bluearchive.wikiru.jp/?%E3%82%AD%E3%83%A3%E3%83%A9%E3%82%AF%E3%82%BF%E3%83%BC%E4%B8%80%E8%A6%A7#j5a6cb9f")        
        print("type:", type(target_table))
        print("len:", len(target_table))
        print(target_table)
        # print(target_table[0])
        

if __name__ == "__main__":
        parser()        
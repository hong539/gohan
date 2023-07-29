# import os
from pathlib import Path
import pykakasi
from bs4 import BeautifulSoup
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
        pass

if __name__ == "__main__":
        parser()        
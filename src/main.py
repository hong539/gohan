import pykakasi
kks = pykakasi.kakasi()
text = "煮込み"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))
    
text = "教えてくれ、五飛"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

text = "早瀬ユウカ"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

text = "二次元"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

text = "nijigen"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

text = "漬鯊"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn'])) 

# かな: kana 'カナ', hiragana: 'かな', romaji: 'kana'
# 漢字: kana 'カンジ', hiragana: 'かんじ', romaji: 'kanji'
# 煮込み
# 二次元nijigen
# 教えてくれ、五飛
# 早瀬ユウカ
# 寿司です
# ムービー
# movie
# うなぎ丼
# 鰻魚飯 (鰻丼)
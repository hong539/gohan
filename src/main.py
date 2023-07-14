import pykakasi
kks = pykakasi.kakasi()
text = "かな漢字"
result = kks.convert(text)
for item in result:
    print("{}: kana '{}', hiragana '{}', romaji: '{}'".format(item['orig'], item['kana'], item['hira'], item['hepburn']))

# かな: kana 'カナ', hiragana: 'かな', romaji: 'kana'
# 漢字: kana 'カンジ', hiragana: 'かんじ', romaji: 'kanji'
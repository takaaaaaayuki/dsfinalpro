from bs4 import BeautifulSoup
import requests #HTTP操作用
import time


# アクセスしたいWebサイトのURL
url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view='

# Webサーバにリクエストを出す．レスポンスを変数に格納しておく
r = requests.get(url)


soup = BeautifulSoup(r.text, 'html.parser') # HTMLソースをBeautifulSoupオブジェクトに変換する（プログラムで扱いやすくするため）




detas = soup.find_all('tr', style="text-align:right;")
index = 0
while index < len(detas):
    a_tag = detas[index].find('a')
    if a_tag:
        day = a_tag.text
        
        temp = detas[index].find_all('td', class_="data_0_0")
        if temp:
            hpa = temp[0].text
            Precipitation = temp[2].text
            temp_av = temp[7].text
            temp_max = temp[8].text
            temp_min = temp[9].text
            humidity_av = temp[10].text
            humidity_min = temp[11].text
            suntime = temp[17].text
        else:
            pass
    else:
        pass
    index += 1


import sqlite3


# wDBファイルを保存するためのファイルパス
path = '/Users/takayuki/Lecture/ds-programming'

# DBファイル名
db_name = 'sleeplv.sqlite'

# DBに接続する
con = sqlite3.connect(path + db_name)

# SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# テーブルを作成するSQL
sql_create_table_DSprogHW = '''
    CREATE TABLE sleeplv (
        day INTEGER,
        hpa REAL,
        Precipitation TEXT,
        temp_av REAL,
        temp_max REAL,
        temp_min IREAL,
        humidity_av TEXT,
        suntime TEXT
    );
'''
# データの挿入
cur.execute('''
    INSERT INTO sleeplv (day, hpa, Precipitation, temp_av, temp_max, temp_min, humidity_av, suntime)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?);
''', (day, hpa, Precipitation, temp_av, temp_max, temp_min, humidity_av, suntime))

# # 4．SQLを実行する
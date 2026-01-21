import sqlite3
import pandas as pd
import os

def init_db():
    """学習用のリッチなサンプルデータベースを作成する"""
    # フォルダがない場合は作成
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect('data/sample.db')
    cursor = conn.cursor()
    
    # 既存のテーブルを削除（カラム変更を反映させるため）
    cursor.execute('DROP TABLE IF EXISTS users')
    
    # 新しい構造でテーブル作成
    # salary(月収), join_date(入社日), rating(評価) を追加
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT,
        salary INTEGER,
        join_date TEXT,
        rating INTEGER
    )
    ''')
    
    # 実務を想定したサンプルデータ
    # 名前, 年齢, 部署, 月収, 入社日, 評価(1-5)
    users = [
        (1, '田中 太郎', 28, '営業', 320000, '2023-04-01', 4),
        (2, '佐藤 花子', 35, '開発', 450000, '2021-10-15', 5),
        (3, '鈴木 一郎', 42, '人事', 380000, '2018-01-20', 3),
        (4, '高橋 次郎', 25, '開発', 280000, '2024-04-01', 4),
        (5, '伊藤 みゆき', 31, '営業', 350000, '2022-07-12', 4),
        (6, '渡辺 健', 50, '開発', 550000, '2015-05-10', 5),
        (7, '中村 結衣', 29, '人事', 300000, '2023-11-01', 2),
        (8, '小林 直樹', 38, '営業', 410000, '2020-02-15', 3)
    ]
    
    cursor.executemany('INSERT INTO users VALUES (?,?,?,?,?,?,?)', users)
    
    conn.commit()
    conn.close()

def run_query(query):
    """SQLを実行して結果をPandas DataFrameで返す"""
    conn = sqlite3.connect('data/sample.db')
    try:
        # DBが空の場合に備えて初期化を走らせる
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return str(e)
    finally:
        conn.close()
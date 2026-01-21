import sqlite3
import pandas as pd
import os

def init_db():
    """学習用データベースの初期化（AI用リッチテーブルとPG用シンプルテーブルの両方を作成）"""
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect('data/sample.db')
    cursor = conn.cursor()
    
    # --- 1. AI SQL Search用のリッチなテーブル (users) ---
    cursor.execute('DROP TABLE IF EXISTS users')
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
    
    users_data = [
        (1, '田中 太郎', 28, '営業', 320000, '2023-04-01', 4),
        (2, '佐藤 花子', 35, '開発', 450000, '2021-10-15', 5),
        (3, '鈴木 一郎', 42, '人事', 380000, '2018-01-20', 3),
        (4, '高橋 次郎', 25, '開発', 280000, '2024-04-01', 4),
        (5, '伊藤 みゆき', 31, '営業', 350000, '2022-07-12', 4),
        (6, '渡辺 健', 50, '開発', 550000, '2015-05-10', 5),
        (7, '中村 結衣', 29, '人事', 300000, '2023-11-01', 2),
        (8, '小林 直樹', 38, '営業', 410000, '2020-02-15', 3)
    ]
    cursor.executemany('INSERT INTO users VALUES (?,?,?,?,?,?,?)', users_data)
    
    # --- 2. SQL Playground用のシンプルなテーブル (simple_users) ---
    cursor.execute('DROP TABLE IF EXISTS simple_users')
    cursor.execute('''
    CREATE TABLE simple_users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT
    )
    ''')
    
    simple_users_data = [
        (1, '田中 太郎', 25, '営業'),
        (2, '佐藤 花子', 32, '開発'),
        (3, '鈴木 一郎', 45, '人事'),
        (4, '高橋 次郎', 28, '開発')
    ]
    cursor.executemany('INSERT INTO simple_users VALUES (?,?,?,?)', simple_users_data)
    
    conn.commit()
    conn.close()

def run_query(query):
    """SQLを実行して結果をPandas DataFrameで返す"""
    conn = sqlite3.connect('data/sample.db')
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except Exception as e:
        return str(e)
    finally:
        conn.close()
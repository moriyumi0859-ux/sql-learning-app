import sqlite3
import pandas as pd

def init_db():
    """学習用のサンプルデータベースを作成する"""
    conn = sqlite3.connect('data/sample.db')
    cursor = conn.cursor()
    
    # ユーザーテーブルの作成
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT
    )
    ''')
    
    # サンプルデータの挿入
    users = [
        (1, '田中 太郎', 25, '営業'),
        (2, '佐藤 花子', 32, '開発'),
        (3, '鈴木 一郎', 45, '人事'),
        (4, '高橋 次郎', 28, '開発')
    ]
    cursor.executemany('INSERT OR IGNORE INTO users VALUES (?,?,?,?)', users)
    
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
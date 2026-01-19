import streamlit as st
import os
from utils import init_db

# アプリの設定
st.set_page_config(
    page_title="SQL学習アプリ",
    page_icon="🎓",
    layout="wide"
)

# dataフォルダがない場合は作成
if not os.path.exists('data'):
    os.makedirs('data')

# データベースの初期化
init_db()

st.title("🎓 効率よくSQLを学べるアプリ")
st.write("このアプリでは、実践的な操作を通じてSQLの基本から応用までを効率よく学習できます。")

st.info("左側のサイドバーから学習したいコンテンツを選択してください。")

# コンテンツの紹介
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. 📊 SQL Playground")
    st.write("自由にSQLを書いて、結果をグラフで可視化してみましょう。")
    
    st.subheader("2. 🔗 Join Master")
    st.write("図解を見ながら、テーブルの結合（JOIN）を視覚的に理解します。")

with col2:
    st.subheader("3. 🤖 AI Search")
    st.write("「〜のデータを取ってきて」と日本語で命令してSQLを生成します。")
    
    st.subheader("4. 📝 Quiz Drill")
    st.write("穴埋め問題に答えて、基本構文をマスターしましょう。")
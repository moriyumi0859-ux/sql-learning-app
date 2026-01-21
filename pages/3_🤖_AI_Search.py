import streamlit as st
from openai import OpenAI
from utils import run_query
from style import apply_custom_css
import pandas as pd

# デザイン適用
apply_custom_css()

st.title("🤖 AI SQL Search")

# 1. データの可視化（ここが重要！）
st.subheader("📊 現在のデータ（先頭3件を表示中）")
sample_data = run_query("SELECT * FROM users LIMIT 3")
if isinstance(sample_data, pd.DataFrame):
    st.dataframe(sample_data, use_container_width=True, hide_index=True)
else:
    st.warning("データの読み込みに失敗しました。init_db()を実行してください。")

# 2. 質問のヒント（ボタンで入力できるようにする）
st.write("💡 **こんな質問ができます（クリックでコピー）:**")
example_col1, example_col2, example_col3 = st.columns(3)

# セッション状態を使ってテキスト入力を制御
if 'search_input' not in st.session_state:
    st.session_state.search_input = ""

if example_col1.button("部署ごとの平均給与は？"):
    st.session_state.search_input = "部署ごとの平均給与を計算して"
if example_col2.button("評価4以上の開発部員は？"):
    st.session_state.search_input = "開発部で評価が4以上の人の名前と入社日を教えて"
if example_col3.button("一番給与が高い人は？"):
    st.session_state.search_input = "給与が最も高い人の名前と年齢を表示して"

# 3. AIへの入力エリア
user_input = st.text_input(
    "AIに日本語で依頼:", 
    value=st.session_state.search_input,
    placeholder="例：2023年以降に入社した人を教えて"
)

if user_input:
    with st.spinner("AIが最適なSQLを考案中..."):
        # プロンプト（AIにテーブル情報を教える）
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        prompt = f"""
        あなたはSQLの専門家です。以下のテーブル構造に基づいてSQLを生成してください。
        テーブル名: users
        カラム: id, name, age, department, salary(給与), join_date(入社日), rating(評価)
        
        依頼内容: {user_input}
        出力: SQL文のみ
        """
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        generated_sql = response.choices[0].message.content.strip().replace("```sql", "").replace("```", "").strip()

    st.subheader("📝 生成されたSQL")
    st.code(generated_sql, language="sql")

    if st.button("このSQLを実行する", type="primary"):
        result = run_query(generated_sql)
        if isinstance(result, str):
            st.error(f"実行エラー: {result}")
        else:
            st.success(f"検索結果: {len(result)} 件")
            st.dataframe(result, use_container_width=True, hide_index=True)
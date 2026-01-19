import streamlit as st
from openai import OpenAI
from utils import run_query

st.title("🤖 AI SQL Search")
st.write("「30歳以上のユーザーを教えて」のように日本語で入力してください。")

# クライアントの初期化（Secretsからキーを取得）
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ユーザー入力
user_input = st.text_input("知りたい情報を入力してください:", placeholder="例：営業部のユーザーを全員表示して")

if user_input:
    with st.spinner("AIがSQLを生成中..."):
        # AIへの指示（プロンプト）
        prompt = f"""
        あなたはSQLの専門家です。以下のテーブル構造に基づいて、ユーザーの依頼をSQL文に変換してください。
        
        テーブル名: users
        カラム: id, name, age, department
        
        依頼: {user_input}
        
        返答はSQL文のみを出力してください。解説は不要です。
        """
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        
        generated_sql = response.choices[0].message.content.strip()
        # Markdownの装飾（```sql ... ```）を外す処理
        generated_sql = generated_sql.replace("```sql", "").replace("```", "").strip()

    st.subheader("生成されたSQL")
    st.code(generated_sql, language="sql")

    if st.button("このSQLを実行する"):
        result = run_query(generated_sql)
        if isinstance(result, str):
            st.error(f"実行エラー: {result}")
        else:
            st.success("実行結果:")
            st.dataframe(result)
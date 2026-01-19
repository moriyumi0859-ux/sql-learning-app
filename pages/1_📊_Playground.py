import streamlit as st
from utils import run_query
import plotly.express as px
import pandas as pd
from style import apply_custom_css

apply_custom_css()

st.title("📊 SQL Playground")

# 1. イントロダクション
st.info("""
### 💡 ここでできること
SQLを書いて、データを自由に取り出したり集計したりしてみましょう。
左側の**「元のデータ」**が、あなたの書いたSQLでどう変わるか右側の**「実行結果」**で確認できます。
""")

# 2. 画面を左右に分割して、比較しやすくする
col_source, col_main = st.columns([1, 2])

with col_source:
    st.subheader("📋 元のネタ（users）")
    st.caption("この名簿を加工します。")
    source_df = run_query("SELECT * FROM users")
    if isinstance(source_df, pd.DataFrame):
        st.dataframe(source_df, use_container_width=True, hide_index=True)

with col_main:
    st.subheader("✍️ SQLを書いてみよう")
    
    # お手本ボタンの配置
    st.write("お手本をクリックしてみてね：")
    c1, c2, c3 = st.columns(3)
    
    # セッション状態を使ってテキストエリアの内容を書き換える
    if 'query_text' not in st.session_state:
        st.session_state.query_text = "SELECT * FROM users;"

    if c1.button("全員表示"):
        st.session_state.query_text = "SELECT * FROM users;"
    if c2.button("部署ごとに集計"):
        st.session_state.query_text = "SELECT department, COUNT(*) as 人数 FROM users GROUP BY department;"
    if c3.button("年齢が高い順"):
        st.session_state.query_text = "SELECT name, age FROM users ORDER BY age DESC;"

    # テキストエリア
    query = st.text_area("SQLを入力:", value=st.session_state.query_text, height=100, key="sql_input")

    if st.button("実行する", type="primary"):
        result = run_query(query)
        
        if isinstance(result, str):
            st.error(f"エラーが発生しました: {result}")
        else:
            st.success("成功しました！")
            
            # 結果表示エリア
            res_tab, chart_tab = st.tabs(["📋 結果の表", "📈 グラフ"])
            
            with res_tab:
                st.dataframe(result, use_container_width=True, hide_index=True)
            
            with chart_tab:
                # 数値列があるかチェックしてグラフを描画
                numeric_cols = result.select_dtypes(include=['number']).columns.tolist()
                if len(result.columns) >= 2 and len(numeric_cols) > 0:
                    fig = px.bar(result, x=result.columns[0], y=numeric_cols[0], 
                                 title=f"{numeric_cols[0]} の分布",
                                 color_discrete_sequence=['#00CC96'])
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("グラフを表示するには、集計結果に数値列が必要です（『部署ごとに集計』などを試してね）。")

# ヒントを下に置く
with st.expander("🔍 SQLのヒント"):
    st.markdown("""
    - **SELECT * FROM users;** : 全員の名簿が見れます。
    - **WHERE age >= 30;** : 30歳以上の人に絞り込めます。
    - **ORDER BY age DESC;** : 年齢が高い順に並び替えます。
    - **GROUP BY department;** : 部署ごとにまとめます。
    """)
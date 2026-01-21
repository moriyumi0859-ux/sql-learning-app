import streamlit as st
from style import apply_custom_css
import pandas as pd
import os

st.title("📝 SQL Quiz Drill")
apply_custom_css(progress_val=100)

# 1. データの読み込み
@st.cache_data
def load_quiz_data():
    file_path = 'data/quiz_data.csv'
    if os.path.exists(file_path):
        # quotechar='"' を追加することで、"で囲まれた中のカンマを無視します
        return pd.read_csv(file_path, quotechar='"', skipinitialspace=True)
    else:
        return None
    
df_questions = load_quiz_data()

if df_questions is None:
    st.error("問題データが見つかりません。data/quiz_data.csv を作成してください。")
    st.stop()

# 2. セッション状態で進捗を管理
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0

# 全問題数
total_q = len(df_questions)

# 3. 進捗表示
if st.session_state.current_q < total_q:
    progress = (st.session_state.current_q) / total_q
    st.progress(progress)
    st.write(f"問題 {st.session_state.current_q + 1} / {total_q}")

    # 現在の問題を抽出
    q = df_questions.iloc[st.session_state.current_q]
    
    with st.container(border=True):
        st.subheader(q["q"])
        st.info(f"💡 ヒント: {q['hint']}")
        
        cols = st.columns([2, 1, 2])
        cols[0].code(q["code_pre"], language="sql")
        user_input = cols[1].text_input("ここに入力", key=f"q_{st.session_state.current_q}")
        cols[2].code(q["code_post"], language="sql")
        
        if st.button("回答する", type="primary"):
            clean_input = user_input.strip()
            # CSVからの読み込みは型が変わることがあるためstrで比較
            if clean_input.upper() == str(q["answer"]).upper():
                st.success("正解です！✨")
                st.session_state.score += 1
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.error("もう一度考えてみましょう！")
else:
    # 終了画面
    st.balloons()
    st.success(f"🎊 全問クリア！スコア: {st.session_state.score} / {total_q}")
    if st.button("最初から挑戦する"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.rerun()
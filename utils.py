import streamlit as st

def apply_custom_css():
    """アプリ全体のモダンデザインとサイドバーの装飾を一括適用"""
    st.markdown("""
    <style>
        /* 1. ボタン：浮き出るモダンデザイン */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border-radius: 30px;
            border: none;
            padding: 12px 30px;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(110, 142, 251, 0.3);
            transition: all 0.3s;
        }
        div.stButton > button[kind="primary"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(110, 142, 251, 0.4);
        }

        /* 2. 入力枠：二重線を防ぎ、フォーカス時に光らせる */
        /* 標準の枠線を消すのではなく、自然に馴染ませます */
        .stTextArea textarea, .stTextInput input {
            border: 1px solid #e0e0e0 !important; /* 細い一本線に固定 */
            border-radius: 10px !important;
            transition: all 0.3s ease;
        }
        
        /* 入力中（フォーカス時）の演出 */
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #6e8efb !important;
            box-shadow: 0 0 0 3px rgba(110, 142, 251, 0.2) !important; /* 外側に光る輪を出す */
            outline: none !important;
        }

        /* サイドバーの背景色を少し明るく */
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa;
        }
    </style>
    """, unsafe_allow_html=True)

    # サイドバーのコンテンツ（日本語版）
    with st.sidebar:
        st.divider()
        st.caption("🚀 学習ロードマップ")
        st.progress(75, text="現在は「AI応用」フェーズ") 
        
        st.markdown("""
        <div style='font-size: 0.8rem; color: #666; background-color: #ffffff; padding: 10px; border-radius: 10px; border: 1px solid #eee;'>
        <b>💻 システム稼働状況</b><br>
        🟢 データベース: 接続済み<br>
        🟢 AIエンジン: 待機中 (GPT-4o)<br>
        🔵 環境: Mac mini M4 Pro
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        st.caption("💡 今日のSQLヒント")
        st.info("JOIN（結合）のコツは、2つの表をつなぐ『接着剤（共通の列）』を見つけることです。")
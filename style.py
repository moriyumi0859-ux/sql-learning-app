import streamlit as st

def apply_custom_css():
    """アプリ全体のモダンデザインとサイドバーのプロフィールを一括適用"""
    st.markdown("""
    <style>
        /* 1. ボタン：今どきの浮き出るモダンデザイン */
        div.stButton > button[kind="primary"] {
            background: linear-gradient(135deg, #6e8efb, #a777e3);
            color: white;
            border-radius: 30px;
            border: none;
            padding: 12px 30px;
            font-weight: 600;
            letter-spacing: 1px;
            box-shadow: 0 10px 20px rgba(110, 142, 251, 0.3);
            transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
        }
        div.stButton > button[kind="primary"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px rgba(110, 142, 251, 0.5);
            color: white;
        }

        /* 2. 入力枠：背景から浮かせて視認性をアップ */
        .stTextArea textarea, .stTextInput input {
            background-color: #ffffff !important;
            border: 2px solid #e0e0e0 !important;
            border-radius: 12px !important;
        }
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #6e8efb !important;
            box-shadow: 0 0 15px rgba(110, 142, 251, 0.2) !important;
        }

        /* 3. サイドバー：プロ仕様の装飾 */
        section[data-testid="stSidebar"] {
            background-color: #f0f2f6;
        }
        
    </style>
    </div>
    """, unsafe_allow_html=True)

    # サイドバーにあなたのプロフィールを追加
    with st.sidebar:
        st.divider() # 区切り線
        
        # 1. 学習ロードマップ
        st.caption("🚀 SQL Learning Roadmap")
        st.progress(75, text="Your Journey: Advanced") # 進捗バーっぽく見せる
        
        # 2. ミニ情報
        st.markdown("""
        <div style='font-size: 0.8rem; color: gray;'>
        <b>System Status</b><br>
        🟢 Database: Connected<br>
        🟢 AI Engine: Ready (GPT-4o)<br>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # 3. ちょっとしたお遊び（今日のSQL格言など）
        st.caption("💡 SQL Tip of the Day")
        st.info("JOINのコツは、共通の『接着剤（Key）』を見つけることです。")
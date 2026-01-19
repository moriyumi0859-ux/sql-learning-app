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
        st.markdown("### 🛠️ Developer Profile")
        st.info("""
        **Generative AI Engineer Trainee**
        
        SQL学習をもっと楽しく、直感的に。
        Mac mini M4 Proのパワーを活かして開発しています。
        """)
        st.divider()
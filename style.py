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

with st.sidebar:
        st.divider() # 区切り線
        
        # 1. 学習ステップ（今の進み具合を視覚化）
        st.caption("🚀 学習ロードマップ")
        # 4つのページがあるので、3つ目まで来たということで75%に設定
        st.progress(75, text="現在は「AI応用」フェーズ") 
        
        # 2. システムの状態（🟢を使って「正常に動いている」ことをアピール）
        st.markdown("""
        <div style='font-size: 0.8rem; color: #666666; background-color: #ffffff; padding: 10px; border-radius: 10px; border: 1px solid #e0e0e0;'>
        <b>💻 システム稼働状況</b><br>
        🟢 データベース: 接続済み<br>
        🟢 AIエンジン: 待機中 (GPT-4o)<br>
        🔵 環境: Mac mini M4 Pro
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # 3. ワンポイントアドバイス（親切心をアピール）
        st.caption("💡 今日のSQLヒント")
        st.info("JOIN（結合）のコツは、2つの表をつなぐ『接着剤（共通の列）』を見つけることです。")
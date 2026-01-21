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

        /* 2. 入力枠：二重線を完全に解消 */
        div[data-baseweb="input"], div[data-baseweb="textarea"] {
            border: none !important;
        }
        .stTextArea textarea, .stTextInput input {
            border: 1px solid #e0e0e0 !important;
            border-radius: 10px !important;
            background-color: #ffffff !important;
            transition: all 0.3s ease;
        }
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: #6e8efb !important;
            box-shadow: 0 0 0 2px rgba(110, 142, 251, 0.2) !important;
            outline: none !important;
        }

        /* サイドバーの背景色 */
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa;
        }
    </style>
    """, unsafe_allow_html=True)

    # サイドバーのコンテンツ
    with st.sidebar:
        st.markdown("## 🚀 SQL学習ロードマップ")
        
        # 全体の進捗バー
        st.progress(75, text="現在は「Step 3: AI応用」フェーズ") 
        
        # 学習ステップのマイルストーン（詳細説明入り）
        st.markdown("""
        <div style='font-size: 0.85rem; line-height: 1.7; background-color: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #eef2f6; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>
            <b style='color: #6e8efb;'>Step 1: 🔰 Playground</b><br>
            <span style='color: #666;'>【基本】SQLの基本操作をマスター</span><br>
            <hr style='margin: 8px 0; border: 0; border-top: 1px solid #eee;'>
            
            <b style='color: #6e8efb;'>Step 2: 🔗 Join Master</b><br>
            <span style='color: #666;'>【結合】表のつながりを視覚的に理解</span><br>
            <hr style='margin: 8px 0; border: 0; border-top: 1px solid #eee;'>
            
            <b style='color: #2e59d9; font-size: 0.95rem;'>Step 3: 🤖 AI Search</b><br>
            <span style='color: #000; font-weight: bold;'>【応用】自然言語での高度なデータ分析</span><br>
            <hr style='margin: 8px 0; border: 0; border-top: 1px solid #eee;'>
            
            <b style='color: #bbb;'>Step 4: 📝 Quiz Drill</b><br>
            <span style='color: #bbb;'>【総仕上げ】習得度チェック（準備中）</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        # 今日の学習ヒント
        st.caption("💡 今日の学習ヒント")
        st.info("SQLは『どの表から(FROM)』『どの列を(SELECT)』選ぶか、という構造を意識するのが上達の近道です。")
import streamlit as st

def apply_custom_css(progress_val=0):
    """アプリ全体のモダンデザインとサイドバーの装飾を一括適用"""
    
    # プログレスバーが「満タン」になるのを防ぐための補正
    # 1.0より大きい（25など）場合は100で割って 0.25 に変換する
    if progress_val > 1.0:
        display_val = progress_val / 100.0
    else:
        display_val = progress_val

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

        /* サイドバーの背景色をパステルブルーに変更 */
        section[data-testid="stSidebar"] {
            background-color: #eef2f6 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # サイドバーのコンテンツ
    with st.sidebar:
        st.title("🎓 SQL学習アプリ")
        
        st.caption("📈 学習の進捗")
        
        # メッセージ判定（progress_valが整数の場合でも動作するように判定）
        p_check = progress_val if progress_val > 1.0 else progress_val * 100
        
        if p_check <= 25:
            status_text = "Step 1: 🔰 基本フェーズ"
        elif p_check <= 50:
            status_text = "Step 2: 🔗 結合マスター"
        elif p_check <= 75:
            status_text = "Step 3: 🤖 AI分析（応用）"
        elif p_check <= 100:
            status_text = "Step 4: 📝 Quiz Drill（総仕上げ）"
        else:
            status_text = "学習完了！"
            
        # 補正後の display_val を使って描画
        st.progress(display_val, text=status_text)  
      
        st.divider()
        
        # 今日のヒント
        st.caption("💡 今日の学習ヒント")
        st.info("SQLは『どの表から(FROM)』『どの列を(SELECT)』選ぶか、という構造を意識するのが上達の近道です。")
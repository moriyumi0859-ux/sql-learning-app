import streamlit as st
import pandas as pd
from utils import run_query
from style import apply_custom_css  # style.pyを読み込み

# 1. ページ設定とデザイン適用
if 'layout_set' not in st.session_state:
    st.set_page_config(layout="wide")
    st.session_state.layout_set = True

apply_custom_css()  # 立体的なボタンなどのデザインを適用

st.title("🔗 テーブル結合（JOIN）マスター")

# 2. イントロダクション（より分かりやすく！）
with st.expander("📖 はじめての方へ：このページの使い方", expanded=True):
    st.write("""
    このページは、**「2つのバラバラな名簿を、1つに合体させる方法」**を学ぶ場所です。
    1. **ステップ1**：左にいる「鈴木さん（人事部）」に注目してください。
    2. **ステップ2**：ボタンを切り替えてみましょう。
    3. **ステップ3**：鈴木さんが**「消える」**か**「空欄で残る」**かを確認してください。
    """)

st.divider()

# 3. 元データの表示
st.subheader("ステップ1：元のデータを見てみよう")
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("👤 **A: ユーザー名簿**")
    df_a = run_query("SELECT name as 氏名, department as 部署 FROM users")
    if isinstance(df_a, pd.DataFrame):
        # 💡 改善：詳細表示（虫眼鏡）などを無効化してシンプルにする
        st.dataframe(df_a, use_container_width=True, hide_index=True, selection_mode="disallowed")
    st.warning("⚠️ 鈴木さんは「人事部」ですが、右側のリストに人事部はありますか？")

with col_b:
    st.markdown("🏢 **B: 部署の場所リスト**")
    dept_display = pd.DataFrame({
        '部署': ['営業', '開発'],
        '勤務地': ['東京', '大阪']
    })
    st.dataframe(dept_display, use_container_width=True, hide_index=True, selection_mode="disallowed")

st.divider()

# 4. 操作パネル
st.subheader("ステップ2：合体のルールを選ぼう")
join_type = st.radio(
    "どうやって合体させますか？",
    ("共通点がある人だけ残す (INNER JOIN)", "名簿の全員を残して、場所を付け足す (LEFT JOIN)"),
    horizontal=True
)

st.divider()

# 5. 実行と解説
st.subheader("ステップ3：実行されたSQLと結果")

if "INNER" in join_type:
    status_msg = "🚫 **INNER JOIN：鈴木さんは除外されました**"
    explanation = "両方の表に『部署名』がある人だけを合体させるルールです。場所リストにない『人事部』の鈴木さんは消えてしまいます。"
    query = """SELECT u.name as 氏名, u.department as 部署, d.l as 勤務地
FROM users u
INNER JOIN (
    SELECT '営業' as d_name, '東京' as l 
    UNION SELECT '開発', '大阪'
) d ON u.department = d.d_name;"""
    color = "error" # 赤色系
else:
    status_msg = "✅ **LEFT JOIN：鈴木さんも残りました！**"
    explanation = "左側の名簿を優先するルールです。場所がわからなくても鈴木さんを表示し、勤務地は空っぽ（NULL）になります。"
    query = """SELECT u.name as 氏名, u.department as 部署, d.l as 勤務地
FROM users u
LEFT JOIN (
    SELECT '営業' as d_name, '東京' as l 
    UNION SELECT '開発', '大阪'
) d ON u.department = d.d_name;"""
    color = "success" # 緑色系

# 状態を分かりやすく表示
if "INNER" in join_type:
    st.error(status_msg)
else:
    st.success(status_msg)

st.info(f"💡 **解説:** {explanation}")

st.markdown("##### 📝 この結果を作るためのSQLコード")
st.code(query, language="sql") 

st.markdown("##### 📊 合体した後の表")

# 実行結果
result = run_query(query)
if isinstance(result, pd.DataFrame):
    # 💡 改善：ここでも虫眼鏡（詳細表示）を無効化して、混乱を防ぐ
    st.dataframe(result, use_container_width=True, hide_index=True, selection_mode="disallowed")
else:
    st.error(f"SQLの実行に失敗しました。エラー内容: {result}")

with st.expander("🔍 SQLの命令を日本語で詳しく読む"):
    st.write("""
    - **SELECT**: 取り出したい項目（名前、部署、場所）。
    - **FROM**: メインの表（ユーザー名簿）。
    - **INNER / LEFT JOIN**: 合体のルール（厳しい合体か、優しい合体か）。
    - **ON**: 接着剤にする項目（部署名）。
    """)
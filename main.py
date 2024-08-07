import streamlit as st

# アプリのタイトル
st.title("4択クイズアプリ")

# 質問と選択肢を定義
quiz_data = [
    {
        "question": "フランスの首都はどこですか？",
        "options": ["ベルリン", "パリ", "ローマ", "マドリード"],
        "answer": "パリ"
    },
    {
        "question": "赤い惑星として知られているのはどれですか？",
        "options": ["地球", "火星", "木星", "土星"],
        "answer": "火星"
    },
    {
        "question": "『ハムレット』を書いたのは誰ですか？",
        "options": ["マーク・トウェイン", "ウィリアム・シェイクスピア", "チャールズ・ディケンズ", "レフ・トルストイ"],
        "answer": "ウィリアム・シェイクスピア"
    },
    {
        "question": "地球上で最も大きな海はどれですか？",
        "options": ["大西洋", "インド洋", "北極海", "太平洋"],
        "answer": "太平洋"
    }
]

# スコアの初期化
score = 0

# クイズデータの各質問をループで処理
for i, q in enumerate(quiz_data):
    st.subheader(f"質問 {i + 1}: {q['question']}")
    # デフォルトの選択肢は何も選ばれていない状態にする
    user_answer = st.radio("答えを選んでください:", ["選択してください"] + q['options'], key=i)

    # ユーザーが「選択してください」を選んだ場合、処理をスキップ
    if user_answer == "選択してください":
        continue

    # 答えが正しいかをチェック
    if user_answer == q['answer']:
        st.success("正解です！")
        score += 1
    else:
        st.error(f"不正解です。正しい答えは「{q['answer']}」です。")

# 最終スコアの表示
st.write(f"あなたの最終スコアは {score}/{len(quiz_data)} です。")

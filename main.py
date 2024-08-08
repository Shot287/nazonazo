import streamlit as st

# アプリのタイトル
st.title("英語　文法クイズ　１２問")

# 質問と選択肢を定義
quiz_data = [
    {"question": "She is ( ) regarded for her achievements in the IT industry.", "options": ["high", "highly", "height", "heighten"], "answer": "highly"},
    {"question": "The agreement was entirely ( ) to our shareholders.", "options": ["accept", "acceptable", "acceptably", "acceptance"], "answer": "acceptable"},
    {"question": "We would appreciate it if you would consider ( ) at our hotel next time.", "options": ["staying", "stayed", "to stay", "stays"], "answer": "staying"},
    {"question": "Some enthusiastic politicians ( ) global environment issues.", "options": ["talked", "said", "spoke", "discussed"], "answer": "discussed"},
    {"question": "The store manager distributed the promotional flyers ( ).", "options": ["he", "his", "him", "himself"], "answer": "himself"},
    {"question": "We have ( ) information about the candidates.", "options": ["many", "little", "every", "several"], "answer": "little"},
    {"question": "Ivan lost his notes. ( ), he made a great speech.", "options": ["If", "Moreover", "Although", "Nevertheless"], "answer": "Nevertheless"},
    {"question": "( ) you install a navigation system, you will never get lost anymore", "options": ["Despite", "Once", "However", "Since"], "answer": "Once"},
    {"question": "This e-mail explains ( ) candidates must prepare for their job interview.", "options": ["whom", "what", "who", "whose"], "answer": "what"},
    {"question": "Companies ( ) export their goods have increased sales sharply.", "options": ["that", "whose", "whom", "what"], "answer": "that"},
    {"question": "We were given an award for achieving the ( ) sales in 10 years.", "options": ["highest", "high", "higher", "highly"], "answer": "highest"},
    {"question": "Construction of the new hotel took ( ) longer than originally planned.", "options": ["more", "far", "too", "very"], "answer": "far"}
]

# スコアの初期化
score = 0

# クイズデータの各質問をループで処理
for i, q in enumerate(quiz_data):
    st.subheader(f"問題 {i + 1}: {q['question']}")
    # ユーザーの回答を取得
    user_answer = st.radio("答えを選んでください:", ["選択してください"] + q['options'], key=i)

    # ユーザーが「選択してください」を選んだ場合、処理をスキップ
    if user_answer == "選択してください":
        continue

    # 答えが正しいかをチェック
    if user_answer == q['answer']:
        st.success("正解です！")
        score += 1
    else:
        st.error("不正解です。")

# 最終スコアの表示
st.write(f"あなたの最終スコアは {score}/{len(quiz_data)} です。")

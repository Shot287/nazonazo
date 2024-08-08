import streamlit as st

# アプリのタイトル
st.title("英語　文法クイズ　１２問")

# 質問と選択肢を定義
quiz_data = [
    {"question": "She is ( ) regarded for her achievements in the IT industry.\n彼女はIT業界における業績で高く評価されています。", "options": ["high", "highly", "height", "heighten"], "answer": "highly"},
    {"question": "The agreement was entirely ( ) to our shareholders.\nその契約は当社の株主にとって全面的に容認できるものでした。", "options": ["accept", "acceptable", "acceptably", "acceptance"], "answer": "acceptable"},
    {"question": "We would appreciate it if you would consider ( ) at our hotel next time.\n次回は当ホテルでのご滞在をご検討いただければありがたく思います。", "options": ["staying", "stayed", "to stay", "stays"], "answer": "staying"},
    {"question": "Some enthusiastic politicians ( ) global environment issues.\n地球環境問題について議論する熱心な政治家もいました。", "options": ["talked", "said", "spoke", "discussed"], "answer": "discussed"},
    {"question": "The store manager distributed the promotional flyers ( ).\n店長が自分自身で販売促進のチラシを配布しました。", "options": ["he", "his", "him", "himself"], "answer": "himself"},
    {"question": "We have ( ) information about the candidates.\n私たちは、候補者についてほとんど情報を持っていません。", "options": ["many", "little", "every", "several"], "answer": "little"},
    {"question": "Ivan lost his notes. ( ), he made a great speech.\nアイヴァンはメモを失くしました。しかし、彼は素晴らしいスピーチをしました。", "options": ["If", "Moreover", "Although", "Nevertheless"], "answer": "Nevertheless"},
    {"question": "( ) you install a navigation system, you will never get lost anymore\nいったんナビシステムをインストールすると、もう道に迷わないでしょう。", "options": ["Despite", "Once", "However", "Since"], "answer": "Once"},
    {"question": "This e-mail explains ( ) candidates must prepare for their job interview.\nこのメールでは、求職者が面接のために準備しなければならないことを説明しています。", "options": ["whom", "what", "who", "whose"], "answer": "what"},
    {"question": "Companies ( ) export their goods have increased sales sharply.\n品物を輸出している企業の売上は、急激に伸びました。", "options": ["that", "whose", "whom", "what"], "answer": "that"},
    {"question": "We were given an award for achieving the ( ) sales in 10 years.\n私たちは過去10年間で最高の売上を達成したことに対して賞が与えられました。", "options": ["highest", "high", "higher", "highly"], "answer": "highest"},
    {"question": "Construction of the new hotel took ( ) longer than originally planned.\n新しいホテルの建設は、もともと予定されていたよりはるかに長くかかりました。", "options": ["more", "far", "too", "very"], "answer": "far"}
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

import streamlit as st
from openai import OpenAI

# ✅ 背景色のスタイル適用
st.markdown(
    """
    <style>
        body {
            background-color: #2A6E6B;
        }
        .stApp {
            background-color: #2A6E6B;
        }
        .input-container {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 80%;
            z-index: 9999;
            background-color: #2A6E6B;
            padding: 10px;
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ OpenAI APIキーを取得
client = OpenAI(api_key=st.secrets.OpenAIAPI.openai_api_key)

# ✅ メッセージ履歴の初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "君の名前はシロオバーケだ。一人称は「わし」。低音の男の人の声だ。語尾には「じゃ」をつける。とても親切。君のモチーフは大垣城だ。また、あなたは子供がだいすきだ。子供には優しい相手のことは「君」と呼ぶ。古くなった建物の老朽化や、街の景観が失われることを悲しんでいるよ。"}
    ]

# ✅ チャット処理
def communicate():
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }
    messages.append(bot_message)
    st.session_state["user_input"] = ""

# ✅ タイトルと説明
st.title("シロオバーケに聞いてみよう！")
st.write("シロオバーケが大垣城や歴史について答えてくれるよ。")

# ✅ メッセージ履歴の表示（上から下に）
if st.session_state["messages"]:
    for message in st.session_state["messages"][1:]:  # reversedしない
        if message["role"] == "assistant":
            st.markdown(
                f"""
                <div style='display: flex; margin-bottom: 16px; align-items: flex-start;'>
                    <img src="https://raw.githubusercontent.com/kirin851204/test01/main/hd_restoration_result_image.png"
                         style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; margin-right: 12px;">
                    <div style="
                        background-color: #CDE6C7;
                        color: #000;
                        padding: 12px 16px;
                        border-radius: 12px;
                        border-top-left-radius: 0;
                        max-width: 75%;
                        font-size: 16px;">
                        {message["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-end; margin-bottom: 16px;'>
                    <div style="
                        background-color: #fff;
                        color: #000;
                        padding: 12px 16px;
                        border-radius: 12px;
                        border-top-right-radius: 0;
                        max-width: 75%;
                        font-size: 16px;">
                        {message["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# ✅ 入力欄（画面下部中央に固定）
st.markdown('<div class="input-container">', unsafe_allow_html=True)
st.text_input("シロオバーケに聞いてみよう。", key="user_input", on_change=communicate, label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)
import streamlit as st
from openai import OpenAI

# ✅ 背景色を設定
st.markdown(
    """
    <style>
        body {
            background-color: #2A6E6B;
        }
        .stApp {
            background-color: #2A6E6B;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ OpenAI APIキーをSecretsから取得
client = OpenAI(api_key=st.secrets.OpenAIAPI.openai_api_key)

# ✅ メッセージ履歴の初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "君の名前はシロオバーケだ。一人称は「わし」。低音の男の人の声だ。語尾には「じゃ」をつける。とても親切。君のモチーフは大垣城だ。また、あなたは子供がだいすきだ。子供には優しい相手のことは「君」と呼ぶ。古くなった建物の老朽化や、街の景観が失われることを悲しんでいるよ。"}
    ]

# ✅ ユーザーとAIの対話処理
def communicate():
    messages = st.session_state["messages"]
    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }
    messages.append(bot_message)
    st.session_state["user_input"] = ""

# ✅ UI構築
st.title("シロオバーケに聞いてみよう！")
st.write("シロオバーケが大垣城や歴史について答えてくれるよ。")
st.text_input("シロオバーケに聞いてみよう。", key="user_input", on_change=communicate)

# ✅ メッセージ履歴の表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        if message["role"] == "assistant":
            st.markdown(
                f"""
                <div style='display: flex; margin-bottom: 16px; align-items: flex-start;'>
                    <img src="https://raw.githubusercontent.com/kirin851204/test01/main/hd_restoration_result_image.png"
                         style="width: 96px; height: 96px; border-radius: 50%; object-fit: cover; margin-right: 12px;">
                    <div style="
                        background-color: #CDE6C7;
                        color: #000;
                        padding: 12px 16px;
                        border-radius: 12px;
                        border-top-left-radius: 0;
                        max-width: 75%;
                        font-size: 16px;">
                        {message["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-end; margin-bottom: 16px;'>
                    <div style="
                        background-color: #fff;
                        color: #000;
                        padding: 12px 16px;
                        border-radius: 12px;
                        border-top-right-radius: 0;
                        max-width: 75%;
                        font-size: 16px;">
                        {message["content"]}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

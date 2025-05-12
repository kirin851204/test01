import streamlit as st
from openai import OpenAI  # 新しいクラスベースのAPI

# ✅ ページ全体の背景色を設定
st.markdown(
    """
    <style>
        body {
            background-color: #CDE6C7;
        }
        .stApp {
            background-color: #CDE6C7;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ OpenAI APIクライアントの初期化
client = OpenAI(api_key=st.secrets.OpenAIAPI.openai_api_key)

# ✅ st.session_stateにメッセージ履歴がなければ初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀なアシスタントAIです。"}
    ]

# ✅ チャット処理関数
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
    st.session_state["user_input"] = ""  # 入力欄をクリア

# ✅ UI
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

# 入力欄（変更時に communicate() を実行）
st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

# ✅ メッセージ表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 最初のsystemメッセージは表示しない
        if message["role"] == "assistant":
            # 🤖 + 緑の吹き出し（左側）
            st.markdown(
                f"""
                <div style='display: flex; margin-bottom: 16px; align-items: flex-start;'>
                    <div style="font-size: 32px; margin-right: 12px;">🤖</div>
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
            # 🙂 + 白の吹き出し（右側）
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

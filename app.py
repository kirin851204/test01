import streamlit as st
from openai import OpenAI

# ✅ 背景色を設定
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

# ✅ OpenAI APIキーをSecretsから取得
client = OpenAI(api_key=st.secrets.OpenAIAPI.openai_api_key)

# ✅ メッセージ履歴の初期化
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀なアシスタントAIです。"}
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
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")
st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

# ✅ メッセージ履歴の表示
if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        if message["role"] == "assistant":
            # AIの吹き出し：丸い画像＋緑背景
            st.markdown(
                f"""
                <div style='display: flex; margin-bottom: 16px; align-items: flex-start;'>
                    <img src="https://raw.githubusercontent.com/kirin851204/test01/main/hd_restoration_result_image.png"
                         style="width: 48px; height: 48px; border-radius: 50%; object-fit: cover; margin-right: 12px;">
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
            # ユーザーの吹き出し：右寄せ＋白背景
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

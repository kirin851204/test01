import streamlit as st
from openai import OpenAI  # 新しいクラスベースのAPI

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
client = OpenAI(api_key=st.secrets.OpenAIAPI.openai_api_key)

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "あなたは優秀なアシスタントAIです。"}
    ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    # 新しいAPI形式
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去

# ✅ 中央に画像を表示（修正済みURL）
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://raw.githubusercontent.com/kirin851204/test01/main/%E3%82%B7%E3%83%AD%E3%82%AA%E3%83%90%E3%83%BC%E3%82%B1.jpg' width='240'/>
    </div>
    """,
    unsafe_allow_html=True
)

# アプリタイトル
st.title("My AI Assistant")
st.write("ChatGPT APIを使ったチャットボットです。")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        if message["role"] == "assistant":
            st.markdown(
                f"""
                <div style='display: flex; align-items: center; margin-bottom: 10px;'>
                    <img src="https://raw.githubusercontent.com/kirin851204/test01/main/%E3%82%B7%E3%83%AD%E3%82%AA%E3%83%90%E3%83%BC%E3%82%B1.jpg" width="32" style="margin-right: 10px;">
                    <span>{message["content"]}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.write("🙂: " + message["content"])

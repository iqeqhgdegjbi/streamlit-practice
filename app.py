import langchain
from langchain_openai import ChatOpenAI
import streamlit as st

st.title("LLM機能を搭載したWebアプリ")

st.write("##### テスト")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["ChatGPTと会話してみよう！"]
)

st.divider()

llm = ChatOpenAI(
    api_key=st.secrets["OEPNAI_API_KEY"]
)


if selected_item == "ChatGPTと会話してみよう！":
    input_message = st.text_input(label="気になることを聞いてみよう！")
    text_count = input_message

if st.button("実行"):
    st.divider()

    if selected_item == "ChatGPTと会話してみよう！":
        if input_message:
            response = llm.invoke(input_message).text()
            st.write(f"ChatGPTからのお言葉: **{response}**")
        else:
            st.error("質問を入力してから「実行」ボタンを押してください。")
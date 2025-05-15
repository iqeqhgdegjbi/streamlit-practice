import langchain
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st


def get_llm_answer(input_message, selected_item):
    llm = ChatOpenAI(
        api_key=st.secrets["OPENAI_API_KEY"]    
    )

    if input_message:
        pass
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")

    messages = []

    if selected_item == "お笑いの専門家":
        messages = [
            SystemMessage("あなたはお笑いの専門家です。ユーザーからの下記質問に答えてください"),
            HumanMessage(input_message)
        ]
    elif selected_item == "スポーツの専門家":
        messages = [
            SystemMessage("あなたはお笑いの専門家です。ユーザーからの下記質問に答えてください"),
            HumanMessage(input_message)
        ]
    
    answer = llm.invoke(messages).text()

    return answer


st.title("LLM機能を搭載したWebアプリ")
st.write("##### テスト")
st.text_area(
    label="説明",
    value="""このツールでは、質問や相談内容を入力することで、AIが専門家の立場からアドバイスをしてくれます。
使い方はかんたんです。まず、入力欄に質問や相談内容を入力します。
次に、どの専門家に答えてほしいかを選びます。
その後、送信ボタンを押すと、選んだ専門家になりきったAIが回答を表示してくれます。
専門家の視点から、あなたの悩みや疑問に合わせたアドバイスが得られる便利なツールです。
お気軽にご利用ください。
"""
    , height=250
)

selected_item = st.radio(
    "動作モードを選択してください。",
    [
        "お笑いの専門家",
        "スポーツの専門家"
    ]
)

st.divider()

input_message = st.text_input(label="気になることを聞いてみよう！")
text_count = input_message


if st.button("実行"):
    st.divider()

    answer = get_llm_answer(
        input_message=input_message, 
        selected_item=selected_item
    )

    st.write(f"ChatGPTからのお言葉: **{answer}**")

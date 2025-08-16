from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st
import os


api_key = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-4o-mini",
                 temperature=0.5, openai_api_key=api_key)

st.title("課題用フォームの作成webアプリ")
st.write("このアプリは、OpenAIのAPIを使用して、課題用のフォームを作成するためのものです。")
st.write("以下のフォームに必要な情報を入力してください。")

selected_item = st.radio("選択してください", ["ITの専門家", "料理の専門家", "数学の専門家"])
st.divider()

input_text = st.text_input(label=f"{selected_item}に関する情報を入力してください")


def get_ai_response(selected_item, input_text):
    role_dict = {  # 選択肢ごとにAIの役割を指定する辞書
        "料理の専門家": "あなたは料理の専門家です。料理以外の質問には答えず、「料理以外の質問には答えられません」と返答してください。",
        "ITの専門家": "あなたはITの専門家です。IT以外の質問には答えないでください。",
        "数学の専門家": "あなたは数学の専門家です。数学以外の質問には答えないでください。"
    }
    messages = [
        SystemMessage(content=role_dict[selected_item]),
        HumanMessage(content=input_text)
    ]
    response = llm(messages)
    return response.content


if st.button("送信"):
    st.divider()
    if input_text:
        answer = get_ai_response(selected_item, input_text)
        st.write("AIの回答:")
        st.write(answer)
    else:
        st.write(f"{selected_item}に関する情報を入力してください。")

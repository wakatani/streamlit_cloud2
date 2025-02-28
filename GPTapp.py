#
# Google Colaboratoryで実行する場合には、事前に、シークレットに、
# OPENAI_API_KEYのキーに対して、APIキーを値でセットしておく必要がある
#
from math import exp
import json
from openai import OpenAI
#from dotenv import load_dotenv
import os
import random
import streamlit as st

# 環境変数のロード
#load_dotenv()

#from google.colab import userdata
#os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] ="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"

client = OpenAI()

#
# 問題作成の元になる文章群
#
explanationList=[
    "東灘区にある阪神電鉄の駅は、深江、青木、魚崎、住吉、御影、石屋川です",
    "東灘区にある阪急電鉄の駅は、岡本、御影です",
    "コンパイラのフロントエンド部分には字句解析と構文解析が含まれます",
    "C言語はコンパイラ言語ですが、Python言語はインタプリタ言語です",
    "BNFで文法を表現する場合、終端記号と非終端記号が使われる",
    "LLパーザを用いた構文解析が利用できる文法は左再帰を含みません",
    "コンパイラ言語は高速ですが、インタプリタ言語は遅いです"
]
#
# 文章群から文章をランダムに選ぶ
#
if st.button('問題'):
  explanation=explanationList[int(random.random()*len(explanationList))]

  response1 = client.chat.completions.create(
    model="gpt-4o-2024-08-06",
    temperature=0.8,
    messages=[{"role": "user",\
               "content": "「{0}」の文章に関する4択問題の4個の選択肢の文言とその答の番号を示せ。選択肢の文言は選択肢の番号は不要である。".format(explanation)}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "quiz_data",
            "schema": {
                "type": "object",
                "properties": {
                    "選択肢１": {"type": "string"},
                    "選択肢２": {"type": "string"},
                    "選択肢３": {"type": "string"},
                    "選択肢４": {"type": "string"},
                    "答え": {"type": "number"},
                },
                "required": ["選択肢１", "選択肢２", "選択肢３", "選択肢４","答え"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
  )

  quiz_response = json.loads(response1.choices[0].message.content)


  msg=quiz_response
  #st.write(msg)
  msg="-----------------------------------------------------"
  st.write(msg)
  msg="次の選択肢から正しいものを選べ"
  st.write(msg)
  msg="１：{0}".format(quiz_response["選択肢１"])
  st.write(msg)
  msg="２：{0}".format(quiz_response["選択肢２"])
  st.write(msg)
  msg="３：{0}".format(quiz_response["選択肢３"])
  st.write(msg)
  msg="４：{0}".format(quiz_response["選択肢４"])
  st.write(msg)
  msg="-----------------------------------------------------"
  st.write(msg)
  msg="-----------------------------------------------------"
  st.write(msg)
  msg="答えは{0}です。".format(quiz_response["答え"])
  st.write(msg)
  msg="  [ {0} ]".format(explanation)
  st.write(msg)
  msg="-----------------------------------------------------"



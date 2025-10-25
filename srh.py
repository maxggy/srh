import streamlit
from PIL import Image
import os
from openai import OpenAI
a=0
streamlit.snow()
streamlit.header(":rainbow[我是聊天AI，星尘]")
streamlit.header(":rainbow[请问有什么可以帮住你的吗？]:smile:",divider="rainbow")
if "messages" not in streamlit.session_state:
    streamlit.session_state.messages = []
for message in streamlit.session_state.messages:
    with streamlit.chat_message(message["role"]):
        streamlit.markdown(message["content"]) 
if streamlit.sidebar.button('清空历史对话'):
    streamlit.session_state.messages = []
    streamlit.rerun()
streamlit.sidebar.text_area("安全提示：",value="请输入合理合法的问题",label_visibility="visible")
abc = streamlit.sidebar.button("背景",type="primary",use_container_width=False)
if abc:
    streamlit.snow()
chat = streamlit.chat_input("给星尘发送信息")
if chat:
    with streamlit.chat_message("user"):
        streamlit.markdown(chat)
    streamlit.session_state.messages.append({"role":"user","content":chat})
    client = OpenAI(
    api_key='sk-caa08ff7e9c64786b45e9b98ec281ee1',
    base_url="https://api.deepseek.com"
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": chat},
        ],
        stream=False
    )
    streamlit.markdown(response.choices[0].message.content)
    streamlit.session_state.messages.append({"role":"assistant","content":response.choices[0].message.content})
y=0
x=streamlit.sidebar.text_input("账号",type="default",label_visibility="visible")
if x=="SRH":
    y+=1
t=streamlit.sidebar.text_input("密码",type="password",label_visibility="visible")
if t=="12345678987654321010203040506070809080706050403020101357924681012345678912345678913579246810":
    y+=1
result = streamlit.sidebar.button("登录",type="primary",use_container_width=False)
if y==2:
    streamlit.sidebar.markdown('密码正确')
else:
    streamlit.sidebar.markdown('密码错误')
    y==0
streamlit.sidebar.markdown('导航：')
streamlit.sidebar.link_button("DeepSeek","https://www.deepseek.com/")
streamlit.sidebar.link_button("百度","https://www.baidu.com/")
pinlun = streamlit.sidebar.radio("你觉的这些回答有用吗",["有用","一般","没用"],captions=["值得鼓励","继续努力","需要提升"])
streamlit.sidebar.write("您觉得",pinlun)
    

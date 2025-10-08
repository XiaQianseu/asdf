import streamlit as st

st.title("我的第一个 Streamlit 网页,哈哈哈哈")
st.write("这是一个网页，而不是桌面窗口。")

x = st.number_input("输入一个数", 0, 100, 10)
y = st.number_input("再输入一个数", 0, 100, 20)


st.write("两数之和是：", x + y)
